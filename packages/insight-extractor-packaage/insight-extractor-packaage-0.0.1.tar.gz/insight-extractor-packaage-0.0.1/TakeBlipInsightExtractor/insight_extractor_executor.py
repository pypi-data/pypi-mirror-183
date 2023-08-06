import os
import sys
import json
import uuid
import shutil
import logging
import traceback
from mlflow.tracking import MlflowClient
from TakeBlipInsightExtractor.insight_extractor import InsightExtractor
from TakeBlipInsightExtractor.outputs.eventhub_log_sender \
    import EventHubLogSender


def read_json_file(root: str, file_name: str) -> dict:
    """Reads a .json file from root/file_name.

    Args:
       root (str): a string with file root path
       file_name (str): a string with file name

    Returns (Dict):
       A dictionary read .from json file
    """
    filename = os.path.join(root, file_name)
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


secrets = read_json_file(os.path.dirname(os.getcwd()),
                         'secrets.json')

class InsightExtractorExecutor:
    def __init__(self,
                 user_email,
                 bot_name,
                 embedding_model_path,
                 output_files_path):
        self.logger = None
        self.insight_extractor = None
        self.user_email = user_email
        self.bot_name = bot_name
        self.embedding_model_path = embedding_model_path
        self.output_files_path = output_files_path
        self.root_path = os.path.join(os.getcwd(), 'default_models')
        self.initialize_eventhub_logger()
        self.initialize_insight_extractor()

    def initialize_eventhub_logger(self):
        try:
            correlation_id = str(uuid.uuid3(uuid.NAMESPACE_DNS,
                                            self.user_email + self.bot_name))

            self.logger = EventHubLogSender(
                application_name='Insight Extractor Package',
                user_email=self.user_email,
                bot_name=self.bot_name,
                file_name='file_name',
                correlation_id=correlation_id,
                connection_string=secrets.get('EVENTHUB_CONNECTION_STRING'),
                eventhub_name=secrets.get('EVENTHUB_NAME')
            )
        except (Exception) as e:
            logging.error(
                'Error {} while initializing Event Hub Logger!'.format(e))

    def initialize_insight_extractor(self):
        self.insight_extractor = InsightExtractor(
            input_data='file',
            separator=',',
            similarity_threshold=0.65,
            embedding_path=self.embedding_model_path,
            postagging_model_path=os.path.join(self.root_path, 'model.pkl'),
            postagging_label_path=os.path.join(self.root_path, 'vocab-label.pkl'),
            ner_model_path=os.path.join(self.root_path, 'nermodel.pkl'),
            ner_label_path=os.path.join(self.root_path, 'ner-vocab-label.pkl'),
            user_email=self.user_email,
            bot_name=self.bot_name,
            use_neighborhood=True,
            logger=self.logger,
            datalake_connector=None,
        )

    def copy_files(self):
        for file in self.insight_extractor.output_files_dict.values():
            shutil.copyfile(os.path.join(os.getcwd(), file),
                            os.path.join(self.output_files_path, file))

    def remove_files(self):
        try:
            self.logger.log_message('DEBUG', 'Removing local files. ')
            for file in self.insight_extractor.output_files_dict.values():
                os.remove(file)
            self.logger.log_message('DEBUG', 'Local files removed. ')
        except Exception as e:
            self.logger.log_error_message('ERROR',
                                     'Error {} while removing files'.format(e))

    def analyze(self, messages):
        self.insight_extractor.predict(percentage_threshold=0.5,
                                  node_messages_examples=10,
                                  batch_size=100,
                                  messages=messages[:1000])
        self.copy_files()
        self.remove_files()




from hate.logger import logging
from hate.exception import CustomException
import sys
#logging.info("welcome to our project")
from hate.configuration.gcloud_syncer import GCloudSync
obj=GCloudSync()
obj.sync_folder_from_gcloud("hate_speech_recognition","dataset.zip","download/dataset.zip")
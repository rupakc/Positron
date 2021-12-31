import tempfile
import os

LOG_FILE_NAME = 'positron.log'
LOG_FILE_PATH = os.path.join(tempfile.gettempdir(), LOG_FILE_NAME)
DEFAULT_LOG_ROTATION_DAYS = 10

CURRENT_NEWS_BASE_URL = "https://api.currentsapi.services/v1/latest-news"
SUPPORTED_SENTIMENT_PREDICTIONS_LIST = ['positive','negative','neutral']
SUPPORTED_NEWS_CHANNELS_LIST = ['currentnews', 'newsapi']
CURRENT_NEWS_API = 'currentnews'
NEWS_ORG_API = 'newsapi'

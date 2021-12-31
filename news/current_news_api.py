import requests
from config import api_keys
from constants import commonconstants


def get_latest_news_list_json():
    """
    Fetches the list of current news from a set of different news sources

    :return: A list of dictionaries containing the fetched news and the corresponding meta-data
    """
    param_dict = {'language': 'en', 'apiKey': api_keys.CURRENT_NEWS_API_KEY}
    response = requests.get(commonconstants.CURRENT_NEWS_BASE_URL, params=param_dict)
    news_list_json = []
    if response.status_code == 200:
        news_list_json = response.json()['news']
    return news_list_json


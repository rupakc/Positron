from config import api_keys
from newsapi.articles import Articles
from newsapi.sources import Sources
import requests


class News:

    def __init__(self,api_key=api_keys.news['api_key']):
        """
        Constructor to initialize the class with the API Key

        :param api_key: String containing the API Key for authentication
        """
        self.api_key = api_key
        self.article = Articles(self.api_key)
        self.source = Sources(self.api_key)
        self.base_url = api_keys.news['base_everything_url']

    def get_all_sources(self):
        """
        Returns all the news sources currently supported by the API

        :return: List of sources supported
        """
        return self.source.all()

    def get_all_categories(self):
        """
        Returns a list of all categories supported by the API

        :return:A List of all categories supported by the API
        """
        return self.source.all_categories()

    def get_articles(self,source_id,selection_type="popular"):
        """
        Returns a list if articles matching the source_id and the selection criteria

        :param source_id: String containing the source id of the news
        :param selection_type: String containing the criteria of the news (i.e. hot, popular etc.)
        :return: List of articles matching the selection criteria and the source id
        """
        if selection_type == 'latest':
            return self.article.get_by_latest(source_id)
        elif selection_type == 'top':
            return self.article.get_by_top(source_id)
        else:
            return self.article.get_by_popular(source_id)

    def get_query_response(self,query,from_date=None,to_date=None,page_size=100, sort_by='publishedAt',language='en'):
        """
        Given a query string returns the matching news articles

        :param query: String containing the query term
        :param from_date: Start date of the published news
        :param to_date: End date of the published news
        :param page_size: The number of items returned in the response (max 100)
        :param sort_by: sorting criteria of the results (currently by published date)
        :param language: String containing the language of the news articles
        :return: List containing the matched news articles
        """
        if query is None or query == '':
            query = "the"
        key_value_params = {
            'apiKey': self.api_key,
            'q': query,
            'from': from_date,
            'to': to_date,
            'sortBy': sort_by,
            'pageSize': page_size,
            'language': language
        }
        article_json_list = []
        response = requests.get(self.base_url, params=key_value_params)
        if response.status_code == 200:
            article_json_list = response.json()['articles']
        return article_json_list

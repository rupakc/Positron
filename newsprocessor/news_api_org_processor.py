import pandas as pd
from news import news_api_org
from sentiment import vader_sentiment_analyzer
from utils import stringutils

pd.set_option('display.max_colwidth', None)


def format_news_dataframe(sentiment_list_to_filter, search_term=None):
    """
    Given a search term and sentiment list to filter it fetches the data from news channels and analyses them

    :param sentiment_list_to_filter: List containing the sentiment to filter upon
    :param search_term: String containing the term to search for
    :return: HTML String containing the data table and its contents
    """
    news_api = news_api_org.News()
    article_list = news_api.get_query_response(query=search_term)
    news_api_article_dataframe = pd.DataFrame(article_list)
    news_api_article_dataframe.dropna(inplace=True)
    news_api_article_dataframe.sort_values('publishedAt', ascending=False, inplace=True)
    news_api_article_dataframe = news_api_article_dataframe[['title','description','author','url']]
    text_list = list(map(lambda title, description: title + ' ' + description,
                         news_api_article_dataframe['title'],
                         news_api_article_dataframe['description']))
    sentiment_list = vader_sentiment_analyzer.get_sentiment_list(text_list)
    news_api_article_dataframe['sentiment'] = sentiment_list
    filtered_sentiment_frame = news_api_article_dataframe[news_api_article_dataframe['sentiment'].isin(sentiment_list_to_filter)]
    if len(filtered_sentiment_frame) == 0:
        filtered_sentiment_frame = news_api_article_dataframe
    filtered_sentiment_frame.dropna(inplace=True)
    filtered_sentiment_frame['sentiment'] = list(map(stringutils.capitalize_first_letter,
                                                     list(filtered_sentiment_frame['sentiment'].values)))
    filtered_sentiment_frame = filtered_sentiment_frame[['title', 'description', 'author','url', 'sentiment']]
    filtered_sentiment_frame['url'] = list(map(stringutils.add_anchor_tag_to_string,
                                               list(filtered_sentiment_frame['url'].values)))
    return filtered_sentiment_frame.to_html(index=False,escape=False)

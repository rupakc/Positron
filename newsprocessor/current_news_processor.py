import pandas as pd
from news import current_news_api
from utils import stringutils
from sentiment import vader_sentiment_analyzer

pd.set_option('display.max_colwidth', None)


def get_current_news_html(sentiment_list_to_filter):
    """
    Given the list of sentiments to filter upon fetches and analyses current news

    :param sentiment_list_to_filter: List containing the sentiments to filter for
    :return: HTML string (the table representation of a dataframe)
    """
    articles_json = current_news_api.get_latest_news_list_json()
    current_news_frame = pd.DataFrame(articles_json)
    current_news_frame = current_news_frame[['title', 'description', 'author', 'url']]
    current_news_frame = current_news_frame[~current_news_frame['description'].isin(['text/plain...'])]
    text_list = list(map(lambda title,description: title + ' ' + description,
                                                    current_news_frame['title'],
                                                    current_news_frame['description']))
    sentiment_list = vader_sentiment_analyzer.get_sentiment_list(text_list)
    current_news_frame['sentiment'] = sentiment_list
    filtered_sentiment_frame = current_news_frame[current_news_frame['sentiment'].isin(sentiment_list_to_filter)]
    if len(filtered_sentiment_frame) == 0:
        filtered_sentiment_frame = current_news_frame
    filtered_sentiment_frame.dropna(inplace=True)
    filtered_sentiment_frame['sentiment'] = list(map(stringutils.capitalize_first_letter,
                                                     list(filtered_sentiment_frame['sentiment'].values)))
    filtered_sentiment_frame['url'] = list(map(stringutils.add_anchor_tag_to_string,
                                               list(filtered_sentiment_frame['url'].values)))
    return filtered_sentiment_frame.to_html(index=False, escape=False)


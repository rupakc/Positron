from constants import commonconstants
from newsprocessor import current_news_processor, news_api_org_processor


def get_processed_channel_data(search_term, channel_name, sentiment_list):
    """
    Given a search term, channel name and the sentiment list processes the data and returns the corresponding formatted object

    :param search_term: String containing the search term
    :param channel_name: String containing the channel name(i.e. News API source)
    :param sentiment_list: String containing the sentiment list to filter on the news
    :return: HTML table string for each channel
    """
    if channel_name not in commonconstants.SUPPORTED_NEWS_CHANNELS_LIST:
        raise Exception("Channel Name Not Supported")
    if channel_name.lower() == commonconstants.CURRENT_NEWS_API:
        return current_news_processor.get_current_news_html(sentiment_list_to_filter=sentiment_list)
    elif channel_name.lower() == commonconstants.NEWS_ORG_API:
        return news_api_org_processor.format_news_dataframe(sentiment_list_to_filter=sentiment_list,
                                                            search_term=search_term)


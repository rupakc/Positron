from utils import stringutils,logutils
from constants import commonconstants
from flask import session
from newsprocessor import processor_factory
logger = logutils.get_logger(__name__)


def get_social_response_data(request):
    request_form_dict = request.form.to_dict(flat=False)
    search_query = request_form_dict['search_term'][0]
    print(search_query)
    if 'news_data_sources' in request_form_dict.keys():
        data_sources = request_form_dict['news_data_sources']
    else:
        data_sources = commonconstants.SUPPORTED_NEWS_CHANNELS_LIST
    if 'prediction_dropdown' in request_form_dict.keys():
        prediction_types = request_form_dict['prediction_dropdown']
    else:
        prediction_types = commonconstants.SUPPORTED_SENTIMENT_PREDICTIONS_LIST
    response_list = list([])
    print(data_sources)
    logger.debug('News Data Sources: %s' % data_sources)
    print(prediction_types)
    logger.debug('News Sentiment Types: %s' % prediction_types)
    for data_source in data_sources:
        response_data_channel = processor_factory.get_processed_channel_data(search_term=search_query,
                                                                             channel_name=data_source,
                                                                             sentiment_list=prediction_types)
        response_list.append((stringutils.capitalize_first_letter(data_source),response_data_channel))
    return response_list

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_sentiment_list(sentence_list):
    """
    Given a list of sentences determines its sentiment using Vader Sentiment Analyzer

    :param sentence_list: List of sentences whose sentiment has to be determined
    :return: List of sentiment for each sentence
    """
    analyzer = SentimentIntensityAnalyzer()
    sentiment_list = []
    for sentence in sentence_list:
        polarity_scores_dict = analyzer.polarity_scores(sentence)
        compound_score = polarity_scores_dict['compound']
        if compound_score >= 0.05:
            sentiment_list.append("positive")
        elif compound_score <= -0.05:
            sentiment_list.append("negative")
        else:
            sentiment_list.append("neutral")
    return sentiment_list


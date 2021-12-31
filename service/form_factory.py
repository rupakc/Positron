from wtforms import Form, validators, StringField, SelectMultipleField


class NewsText(Form):
    search_term = StringField('search_term', validators=[validators.required()])
    prediction_dropdown = SelectMultipleField('prediction',choices=[('positive','Positive'),
                                                                    ('negative','Negative'),
                                                                    ('neutral','Neutral')],
                                                            validators=[validators.required()])

    news_data_sources = SelectMultipleField('news_data',choices=[('currentnews','Current News API'),
                                                                 ('newsapi','News API Org')],
                                                        validators=[validators.required()])



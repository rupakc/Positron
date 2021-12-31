from flask import Flask, render_template, flash, request, session, send_file
from service import form_factory
from service import request_processor
import warnings
warnings.filterwarnings("ignore")


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True


@app.route("/", methods=['GET', 'POST'])
def root():
    form = form_factory.NewsText(request.form)
    if request.method == 'POST':
        response_list = request_processor.get_social_response_data(request)
        flash(response_list)
    return render_template('text.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

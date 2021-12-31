# Positron
An app for fetching current news in real time and evaluating its sentiment

![architecture image][logo]

[logo]: https://github.com/rupakc/Positron/blob/main/static/resources/positron-architecture.png "System Data Flow"

## System Architecture

The system is built to fetch news from thousands of news servers in real-time. By default it will fetch the news from news.org API and current news API . After collecting and parsing the news, it will perform sentiment analysis on the news. For each news article it will use the title and article description in order to determine its sentiment. Once this is done, it will pass this to the front-end for displaying and rendering. Backend uses Flask server and Python, the UI is built using Bootstrap, JQuery and Javascript.

## Steps to Run the Application

  - Install Python 3
  - Clone the repository
  - Install all the dependencies using - ``` pip install -r requirements.txt ```
  - Start the project by running - ``` python main_form.py ``` this will locally run the flask dev server
  

import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()
    piglatinize_url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    # Send request to https://hidden-journey-62459.herokuapp.com/
    # POST request, form data with 'input_text'
    # Use keyword argument 'follow_redirects=False'
    # response = requests, ...
    response = requests.post(
        piglatinize_url,
        allow_redirects = False,
        data = {'input_text':fact}
    )
    print(dir(response))

    # Get location header from the response
    # location_header = response, ...
    location_header = response.headers['Location']

    return "<a href='{}'>{}</a>".format(location_header, location_header)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)


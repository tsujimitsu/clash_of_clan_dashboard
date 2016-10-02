# coding: utf-8

import flask
import requests
import urllib
import os

AUTH_TOKEN = os.environ['AUTH_TOKEN']
BASE_ENDPOINT = "https://api.clashofclans.com/v1"

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/clans/<clan_tag>', methods=['GET'])
def get_clan(clan_tag):
    clan_tag_encode = urllib.quote_plus(clan_tag)
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + AUTH_TOKEN
    }
    messages = requests.get(BASE_ENDPOINT + "/clans/" + clan_tag_encode, headers=header)
    print messages.json()
    return flask.render_template('get_clan.html', msgs=messages.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080, debug=True)

# coding: utf-8

import flask
from flask.ext.babel import gettext as _
from flask.ext.babel import Babel
import requests
import urllib
import os

AUTH_TOKEN    = os.environ['AUTH_TOKEN']
BASE_ENDPOINT = "https://api.clashofclans.com/v1"
BASE_HEADER   = {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + AUTH_TOKEN
                }

app = flask.Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)


@babel.localeselector
def get_locale():
    return flask.request.accept_languages.best_match(['ja', 'ja_JP', 'en'])

@app.route('/hello')
def hello():
    return _('Hello World!') + _('Test')

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/clans/<clan_tag>', methods=['GET'])
def get_clan(clan_tag):
    clan_tag_encode = urllib.quote_plus(clan_tag)
    messages = api_get_clan(clan_tag_encode)
    return flask.render_template('get_clan.html', msgs=messages.json())

def api_get_clan(clan_tag):
    return requests.get(BASE_ENDPOINT + "/clans/" + clan_tag, headers=BASE_HEADER)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080, debug=True)

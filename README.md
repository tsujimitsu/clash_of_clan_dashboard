Clash of Clan Dashboard
====
* Dashboard for Clash of Clan API

usage
----

    $ git clone https://github.com/tsujimitsu/clash_of_clan_dashboard.git
    $ cd clash_of_clan_dashboard
    $ pip install -r requirements.txt
    $ export AUTH_TOKEN=<YOUR API TOKEN>
    $ python app.py
    $ curl localhost:10080
    $ curl localhost:10080/clans/<clan_tag>
    -> clan_tag must do URL encoding


update translation
----

    $ cd ./clash_of_clan_dashboard
    $ pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
    $ pybabel update -i messages.pot -d translations
    $ vi translations/ja/LC_MESSAGES/messages.po
    -> write translate words
    $ pybabel compile -d translations

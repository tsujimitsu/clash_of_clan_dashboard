Clash of Clan Dashboard
====
* Dashboard for Clash of Clan API

usage
----

    $ git clone https://github.com/tsujimitsu/clash_of_clan_dashboard.git
    $ pip install -r requirements.txt
    $ vi app.py
    -> edit AUTH_TOKEN(change to your token)
    $ python app.py
    $ curl localhost:10080
    $ curl localhost:10080/clans/<clan_tag>
    -> clan_tag must do URL encoding

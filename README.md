Clash of Clan Dashboard
====

tl;dr
----
* Dashboard for Clash of Clan Official API
* Support multilingual(en/ja)
* use python(Flask, Babel)

usage
----

    $ git clone https://github.com/tsujimitsu/clash_of_clan_dashboard.git
    $ cd clash_of_clan_dashboard
    $ pip install -r requirements.txt
    $ export AUTH_TOKEN=<YOUR API TOKEN>
    -> You must get the API TOKEN from Clash of Clan developers page.
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


Clash of Clan Official API(2016-10-02)
====

endpoint
----
* https://api.clashofclans.com/v1/

/clans
----
* GET /clans
 * クラン一覧（膨大な数なので何らかのフィルタリングオプションを使って実行する）
 * 例えば、/clans?name=<clanName> など

* GET /clans/{clanTag}
 * クランタグで絞って検索（クラウンタグは%とか#で始める文字列）

* GET /clans/{clanTag}/members
 * クランタグで絞った状態でメンバー一覧取得

* GET /clans/{clanTag}/warlog
 * 戦績。プライベートにしているクラウンは見れない。


/locations
----
* GET /locations
 * 国名とコード一覧

* GET /locations/{locationId}
 * コードで絞って検索

* GET /locations/{locationId}/rankings/clans
 * 各国（地域）でのクランランキング取得（200位まで取れた）
 * 日本のIDは「32000122」

* GET /locations/{locationId}/rankings/players
 * 各国（地域）でのプレイヤーランキング（200位まで取れた）


/leagues
----
* GET /leagues
 * リーグ一覧の取得


example
----

    # APIの認証トークンはDeveloperサイト（※1）で発行します
    $ export AUTH_TOKEN=XXXXXXX
    
    # 検索（日本名はUTF-8でURLエンコードする必要があります）
    $ curl -sX GET --header 'Accept: application/json' --header "authorization: Bearer $AUTH_TOKEN" 'https://api.clashofclans.com/v1/clans?name=<clan name>' | python -mjson.tool
    
    $ curl -sX GET --header 'Accept: application/json' --header "authorization: Bearer $AUTH_TOKEN" 'https://api.clashofclans.com/v1/clans/<clan tag(#XXXXXX)>' | python -mjson.tool
    

reference
====
1. [Clash of Clans API](https://developer.clashofclans.com)

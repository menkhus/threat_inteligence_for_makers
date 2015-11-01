#!/usr/bin/env python
""" import_data is a loader for pulling data from feedslurp's files
    into the database.

    depends on:
        * feedslurp.py
        * feedslurp.db

    Author: Mark Menkhus, menkhus@icloud.com

"""

__author__ = 'Mark Menkhus, menkhus@icloud.com'
__version__ = '0.1'

import re
import sqlite3
import json


def get_rss_data_from_textfile(rss_text_data_file):
    jsondata = open(rss_text_data_file, 'r').readlines()
    return jsondata


def get_feed_list_from_textfile(site_list_file):
    feeds = open(site_list_file, 'r').readlines()
    return feeds


def setup_database(database):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    try:
        curs.execute('drop table rss_sites;')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    curs.execute("""create table rss_sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feed TEXT
                );""")
    try:
        curs.execute('drop table rss_data;')
        conn.commit()
    except sqlite3.OperationalError:
        pass
    curs.execute("""create table rss_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT
                );""")
    conn.commit()
    conn.close()
    return True


def write_site_list_to_db(database, site_list_file):
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    feeds = get_feed_list_from_textfile(site_list_file)
    for feed in feeds:
        if not re.search('^#', feed):
            feed = r'"' + feed + r'"'
            sql = "insert into rss_sites (feed) values (?)"
            curs.execute(sql, (feed,))
    conn.commit()
    conn.close()
    return True


def write_json_data_to_db(database, rss_text_data_file):
    jsondata = get_rss_data_from_textfile(rss_text_data_file)
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    for item in jsondata:
        item = item.strip('\n')
        item = json.dumps(item)
        # print item
        sql = "insert into rss_data (item) values (?)"
        curs.execute(sql, (item,))
    conn.commit()
    conn.close()


def main():
    """ setup database for first use, dump sites and
        json data into database
    """
    rss_text_data_file = 'feedslurp_rss_data.json'
    site_list_file = 'feedslurp_sitelist.txt'
    database = 'feedslurp.db'
    setup_database(database)
    write_site_list_to_db(database, site_list_file)
    write_json_data_to_db(database, rss_text_data_file)


if __name__ == "__main__":
    main()

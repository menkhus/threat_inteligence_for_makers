#!/usr/bin/env python
""" Feedslurp is a simple tool to pull in rss feed items from many rss feeds

    attempts to not store the same item if previously read
    creates a unique key for each item based on the title of the item

depends on:
    * feedparser library, install with "$ pip install feedparser"

    * feedslurp_sitelist.txt file, a list of rss feeds to read

output:
    feedslurp_rss_data.json: this is the database of feeds which feedslurp
    creates. The data is in JSON form, basically it's the JSON from feedparser,
    cleaned up a little for further use. The data is tagged with a signature,
    which is thought to be unique.

Author:
    Mark Menkhus, menkhus@icloud.com
    version = 0.1

License:
    createive commons, see license file in the project

"""
import re
import feedparser
import json
import time
import hashlib

site_list_file = 'feedslurp_sitelist.txt'
rss_data_file = 'feedslurp_rss_data.json'

__version__ = "0.1"
__author__ = "Mark Menkhus, menkhus@icloud.com"


def remove_non_ascii(text):
    """ exchange the non ascii charaters for
        spaces, one for every non ascii character
    """
    return re.sub(r'[^\x00-\x7F]', ' ', text)


def get_feed_list(site_list_file):
    feeds = open(site_list_file, 'r').readlines()
    feedlist = []
    for feed in feeds:
        if re.search(r'^#', feed):
            pass
        else:
            feedlist.append(feed.strip('\n'))
    return feedlist


def get_sig_list(rss_data_file):
    try:
        feed_items = open(rss_data_file, 'r').readlines()
    except IOError:
        msg = """Initializing, will try to create the database. and then
proceed with the first slurp.
        """
        print "IOError: problem opening %s. %s" % (rss_data_file, msg)
        feed_list_file = open(rss_data_file, 'a')
        feed_list_file.write('')
        feed_list_file.close()
        feed_items = []

    all_sigs = []
    for item in feed_items:
        item = json.loads(item)
        all_sigs.append(item['signature'])
    return all_sigs


def main():
    """ feedslurp.py
        depends on a list of rss feeds
        creates a file that will contain new news items appended
        each time feedslurp is run.
    """
    feedlist = get_feed_list(site_list_file)
    all_sigs = get_sig_list(rss_data_file)
    feed_items = open(rss_data_file, 'aw')
    for feed in feedlist:
        f = feedparser.parse(feed)
        for item in f.entries:
            # look to see if the freshly read item is already
            # in the database.
            # signature is a checksum of the title, check to
            # see if that title is already in the data base
            try:
                item['signature'] = hashlib.sha256(item['title']).hexdigest()
                if item['signature'] in all_sigs:
                    # we don't want to write a duplicately titled entry
                    break
            except KeyError:
                # if there is no title, then we just don't want this
                # rss item
                pass
            except UnicodeError:
                # sometimes there are nonascii characters in titles,
                # if there is something a little difficult, we change the
                # title, test for previous existance and store it if new.
                item['title'] = remove_non_ascii(item['title'])
                item['signature'] = hashlib.sha256(item['title']).hexdigest()
                if item['signature'] in all_sigs:
                    # we don't want to write a duplicate titled entry
                    break
            # feedparser yields time.struct_time dates back rather than date
            # strings so published_parsed and updated_parsed are not directly
            # serializable in the JSON data, so we turn it into a human
            # readable date
            try:
                if item['published_parsed']:
                    if isinstance(item['published_parsed'], time.struct_time):
                        item['published_parsed'] = \
                            time.strftime("%a, %d %b %Y %H:%M:%S",
                                          item['published_parsed'])
            except KeyError:
                pass
            try:
                if item['updated_parsed']:
                    if isinstance(item['updated_parsed'], time.struct_time):
                        item['updated_parsed'] = \
                            time.strftime("%a, %d %b %Y %H:%M:%S",
                                          item['updated_parsed'])
            except KeyError:
                pass
            try:
                # put the cleaned up feed item into the feed_items
                item = json.dumps(item)
                feed_items.write(item)
                feed_items.write('\n')
            except Exception as e:
                print "feedslurp.main: ** failed to store this entry: %s " % e,
                print "item: %s" % item
    feed_items.close()
    # end of main


if __name__ == "__main__":
    main()

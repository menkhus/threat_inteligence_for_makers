#!/usr/bin/env python
""" Feedslurp is a simple tool to pull in rss feed items from many rss feeds

    attempts to not store the same item if previously read
    creates a unique key for each item based on the title of the item

depends on:
    feedparser library, install with "$ pip install feedparser"
    list_of_sites_to_mine.txt file, a list of rss feeds to read
    rss_data.json file, a file to store all the previously read
    items, and to store all the new items we find

output:
    rss_data.json file - this is the database of feeds that feedslurp generates
    the data is in json form, basically it's the json from feedparser cleaned
     a little for further use, and tagged with a signature, whish is thought to
     be unique.

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

site_list_file = 'list_of_sites_to_mine.txt'
rss_data_file = 'rss_data.json'

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
        msg = """will try to create the database. and then
proceed with the first slurp.
        """
        print "IOError: problem opening %s, %s" % (rss_data_file, msg)
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
                # if there is not title, then we just don't want this
                # rss item
                pass
            except UnicodeError:
                # sometimes there are nonascii characters in titles,
                # if there is something a little difficult,we change then
                # title, test for existance and store it.

                item['title'] = remove_non_ascii(item['title'])
                item['signature'] = hashlib.sha256(item['title']).hexdigest()
                if item['signature'] in all_sigs:
                    # we don't want to write a duplicately titled entry
                    break
            # feedparser passes parsed dates back rather than strings
            # published_parsed and updated_parsed are not directly serializable
            # in the json data, so we turn it into a human readable date
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
                print "** failed to store this entry: %s " % e,
                print "item: %s" % item
    feed_items.close()
    # end of main


if __name__ == "__main__":
    main()

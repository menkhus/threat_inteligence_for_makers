#!/usr/bin/env python
""" test harness to test features

"""

import sys


def test_feedslurp(testdir='test/'):
    """ feedslurp test harness
    """
    import feedslurp
    site_list_file = testdir + 'feedslurp_sitelist.txt'
    rss_data_file_missing = testdir + 'feedslurp_rss_data.json.none'
    rss_data_file = testdir + 'feedslurp_rss_data.json'

    feedlist = feedslurp.get_feed_list(site_list_file)
    if feedlist:
        print "feedslurp: get_feed_list passed"
    else:
        print "feedslurp: get_feed_list failed"
        sys.exit(1)

    all_sigs = feedslurp.get_sig_list(rss_data_file_missing)
    if not all_sigs:
        print "feedslurp: all_sigs passed"
    else:
        print "feedslurp: all_sigs failed"
        sys.exit(1)

    all_sigs = feedslurp.get_sig_list(rss_data_file)
    if all_sigs:
        print "feedslurp: all_sigs passed"
    else:
        print "feedslurp: all_sigs failed"
        sys.exit(1)

    if feedslurp.get_rss_data(site_list_file, rss_data_file):
        print "feedslurp: get_rss_data passed"
    else:
        print "feedslurp: get_rss_data failed"
        sys.exit(1)
    return True


def test_import_data(testdir='test/'):
    """ import_data test harness
    """
    import import_data
    site_list_file = testdir + 'feedslurp_sitelist.txt'
    rss_text_data_file = testdir + 'feedslurp_rss_data.json'
    site_list_file = testdir + 'feedslurp_sitelist.txt'
    database = testdir + 'feedslurp.db'
    import_data.setup_database(database)
    import_data.write_site_list_to_db(database, site_list_file)
    import_data.write_json_data_to_db(database, rss_text_data_file)

    if import_data.setup_database(database):
        print "import_data: setup_database passed"
    else:
        print "import_data: setup_database failed"
        sys.exit(1)

    if import_data.write_site_list_to_db(database, site_list_file):
        print "import_data: write_site_list_to_db passed"
    else:
        print "fimport_data: write_site_list_to_db  failed"
        sys.exit(1)

    if import_data.write_json_data_to_db(database, rss_text_data_file):
        print "import_data: write_json_data_to_db passed"
    else:
        print "import_data: write_json_data_to_db: failed"
        sys.exit(1)
    return True


def main():
    test_feedslurp()
    test_import_data()


if __name__ == "__main__":
    main()

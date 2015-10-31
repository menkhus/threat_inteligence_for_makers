#### README for feedslurp.py

## About feedslurp:
  Feedslurp is a simple tool that reads a list of rss/atom etc sites and pulls the articles down into a file and stores them in json form.

  No analysis is done in feedslurp, rather feedslurp just creates a news database from the entries in your list_of_sites_to_mine.txt file.

  feedslurp depends on:
  * list_of_sites_to_mine.txt file (this file is provided in this project)
  * output file rss_data.json, which stores entries

  Outputs:
  feedslurp creates a signature from the title, that signature is used to make each item unique. Feedslurp won't repeat store an entry with the same title. The data is stored by default in rss_data.json

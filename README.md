# cps
Chess Puzzle Scraper

This project scrapes the chess puzzles from chesstempo.com in FEN format. 

## How to Install
This project relies on [Scrapy](http://scrapy.org), [Splash](https://github.com/scrapinghub/splash), and [Scrapy-splash](https://github.com/scrapinghub/scrapy-splash). To install the dependencies, install the python requirements specified by **requirements.txt**, and then follow the tutorials on Splash, Scrapy, and Scrapy-splash.

## How to Run

1. Make sure that scrapy is installed correctly, and `scrapy` in the command line gives you the help documentation.
2. Start splash with something like `docker run -p 8050:8050 scrapinghub/splash` (taken from scrapy-splash's documentation)
3. Check **settings.py** and make sure the configs are working.
4. Run `scrapy crawl chesstempo -o chesstempo-puzzles.json`

This should give you around 100 puzzles, each in FEN format, in a single file named **chesstempo-puzzles.json**.

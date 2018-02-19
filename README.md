# RoboDoc

This is the software for the
[RoboDoc project](https://tlocke.github.io/robodoc/). It's purpose is to crawl
UK government websites and make a list of documents that have proprietary file
formats.

Suggestions, contributions or bug reports are very welcome. Please open a new
issue on GitHub or send a pull request.


## Installing and running the RoboDoc software

* Make sure [Python 3](https://www.python.org/) is installed.
* Make sure
  [Scrapy is installed](https://doc.scrapy.org/en/latest/intro/install.html).
* Create a virtual environment: `virtualenv --python=python3 venv`
* Activate virtual environment: `source venv/bin/activate`
* Install via git: `pip install -e git+https://github.com/tlocke/robodoc.git`
* Run with: `./run.sh`

## Running Tests

* Install pytest: `pip install pytest`
* Run the tests: `pytest test_robodoc.py`

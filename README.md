# RoboDoc

Finding where proprietary file formats are used on UK government websites.

## Introduction

In 2014 the UK government [announced that open standards would be used for
sharing government documents](https://www.gov.uk/government/news/open-document-formats-selected-to-meet-user-needs).

In particular, PDF or HTML formats are to be used for viewing government
documents and the Open Document Format (ODF) is to be used for sharing or
collaborating on government documents.

The RoboDoc project aims to crawl the UK government websites and make a list
of documents that aren't published in an open format.


## Installing and running the RoboDoc software

* Make sure [Python 3](https://www.python.org/) is installed.
* Make sure
  [Scrapy is installed](https://doc.scrapy.org/en/latest/intro/install.html).
* Create a virtual environment: `virtualenv --python=python3 venv`
* Activate virtual environment: `source venv/bin/activate`
* Install via git: `pip install -e git+https://github.com/tlocke/robodoc.git`
* Run with: `./run.sh`

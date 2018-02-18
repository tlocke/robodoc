# RoboDoc

Finding where proprietary file formats are used on UK government websites.


## Introduction

In 2014 the UK government [announced that open standards would be used for
sharing government documents](https://www.gov.uk/government/news/open-document-formats-selected-to-meet-user-needs).

In particular, PDF or HTML formats are to be used for viewing government
documents and the Open Document Format (ODF) is to be used for sharing or
collaborating on government documents.

Unfortunately, not all files on UK government websites are published in an open
format yet, some are still published in a proprietary format. The RoboDoc
project aims to crawl the UK government websites and make a list of documents
that are still published in a proprietary format.


## List Of Proprietary Files

Here is the CSV of the first run of the RoboDoc crawler:

* [problems\_2018-02-19.csv](https://tlocke.github.io/robodoc/problems_2018-02-19.csv)

The run was performed on 10,000 pages of `http://www.gov.uk/`. It lists all
files on the site that end in either '.xls', '.xlsx', '.doc' or '.docx'. The
titles of the CSV are:

* `document_url`: The URL of the document in a proprietary format.
* `file_extension`
* `link_url`: The page that the link to the document is on.
* `crawl_timestamp`: The point in time when the document was found.


## Why Open Standards?

If a document is written in an open format, anyone can freely write editing
and viewing software for the format. This means that users aren't beholden to a
single vendor of software. In contrast, if a document is written in a
proprietary format, then the user can be locked-in to using software from a
single vendor.

For example, web pages are written in the open format HTML, which means there's
a good choice of web browser (eg. Microsoft Internet Explorer, Mozilla Firefox,
Apple Safari or Google Chrome).

A WikiBook on open standards has been written which includes a section on the
[benefits of open standards](https://en.wikibooks.org/wiki/FOSS_Open_Standards/Importance_and_Benefits_of_Open_Standards).


## Contributing

Suggestions, contributions or bug reports are very welcome. Please open a new
issue on GitHub.


## Installing and running the RoboDoc software

* Make sure [Python 3](https://www.python.org/) is installed.
* Make sure
  [Scrapy is installed](https://doc.scrapy.org/en/latest/intro/install.html).
* Create a virtual environment: `virtualenv --python=python3 venv`
* Activate virtual environment: `source venv/bin/activate`
* Install via git: `pip install -e git+https://github.com/tlocke/robodoc.git`
* Run with: `./run.sh`

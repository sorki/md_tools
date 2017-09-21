========
md_tools
========

Tools for https://otevrenamesta.cz/

------------
Requirements
------------

* python-slugify
* python-requests

------------
Installation
------------

Use the following commands::
    git clone https://github.com/sorki/md_tools/
    cd md_tools

Install dependencies with::
    pip install -r requirements.txt

-------------
Configuration
-------------

Create configuration file ``~/.md_tools`` with following contents::
    [ckan]
    url = https://ckan.example.org
    apikey = CHANGE_ME

-----
Tools
-----

* md_import - import data from CSV FILE

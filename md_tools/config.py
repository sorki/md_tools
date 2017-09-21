import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read(os.path.expanduser('~/.md_tools'))

ckan_url = config.get("ckan", "url")
ckan_apikey = config.get("ckan", "apikey")

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mendiafilescraper']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.2,<0.6.0',
 'peewee>=3.15.4,<4.0.0',
 'pymediainfo>=5.0.3,<5.1.0',
 'requests>=2.25.1,<2.26.0',
 'tmdbsimple>=2.7.0,<2.8.0',
 'websockets>=10.4,<11.0']

entry_points = \
{'console_scripts': ['mendia-scraper = mendiafilescraper:__main__.main']}

setup_kwargs = {
    'name': 'mendiafilescraper',
    'version': '3.1.1',
    'description': 'File scrapper for clients to sync with a mendia rust application running on a server.',
    'long_description': '# Mendia File Scraper\n\n## About\n\nThis is a client for [mendia](https://crates.io/crates/mendia).\nIt indexes local media (currently limited to movies), stores the findings in  a local database and publishes new additions to the server running mendia.\n\n## Installation:\n\n```console\nsudo apt update\nsudo apt install libmediainfo0v5\npip install mendiafilescraper\n```\n\n> Note: This package needs the mediainfo library.\n>\n> Ubuntu/Debian: \'libmediainfo0v5\'\n>\n> Arch: \'libmediainfo\'\n\n## Usage:\n\n```--setup```:\n> Asks for\n> - Username\n> - Password\n> - Media folders\n> - Server address (e.g `wss://hostname/ws/`, depending on the `mendia` server)\n>\n> and stores everything in a config file in the home directory\n>\n> `~/.mendiafilescraper/config.txt`\n\n```--scan```:\n> Searches all given media folders for new additions and adds them to the database.\n\n```--publish```:\n> Sends new additions to the configured `mendia` server. Use only with `--scan`\n\n## Example:\n### Settings\n\n```console\nmendia-scraper --setup\n```\n\n***Add media paths, specify the server address and put in your username and password.***\n\n> Note: Ask the admin of your target `mendia` server to create a username/password for you.\n\n### First scan\nThe initial scan populates the local database.\n`--publish` should not be used for the first scan, otherwise this might flood the server.\n\n```console\nmendia-scraper --scan\n```\n\n> Warning: ***Make sure that the initial scan worked before proceeding.***\n\n### Real scan\n\nAfter the first scan we can add `--publish`, from now on new movies will be sent to `mendia`.\n\n```console\nmendia-scraper --scan --publish\n```\n\n## Cronjob\n\nIt makes sense to add the scan command to your crontab for automatic scans.\n\n```console\ncrontab -e\n```\n\nFor a daily scan add\n\n```console\n@daily mendia-scraper --scan --publish\n```\n\n## Problems:\n\n### I have a new movie but mendia did not inform about it\n\nIt is possible to delete movies from the local database and to retry scanning the movie.\n\n> Note: It is easier to use a gui application with sqlite support, but on typical NAS systems there is no gui.\n\n```console\nsudo apt install sqlite3\ncd ~/.MendiaFileScraper\nsqlite3 database.db\n```\n\nLet\'s say we want to remove the movie "Captive State".\n\nIn the sqlite3 shell:\n```sql\nSELECT title, hash FROM movies WHERE instr(title, \'Captive\') > 0;\n```\nIf you do not see any result, play with the search parameters until you found it.\n\nLet\'s say our result is:\n```\nCaptive State|a67edf9ee879a7562c17092b97dfe672\n```\n\nThe second value is the hash value that was computed based on the movie file.\nTo delete the entry with the has "a67edf9ee879a7562c17092b97dfe672" we do:\n```sql\nDELETE FROM movies WHERE hash="a67edf9ee879a7562c17092b97dfe672";\n```\n\n`CTRL+D` to exit from the sqlite3 shell.\n\nVoila, the movie was removed and you can retry scanning with\n\n```console\nmendia-scraper --scan --publish\n```\n',
    'author': 'Lukas Riedersberger',
    'author_email': 'lukas.riedersberger@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/derfreak/MediaScrapper',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)

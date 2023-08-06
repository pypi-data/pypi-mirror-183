# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mendiafilescraper']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.2,<0.6.0',
 'pymediainfo>=5.0.3,<5.1.0',
 'requests>=2.25.1,<2.26.0',
 'tmdbsimple>=2.7.0,<2.8.0',
 'toml',
 'websockets>=10.4,<11.0']

entry_points = \
{'console_scripts': ['mendia-scraper = MendiaFileScraper:__main__.main']}

setup_kwargs = {
    'name': 'mendiafilescraper',
    'version': '2.0.1',
    'description': 'File scrapper for clients to sync with a mendia rust application running on a server.',
    'long_description': '# Willkommen beim Network File Scrapper !\n\n## Installation:\n\n```console\nsudo apt update\nsudo apt install git python3 python3-pip libmediainfo0v5\ngit clone https://gitlab.com/derfreak/MediaScrapper.git\ncd MediaScrapper\npython3 -m pip install -e .\n```\n\n## Verwendung:\n\n```--setup```:\n> Erstellt eine Konfigurationsdatei im Home-Verzeichnis des ausführenden Benutzers\n>\n> `~/.MendiaFileScraper/config.txt`\n>\n> Fragt nach\n> - Username\n> - Suchpfaden\n> - Serveradresse:Port\n> - Token\n> und trägt diese Daten in die Konfigurationsdatei ein\n\n```--scan```:\n> Durchsucht alle angegebenen Ordner nach neuen Dateien und schickt sie dem Server\n\n```--publish```:\n> mit `--scan` benutzen\n> Filme die mit dieser Option neu gefunden wurden werden anderen Usern bekannt gemacht\n\n\n## Benutzen:\n### Einstellungen\n\n```console\npython3 -m MendiaFileScraper --setup\n```\n\n***Fügt hier eure Pfade hinzu, setzt den Benutzernamen und stellt den Server und euer Zugangstoken ein.***\n\n***Ganz wichtig: Wenn euch etwas fehlt fragt den Entwickler/Betreiber des Servers***\n\n***Nur weitermachen wenn ALLES geht***\n\n### Erster Scan\nInitialer scan, populiert die Datenbank aber deaktiviert Telegram-Nachrichten.\n\n***Stellt sicher dass die Filme auch rausgeschickt werden sonst hagelt es hunderte Telegram-Nachrichten beim richtigen scan.***\n\n```console\npython3 -m MendiaFileScraper --scan\n```\n\n### Scan\n\nFügt danach die Option `--publish` hinzu damit neue Filme jedem bekannt gemacht werden.\n\n> **WARNUNG**: Der erste scan muss erfolgreich gewesen sein, ansonsten werden möglicherweise hunderte Filme an alle anderen User rausgeschicht\n\n```console\npython3 -m MendiaFileScraper --scan --publish\n```\n\n## Cronjob\n\nErstellt einen neuen crontab\n\n```console\ncrontab -e\n```\n\nHier diese Zeile einfügen\n\n```console\n@daily /usr/bin/python3 -m MendiaFileScraper --scan --publish\n```\n\n## Probleme:\n\n### Film hätte in Telegram sichtbar sein sollen\n\nUm einen Film zu löschen müsst ihr mit der sqlite3 shell die Datenbankdatei öffnen und dann über sql-Befehle den Film entfernen.\n\n```console\ncd ~/.MendiaFileScraper\nsudo apt install sqlite3\nsqlite3 database.db\n```\n\nSagen wir der Film den ihr löschen wollt heißt "Captive State".\n\nIn der sqlite3 shell:\n```sqlite-sql\nSELECT title, hash FROM movies WHERE instr(title, \'Captive\') > 0;\n```\nFalls ihr kein Ergebnis seht, passt den Suchstring "Captive" an.\nGroß und Kleinschreibung ist wichtig !\n\nBei mir kam folgendes Ergebnis:\n```sqlite-sql\nCaptive State|a67edf9ee879a7562c17092b97dfe672\n```\n\nAlso löscht ihr jetzt den Eintrag mit dem hash "a67edf9ee879a7562c17092b97dfe672"\n```sqlite-sql\nDELETE FROM movies WHERE hash="a67edf9ee879a7562c17092b97dfe672";\n```\n\n`STRG+D` um die sqlite3 shell zu beenden.\n',
    'author': 'Lukas Riedersberger',
    'author_email': 'lukas.riedersberger@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/derfreak/MediaScrapper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)

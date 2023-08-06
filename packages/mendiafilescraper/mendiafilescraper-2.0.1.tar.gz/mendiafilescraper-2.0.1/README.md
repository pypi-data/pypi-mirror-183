# Willkommen beim Network File Scrapper !

## Installation:

```console
sudo apt update
sudo apt install git python3 python3-pip libmediainfo0v5
git clone https://gitlab.com/derfreak/MediaScrapper.git
cd MediaScrapper
python3 -m pip install -e .
```

## Verwendung:

```--setup```:
> Erstellt eine Konfigurationsdatei im Home-Verzeichnis des ausführenden Benutzers
>
> `~/.MendiaFileScraper/config.txt`
>
> Fragt nach
> - Username
> - Suchpfaden
> - Serveradresse:Port
> - Token
> und trägt diese Daten in die Konfigurationsdatei ein

```--scan```:
> Durchsucht alle angegebenen Ordner nach neuen Dateien und schickt sie dem Server

```--publish```:
> mit `--scan` benutzen
> Filme die mit dieser Option neu gefunden wurden werden anderen Usern bekannt gemacht


## Benutzen:
### Einstellungen

```console
python3 -m MendiaFileScraper --setup
```

***Fügt hier eure Pfade hinzu, setzt den Benutzernamen und stellt den Server und euer Zugangstoken ein.***

***Ganz wichtig: Wenn euch etwas fehlt fragt den Entwickler/Betreiber des Servers***

***Nur weitermachen wenn ALLES geht***

### Erster Scan
Initialer scan, populiert die Datenbank aber deaktiviert Telegram-Nachrichten.

***Stellt sicher dass die Filme auch rausgeschickt werden sonst hagelt es hunderte Telegram-Nachrichten beim richtigen scan.***

```console
python3 -m MendiaFileScraper --scan
```

### Scan

Fügt danach die Option `--publish` hinzu damit neue Filme jedem bekannt gemacht werden.

> **WARNUNG**: Der erste scan muss erfolgreich gewesen sein, ansonsten werden möglicherweise hunderte Filme an alle anderen User rausgeschicht

```console
python3 -m MendiaFileScraper --scan --publish
```

## Cronjob

Erstellt einen neuen crontab

```console
crontab -e
```

Hier diese Zeile einfügen

```console
@daily /usr/bin/python3 -m MendiaFileScraper --scan --publish
```

## Probleme:

### Film hätte in Telegram sichtbar sein sollen

Um einen Film zu löschen müsst ihr mit der sqlite3 shell die Datenbankdatei öffnen und dann über sql-Befehle den Film entfernen.

```console
cd ~/.MendiaFileScraper
sudo apt install sqlite3
sqlite3 database.db
```

Sagen wir der Film den ihr löschen wollt heißt "Captive State".

In der sqlite3 shell:
```sqlite-sql
SELECT title, hash FROM movies WHERE instr(title, 'Captive') > 0;
```
Falls ihr kein Ergebnis seht, passt den Suchstring "Captive" an.
Groß und Kleinschreibung ist wichtig !

Bei mir kam folgendes Ergebnis:
```sqlite-sql
Captive State|a67edf9ee879a7562c17092b97dfe672
```

Also löscht ihr jetzt den Eintrag mit dem hash "a67edf9ee879a7562c17092b97dfe672"
```sqlite-sql
DELETE FROM movies WHERE hash="a67edf9ee879a7562c17092b97dfe672";
```

`STRG+D` um die sqlite3 shell zu beenden.

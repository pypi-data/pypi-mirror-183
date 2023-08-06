# xsget

Console tools to download online novel and convert to text file.

## Installation

Stable version From PyPI:

```console
python3 -m pip install xsget
playwright install
```

Latest development version from GitHub:

```console
python3 -m pip install -e git+https://github.com/kianmeng/xsget.git
playwright install
```

## xsget

```console
$ xsget -h
usage: xsget [-l CSS_PATH] [-p URL_PARAM] [-g [FILENAME] | -c [FILENAME]] [-r]
             [-t] [-b] [-bs SESSION] [-bd DELAY] [-d] [-h] [-v]
             URL

xsget is a console app that crawl and download online novel.

  website: https://github.com/kianmeng/xsget
  issues: https://github.com/kianmeng/xsget/issues

positional arguments:
  URL            set url of the index page to crawl

optional arguments:
  -l CSS_PATH    set css path of the link to a chapter (default: 'a')
  -p URL_PARAM   use url param key as filename (default: '')
  -g [FILENAME]  generate config file from options (default: 'xsget.toml')
  -c [FILENAME]  load config from file (default: 'xsget.toml')
  -r             refresh the index page
  -t             show extracted urls without crawling
  -b             crawl by actual browser (default: 'False')
  -bs SESSION    set the number of browser session (default: 10)
  -bd DELAY      set the second to wait for page to load in browser (default: 0)
  -d             show debugging log and stacktrace
  -h             show this help message and exit
  -v             show program's version number and exit

examples:
  xsget http://localhost
```

## xstxt

```console
$ xstxt -h
usage: xstxt [-pt CSS_PATH] [-pb CSS_PATH] [-rh REGEX REGEX] [-rt REGEX REGEX]
             [-bt TITLE] [-ba AUTHOR] [-ic INDENT_CHARS] [-i GLOB_PATTERN]
             [-e GLOB_PATTERN] [-l TOTAL_FILES] [-w WIDTH] [-o FILENAME]
             [-g [FILENAME] | -c [FILENAME]] [-d] [-h] [-v]

xstxt is a cli app that extract content from HTML to text file.

https://github.com/kianmeng/xsget

optional arguments:
  -pt CSS_PATH      set css path of chapter title (default: 'title')
  -pb CSS_PATH      set css path of chapter body (default: 'body')
  -rh REGEX REGEX   set regex to replace word or pharase in html file
  -rt REGEX REGEX   set regex to replace word or pharase in txt file
  -bt TITLE         set title of the novel (default: '不详')
  -ba AUTHOR        set author of the novel (default: '不详')
  -ic INDENT_CHARS  set indent characters for a paragraph (default: '\u3000\u3000')
  -i GLOB_PATTERN   set glob pattern of html files to process (default: '['./*.html']')
  -e GLOB_PATTERN   set glob pattern of html files to exclude (default: '[]')
  -l TOTAL_FILES    set number of html files to process (default: '3')
  -w WIDTH          set the line width for wrapping (default: 60), 0 to disable
  -o FILENAME       set output txt file name (default: 'book.txt')
  -g [FILENAME]     generate config file from options (default: 'xstxt.toml')
  -c [FILENAME]     load config from file (default: 'xstxt.toml')
  -d                show debugging log and stacktrace
  -h                show this help message and exit
  -v                show program's version number and exit

examples:
  xstxt -i *.html
```

## Copyright and License

Copyright (C) 2021,2022 Kian-Meng Ang

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>.

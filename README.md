# tgnewspaper

## Dependencies

### Debian GNU/Linux

```
# apt install git make python3 python3-pip texlive-full texlive-lang-cyrillic \
```

probably will also work with [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)

### Windows

lmao idk

## Usage

produces output to latex/news.pdf


```
$ git clone https://github.com/qq333teea/tgnewspaper
$ cd tgnewspaper
$ make
```

## Useful variables

`fetch.py`:

| variable   | value     | description                                     |
|------------|-----------|-------------------------------------------------|
| FETCHCOUNT | 140       | number of posts to request                      |
| POSTCOUNT  | 3         | number of posts from each channel in the output |
| PERIOD     | 7         | time period in days                             |
| channels   | [ tl;dr ] | list of channels (short name)                   |

## Make commands:
     clean  - ...
     deps   - install from requirements.txt
     fetch  - generate tex source
     latex  - compile tex source

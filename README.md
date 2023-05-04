# tgnewspaper

## Dependencies

### Debian GNU/Linux

    # apt install git make python3 python3-pip texlive-full texlive-lang-cyrillic

probably will also work with [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux)

### Windows

lmao idk

## Usage

produces output to latex/news.pdf

    $ git clone https://github.com/qq333teea/tgnewspaper
    $ cd tgnewspaper
    $ make

## Options

opts example:

    $ F=10 P=10 D=900 H=0 A=0 C="channel1 channel2" NAME=testname make

| variable | value     | description                                     |
|----------|-----------|-------------------------------------------------|
| F        | 300       | number of posts to request                      |
| P        | 3         | number of posts from each channel in the output |
| D        | 7         | time period in days                             |
| C        | [ tl;dr ] | list of channels (short name)                   |
| H        | 1         | bool include neural horoscope (1 or 0)          |
| A        | 1         | bool sign posts (1 or 0)                        |
| VOL      |           | paper volume                                    |
| ISSUE    |           | paper issue                                     |
| NAME     |           | paper name                                      |
| SLOGAN   |           | paper slogan                                    |
| PRICE    |           | paper price                                     |

## Make commands:
     clean  - ...
     deps   - install from requirements.txt
     fetch  - generate tex source
     latex  - compile tex source

.PHONY: all clean deps fetch latex

all: clean deps fetch latex

clean:
	rm -f latex/*.aux latex/*.log latex/fig/*

deps:
	pip3 install -r requirements.txt

fetch:
	python3 fetch.py

latex:
	sh -c 'cd latex; xelatex news.tex'

all: clean deps fetch

clean:
	rm -rf news latex/*.aux latex/*.log

deps:
	pip3 install -r requirements.txt

fetch:
	python3 fetch.py

latex:
	cd latex
	pdflatex news.tex

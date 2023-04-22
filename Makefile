all: deps run

run:
	python3 fetch.py

deps:
	pip3 install -r requirements.txt

latex:
	cd latex
	pdflatex news.tex

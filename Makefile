all: clean deps run

run:
	python3 fetch.py

deps:
	pip3 install -r requirements.txt

clean:
	rm -r news

latex:
	cd latex
	pdflatex news.tex

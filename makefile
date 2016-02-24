all: main.py draw.py display.py
	python main.py

cool: cool.py
	python cool.py

clean:
	rm *.pyc

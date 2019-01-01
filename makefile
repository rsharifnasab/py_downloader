
reset:
	@python3 py_dl.py
	@python3 py_dl.py

run: 
	@python3 py_dl.py

install:
	sudo apt-get install python3
	sudo apt-get install wget
	sudo apt-get install python3-bs4

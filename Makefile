init:
	pip install -r requirements.txt

test:
	nosetests tests

clean:
	rm tests/sheets/*.xlsx

go into the NEXTRApol_example directory
	cd path_to/NEXTRApol_example

create virtual environment within NEXTRApol_example
	python3 -m venv venv_nextrapol
	source venv_nextrapol/bin/activate

update pip
	pip install --upgrade pip

install the required python packages
	pip install -r requirements.txt

install the nextrapol package. It is located in the directory named NEXTRApol
	pip install -e ../NEXTRApol     ## if necessary change path to the nextrapol package top level directory (above src)

finalise the installation by issuing the shell command 
	intialize

You can now use nextra in your python scipts as 
	import nextrapol as nx




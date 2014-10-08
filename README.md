cow-as-as-service
=================

Cowsay as a web service

An example webservice for webservice command-line tool, writen in python using flask.

See http://github.com/fiedzia/webservices


Set up:

		virtualenv -p python3 venv
    . ./venv/bin/activate
    pip install -r requirements.txt
    python caas.py


Standalon usage:

		Set it up, then go to http://localhost:5000/cowsay/?t=hello

Usage via ws:

		Get ws command from http://github.com/fiedzia/webservices
    then run:

		./ws example/cowsay -t hello

		and enjoy cow speaking to you.

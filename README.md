# Challenge48h

Documentation for develop blockchain application with Python 

## Instructions to run

Clone the project,

```sh
$ git clone https://github.com/valentingbt/challenge48h.git
```

Install the dependencies,

```sh
$ cd challenge48h
$ pip install -r requirements.txt
```

Start a blockchain node server,

```sh
$ export FLASK_APP=node_server.py
$ flask run --port 8000
```

One instance of our blockchain node is now up and running at port 8000.


Run the application on a different terminal session,

```sh
$ python run_app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).

If you would to try multiple sessions nodes, use the next command.

```sh
# already running
$ flask run --port 8000 &
# spinning up new nodes
$ flask run --port 8001 &
$ flask run --port 8002 &
```


## Xmeme

 A web application for memer's

## setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/TheShubham-K/Xmeme.git
$ cd crio_xmeme
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```


Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

make a .env file in the crio_xmeme project directory `(not in the root directory)` and save your ``SECRET_KEY`` in it in the following way :
```sh 
SECRET_KEY=your_secret_key
```



Once `pip` has finished downloading the dependencies and finished setting .env file :
make sure that you have docker installed in your local machine and it's running. 

```sh
(env)$ cd crio_xmeme
(env)$ make compose-start
```

if some error occurs then first try running these following command :
```sh
(env)$ make build
(env)$ make build-prod
(env)$ make compose-start
```

To stop the docker server :
```sh
(env)$ make compose-stop
```

These are the list of API routes to navigate through.

```sh
http://localhost:8000/memes/  # Memes Stream List
http://localhost:8000/memes/<id>/ # to a particular meme with id (place the id of the meme in place of <id> in integer number format)
http://localhost:8000/memes-form/ # to add a new meme in the memes list
http://localhost:8000/memes-update/3/ # to update a meme.
```


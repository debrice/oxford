# Oxford dictionary API

A basic REST API returning the definition of a word as a JSON response.


In order to resolve the anagram, the table receives an index on the
anagram column. Anagram will be stored with their letters sorted.
for example, "wolf", "flow" and "fowl" will all receives the anagram "flow".
This allows an instant matching instead of using costly permutations O(n!). see the [DictionaryEntry init](https://github.com/debrice/oxford/blob/master/oxford/models.py#L11) and [dictionary get_anagrams](https://github.com/debrice/oxford/blob/master/oxford/dictionary.py#L22) for more details.


I've decided to use SQL-Alchemy as it offesr more options on the storage
medium (postgres, mysql, sqlite). Relational databases are a better
storage strategy for the current use (word lookup) than Elastic
Search (expensive "index all" behavior).


## Example

```
$ curl http://127.0.0.1:5000/?word=flow  | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   634  100   634    0     0   225k      0 --:--:-- --:--:-- --:--:--  309k
{
  "definition": " —v. 1 glide along ... river (ebb and flow). [old english]",
  "word": "flow",
  "anagrams": [
    "fowl",
    "wolf"
  ]
}
```

## Install

The application is meant to be run in a virtual environment

First create your virtual environment

```sh
virtualenv venv
```

Then activate it

```sh
. venv/bin/activate
```

And install the requirements

```sh
pip install -r requirements.txt
```


## Usage

First, load some data in the app using the CLI. The assets folder contains the
database of words. To load it in the database, use the CLI

```sh
python manage.py load --source assets/Oxford\ English\ Dictionary.txt
```

then launch the app

```sh
python manage.py run

```

by default it should start on port 5000. You may change the port using
the -p parameter

```sh
python manage.py run -p 9001
```

## CLI

This app comes with a basic Command Line Interface (CLI)

```sh
$ python manage.py
Usage: manage.py [OPTIONS] COMMAND [ARGS]...

  The Oxford dictionary Restful API.

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  load   Load the DB with the source file
  run    Runs a development server.
  shell  Runs a shell in the app context.
```

## Testing

Use nose for testing, the root folder of the app, type:

```sh
nosetests
```

to display the code coverage use nose-cov

```sh
nosetests --with-cov --cov-report term-missing --cov oxford
```

which should give you the code coverage of the project

```
...........
---------- coverage: platform linux2, python 2.7.12-final-0 ----------
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
oxford/__init__.py                    13      0   100%
oxford/config.py                       4      0   100%
oxford/dictionary.py                  22      0   100%
oxford/endpoints.py                   12      0   100%
oxford/models.py                       9      0   100%
oxford/test.py                        18      0   100%
oxford/test_config.py                  2      0   100%
oxford/tests/dictionary_tests.py      21      0   100%
oxford/tests/endpoints_tests.py       34      0   100%
oxford/tests/models_tests.py          10      0   100%
----------------------------------------------------------------
TOTAL                                145      0   100%
----------------------------------------------------------------------
Ran 11 tests in 0.235s

OK
```


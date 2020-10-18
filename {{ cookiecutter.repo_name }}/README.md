{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Directory structure for machine learning projects.

### Requirements to use the cookiecutter template:
-----------
 - Python 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip package manager:

``` bash
$ pip install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/{username}/{catalyst}


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure

Project Organization
------------

```
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── Makefile
    ├── README.md
    ├── TODO
    ├── credentials --  passwds and api keys
    │   ├── aws
    │   ├── email
    │   └── gcloud
    ├── data    --  all kinds of data
    │   ├── cache   --  intermediate data like pkl version of processed dataset
    │   ├── parameters  --  preprocessed data in form suitable for feeding into the models
    │   └── raw --  raw datasets not overwritten by any code
    ├── docs    --  documentation for end user
    ├── images
    │   ├── figures --  generated analysis as HTML, PDF, LaTeX, etc.
    │   └── plots   --  generated graphics and figures to be used in reporting
    ├── libs    --  external modules and packages/requirements/docker file
    ├── notebooks   --  exploratory notebooks
    ├── notes   --  technical notes and ideas mostly internal stuff
    │   ├── references  --  notes pertaining to dataset schema
    │   └── snippets
    ├── reports
    │   ├── diagnostics --  data diagnostics like missing values, model diagnostics
    │   ├── logs
    │   │   ├── datafeed    --  logs produced by dataloaders and feeders
    │   │   └── model   --  logs produced by model objects
    │   └── profiling   --  code coverage and profiling
    ├── requirements.txt    --  cookiecutter requirements file
    ├── setup.py    --  cookiecutter setup file
    ├── src
    │   ├── models  --  model file, trainer, test and logger files
    │   └── scripts --  scripts mostly bash, sometime python too
    ├── test_environment.py --  cookiecutter test env
    ├── tex --  in case this work is for publication
    └── tox.ini --  tox file with settings for running tox; see tox.testrun.org
```

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

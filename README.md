# Automated browser testing for DBCA

## Install

* Create a virtualenv for this project
* Clone this repo
* Pip install dependencies

```
mkproject turtle-testing
git clone GITHUBREPO .
pip install -r requirements.txt
```

## Setup

Rename a copy of `.env.template` to `.env` and enter 
your DBCA course URL, enrolment key, username and password.
```
COURSE="https://learning-uat.dpaw.wa.gov.au/course/view.php?id=123"
UN="myDBCAusername"
PW="myDBCApassword"
```

## Run

Including activating and deactivating the virtualenv, run:
```
workon turtle-testing
python test.py
deactivate
```


http://www.seleniumhq.org/docs/03_webdriver.jsp
# Requirements
- mongoDB installed and running

# Installation
```bash
# clone repo
git clone https://github.com/karate/peregrin.git peregrin
cd peregrin

# create virtualenv
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate

# install requirements
pip install requirements.txt
```

# Testing
## Run server
```bash
gunicorn app:api
```

## Test with curl
```bash
curl -X GET localhost:8000/pages
curl -X POST -d '{"title":"Test page","url":"/test-page"}' localhost:8000/pages
curl -X GET localhost:8000/pages
```

# Serverless Framework Solution with Python and Flask

## Requirements

- It's required to have already installed and configured `AWS CLI` and `Serverless Framework`.
- For the deployment process it's required to have installed and running `Docker`.

## Running the application locally

```sh
npm install                                             # Install the serverless dependencies
pip install virtualenv                                  # Installing virtualenv python library
virtualenv venv --python=python3                        # Setting up the virtual env
pip install -r requirements.txt --no-index --find-links # Install python libraries locally

python app.py                                           # Run the REST API with Python

export FLASK_APP=app.py # Setting up the entry point of the flask application, required to run the API with Flask command
export FLASK_DEBUG=1    # For development purpose. It allows to edit the files and the dev server is reloaded when it happens
flask run               # Run the REST API with Flask
```

## Deploy the REST API to AWS with Serverless Framework

```sh
sls deploy
```

## Resources

- [How to handle the errors in Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

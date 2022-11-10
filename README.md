# fastapi-amazon-example

## About

This is a simple example of how to use [FastAPI](https://fastapi.tiangolo.com/)
to create a CRUD API that can be deployed
to [AWS Lambda](https://aws.amazon.com/lambda/)
using [Mangum](https://mangum.io/)
and [DynamoDB](https://aws.amazon.com/dynamodb/).

## Running locally

### Install dependencies

```bash
poetry install
```

create aws config file path `~/.aws/config`

```bash
[default]
region = your-region
aws_access_key_id=your-access-key
aws_secret_access_key=your-secret-key
```

### Run the API

```bash
poetry run uvicorn app.main:app --reload
```

### Run pylint

```bash
poetry run pylint app tests
```

### Run the tests

```bash
poetry run pytest
```

## Deploying to AWS Lambda

check the .github/workflows/main.yml

## Features

1. [ ] Write tests for the routes
2. [ ] Write tests for the services
3. [ ] Write tests for the repositories
4. [ ] [dependency injection](https://python-dependency-injector.ets-labs.org/)
5. [ ] [mypy](http://mypy-lang.org/)
6. [ ] [sphinx](https://www.sphinx-doc.org/en/master/)

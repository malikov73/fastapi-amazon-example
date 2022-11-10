# fastapi-amazon-example

This is an example of how to use [FastAPI](https://fastapi.tiangolo.com/),
to create a simple CRUD API that can be deployed to [AWS Lambda](https://aws.amazon.com/lambda/)
[Mangum](https://mangum.io/) and [DynamoDB](https://aws.amazon.com/dynamodb/).



## Running locally

### Install dependencies

```bash
poetry install
```

set environment variables

```bash
export AWS_ACCESS_KEY_ID=your_aws_access_key_id
export AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
export AWS_DEFAULT_REGION=your_aws_default_region
```

### Run the API

```bash
poetry run uvicorn app.main:app --reload
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
4. [ ] add [dependency injection](https://python-dependency-injector.ets-labs.org/)

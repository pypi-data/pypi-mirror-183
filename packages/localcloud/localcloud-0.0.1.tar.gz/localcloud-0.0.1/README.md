`localcloud` - CLI tool allowing to imitate cloud components locally for testing their integration.

## Usage
Clone code repositories into working directory and run `localcloud`, which will read 
Terraform configuration from all of the repositories and will locally create their
imitations (using docker containers and mocks). Now you should have all of the resources
working locally and you should be able to run integration tests on them, e.g. `make run_integration_tests`.

## Roadmap
- [ ] Add Lmabda support
- [ ] Add SQS support
- [ ] Add EventBridge support
- [ ] Add generic resource mock, which allows to define interface wrappings.

## Development
`make venv` - will create virtual env with dev dependencies.
`make check` - will run Flake8, MyPy and PyTest checks.

## Related projects
This tool was inspired by:
- https://localstack.io

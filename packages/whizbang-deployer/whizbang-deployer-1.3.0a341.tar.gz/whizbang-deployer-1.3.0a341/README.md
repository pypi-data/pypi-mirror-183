## Whizbang

The Whizbang deployer is a tool designed to simplify deployments of Azure solutions.  The solutions contains utilities and functions that implmenting projects use to deploy specific azure solutions for customers.

[![Whizbang Deployer CI Run](https://github.com/hitachisolutionsamerica/whizbang-deployer/actions/workflows/python-app.yaml/badge.svg)](https://github.com/hitachisolutionsamerica/whizbang-deployer/actions/workflows/python-app.yaml)

## NOTICE - Main Branch Change
The `development` branch has been renamed to `main`.  Follow the steps below to adjust your local environment.
```
git branch -m development main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a
```

### Installation

It it important to note that this package is installed and distributed in two different modes:
- **Local Binary Installation** -> This requires the needed packages to be install globally.  This is how development with dependent projects (i.e. empower) is typically done.
- **Containerized** -> The containerized method includes binary dependencies which are used for CI/CD and is how the artifact is actually deployed and used in production.

#### Mac Prequisites
- `brew install docker docker-compose`

#### Windows Prequisites
_TODO_

#### Local Binary Build
`poetry install`
`poetry build`
`pip3 uninstall whizbang-deployer -y`
`pip3 install ./dist/whizbang*.whl`
_Then run any solution file directly: `python solution.py`_

**To run tests:**
`python3 -m pytest`

#### Containerized Build
_These may no longer work._

**To run pytests:**
- `docker-compose -f docker_builds/docker-compose.yml up --build pyenv`

**To run pytests with watch:**
- `docker-compose -f docker_builds/docker-compose.yml up --build pyenv-watch`

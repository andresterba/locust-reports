# locust-reports

This repo contains some usefull scripts to generate graphs of the generated csv of the load testing tool [Locust](https://locust.io/).

## Getting started

This project uses [Poetry](https://python-poetry.org/) to somehow handle Python dependencies.
So you need `Poetry` installed on your machine (that can be a bit of a hassle...).

```sh
# Poetry on Ubuntu 20.04 / Debian 10
apt install -y python3-pip python3-venv
apt install -y build-essential libssl-dev libffi-dev python3-dev
pip3 install poetry

# Init project
poetry install --no-dev
poetry shell
```

## Generate CSV

To save the collected data into csv use the web-ui or the following cli flag.

```sh
locust -f src/locustfile.py --csv-full-history --csv=name-of-test
```

## Kubernetes
As I have used this scripts to visualize load against an application within Kubernetes there
is also a script to save the current number of pods and nodes in your cluster.

```sh
./log-nodes-and-pods.sh test-1 my-deployment
```
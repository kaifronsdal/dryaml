# dryaml

[![CI](https://github.com/Quantco/dryaml/actions/workflows/ci.yml/badge.svg)](https://github.com/Quantco/dryaml/actions/workflows/ci.yml)
[![Documentation](https://img.shields.io/badge/docs-latest-success?style=plastic)](https://docs.dev.quantco.cloud/qc-github-artifacts/Quantco/dryaml/latest/index.html)

Don't Repeat Yourself YAML is an extension to YAML that includes references within and across configuration files to reduce boilerplate, string interpolation, and more.

## Installation

You can install the package in development mode using:

```bash
git clone git@github.com:kaifronsdal/dryaml.git
cd dryaml

# create and activate a fresh environment named dryaml
# see environment.yml for details
mamba env create
conda activate dryaml

pre-commit install
pip install --no-build-isolation -e .
```

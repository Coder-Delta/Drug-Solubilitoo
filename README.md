# Drug-Solubilitoo

A small Python project for downloading, inspecting, and preparing the ESOL (Delaney) drug solubility dataset for later analysis and visualization.

## Overview

This repository currently focuses on:

- downloading the ESOL dataset from the official DeepChem GitHub source
- saving a local copy as `esol.csv`
- inspecting the dataset structure with `pandas`
- checking column names, data types, and missing values

The main data processing logic lives in [`datacleaner.py`](/home/zedx/Codes/PythonForML/projects/Drug-Solubilitoo/datacleaner.py).

## Dataset

The script uses the Delaney processed dataset from DeepChem:

`https://raw.githubusercontent.com/deepchem/deepchem/master/datasets/delaney-processed.csv`

This dataset contains molecular descriptors and solubility values such as:

- compound ID
- molecular weight
- number of rings
- number of rotatable bonds
- polar surface area
- predicted ESOL solubility
- measured solubility
- SMILES representation

## Project Structure

```text
Drug-Solubilitoo/
├── datacleaner.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Requirements

- Python `3.13`
- `pandas`

The project is configured in [`pyproject.toml`](/home/zedx/Codes/PythonForML/projects/Drug-Solubilitoo/pyproject.toml).

## Setup

If you are using `uv`:

```bash
uv sync
```

If you prefer `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas
```

## How To Run

Run the data cleaning script from the repository root:

```bash
python datacleaner.py
```

Or with `uv`:

```bash
uv run python datacleaner.py
```

## What The Script Does

When you run `datacleaner.py`, it:

1. downloads the ESOL dataset
2. saves it locally as `esol.csv`
3. prints the dataset shape
4. prints the column names
5. prints the data types
6. checks for missing values
7. prints the percentage of missing values per column

## Current Status

This project is an early-stage data preparation script. A few things are still incomplete:

- `matplotlib` is imported but not yet used for visualization
- `df.head()` is called but not printed, so the first five rows are not shown in terminal output
- `main.py` appears to be a separate experiment and is not part of the ESOL workflow
- there are no tests yet

## Next Improvements

Good next steps for this project would be:

- add actual data cleaning or imputation logic
- create visualizations with `matplotlib`
- save cleaned outputs to a dedicated `data/` folder
- add notebooks or scripts for exploratory data analysis
- include tests for the data loading pipeline

## License

No license file is currently included in this repository.

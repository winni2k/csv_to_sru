# CSV to SRU Converter for Skatteverket form K4

This Python-based tool converts CSV files into the SRU format specifically tailored for uploading transactions to Skatteverket for the form K4. The K4 form is used in Sweden for reporting sales of securities and other financial instruments. This converter facilitates the process by transforming the required transaction data from a CSV format into the SRU file format accepted by Skatteverket.

## Features

- Converts CSV files with transaction data into the SRU format for Skatteverket's K4 form.
- Offers a Command Line Interface (CLI) for straightforward conversion.
- Allows for customization of the identity number and name for the generated SRU file. For individual users, the identity number is typically the Swedish social security number.

## Requirements

- Python 3.6 or higher
- `click` library

## Installation

First, clone this repository or download the source code. Make sure you have poetry installed (https://python-poetry.org/docs/#installation). Then, install the necessary Python dependencies by running:

```bash
poetry install
```

## Usage

To convert a CSV file into an SRU file suitable for K4 form submissions, use the following CLI command:

```bash
poetry run python csv_to_sru_converter.py INPUT_FILE_PATH OUTPUT_FILE_PATH --identity "IDENTITY_NUMBER" --name "NAME"
```

In this command, replace INPUT_FILE_PATH and OUTPUT_FILE_PATH with the paths to your input and output files, respectively. Also, replace IDENTITY_NUMBER with your Swedish social security number, and NAME with your name as it should appear in the generated SRU file.

## Testing

Tests are implemented using pytest. To run them, simply execute:

```bash
poetry run pytest
```

## Author

Warren Winfried Kretzschmar

## Acknowledgments

This code was developed with the assistance of ChatGPT-4, an advanced language model by OpenAI.
I used the online SRU file generator https://srumaker.se/ to figure out what the SRU format should look like.


# Issue CWE Extractor

This Python script extracts issue IDs and CWE IDs from a JSON file based on the source file name provided.

## Prerequisites

- Python 3.x

## Installation

No installation is required.

## Usage

Run the script with the following command:

```
python extract.py <json_file> <source_file>
```

- `<json_file>`: Path to the JSON file containing the data.
- `<source_file>`: Name of the source file to search for within the JSON data.

For example:

```
python extract.py data.json "ToolsController.java"
```

## Output

The script will output pairs of (issue_id, cwe_id) if findings are available for the specified source file. If no findings are available, it will display "No findings for the specified source_file."

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `"data.json"` with the path to your JSON file, and `"ToolsController.java"` with the desired filename with its extension.


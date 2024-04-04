import json
import sys
import os

def extract_issue_cwe(json_file, source_file):
    json_file = os.path.abspath(json_file)  # Validate and sanitize the json_file path
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extracting issue_id and cwe_id based on source_file
    pairs = []
    for finding in data["findings"]:
        if os.path.basename(finding["files"]["source_file"]["file"]) == source_file:
            issue_id = finding["issue_id"]
            cwe_id = finding["cwe_id"]
            pairs.append((issue_id, cwe_id))

    return pairs

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <json_file> <source_file>")
        sys.exit(1)

    json_file = sys.argv[1]
    source_file = sys.argv[2]

    pairs = extract_issue_cwe(json_file, source_file)
    if not pairs:
        print("No findings for the specified source_file.")
    else:
        print("Findings for source File: " + source_file)
        print("==================================")
        print ("Issue ID, CWE ID")
        for pair in pairs:
            print(pair)

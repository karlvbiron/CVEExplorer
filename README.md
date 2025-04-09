# CVEExplorer

![cveexplorer_personified](assets/cveexplorer_personified.png)

A lightweight RESTful Flask API for retrieving and exploring CVE (Common Vulnerabilities and Exposures) data from the National Vulnerability Database (NVD).

## Overview

CVEExplorer provides a simple, RESTful API that allows security researchers, developers, and cybersecurity professionals to query specific CVE information. It uses the NVDLIB library to fetch vulnerability data directly from the National Vulnerability Database and presents it in a clean JSON format.

## Features

- RESTful architecture for resource-based CVE information retrieval
- Retrieve comprehensive CVE information by ID
- Access specific fields or attributes of a CVE
- JSON-formatted responses for easy integration
- Custom JSON serialization for handling complex objects and dates

## Installation

### Prerequisites

- Python 3.6+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/karlvbiron/CVEExplorer.git
cd CVEExplorer
```

2. Create a virtual environment (recommended):
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the API Server

Run the application:
```bash
python app.py
```

The server will start on `http://127.0.0.1:5000` by default in debug mode.

### API Endpoints

The API follows RESTful principles, organizing endpoints around resources (CVEs and their attributes):

#### Get Full CVE Information

```
GET /cve/<cve_id>
```

Returns all available information about the specified CVE.

Example:
```bash
curl http://localhost:5000/cve/CVE-2021-27928
```

#### Get Specific CVE Field

```
GET /cve/<cve_id>/<field_name>
```

Returns a specific field from the CVE data.

Examples:
```bash
# Get just the CVE ID
curl http://localhost:5000/cve/CVE-2021-27928/id

# Get the metrics information
curl http://localhost:5000/cve/CVE-2021-27928/metrics

# Get the score information
curl http://localhost:5000/cve/CVE-2021-27928/score

# Get the CVSSv2 score
curl http://localhost:5000/cve/CVE-2021-27928/v2score
```

### Response Format

All responses are returned in JSON format, following RESTful conventions. If the requested CVE or field doesn't exist, a 404 error is returned with an appropriate error message.

## Response Examples

### Full CVE Information

```json
{
  "id": "CVE-2021-27928",
  "descriptions": [...],
  "metrics": {...},
  "references": [...],
  ...
}
```

### Specific Field (ID)

```json
{
  "id": "CVE-2021-27928"
}
```

### Specific Field (Score)

```json
{
  "score": [
    "V31",
    7.2,
    "HIGH"
  ]
}
```

## Implementation Details

- Uses Flask for the RESTful web framework
- NVDLIB for interfacing with the National Vulnerability Database
- Custom JSON encoder to handle complex objects like datetime and sets
- RESTful design principles for resource-oriented architecture

## Limitations

- Only supports direct CVE ID queries
- Does not support searching by keywords, vendors, or other criteria
- Nested fields (beyond top-level attributes) are not directly accessible
- Limited to READ operations (GET requests only)

## Development

This project is in development mode. For production deployment, consider:

- Using a production WSGI server (like Gunicorn or uWSGI)
- Disabling debug mode
- Implementing proper error handling and logging
- Adding authentication for API access
- Expanding the RESTful capabilities with additional endpoints

## License

[MIT License](LICENSE)
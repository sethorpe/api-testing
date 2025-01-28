# Python API Testing Framework

This folder contains the **Python implementation** of the API testing framework

## Features
- **Framework**: Built with `pytest` for streamlined test execution.
- **Reporting**: Integrated with Allure for detailed, interactive HTML reports.
- **Logging**: Logs API requests and responses for easier debugging and test traceability

## Prerequisites
- Python 3.8 or higher
- Allure CLI installed globally:
    ```bash
    allure --version
    ```

## Setup
1. Navigate to the `python_api` directory:
    ```bash
    cd python_api
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests
### Using VS Code Test Runner
1. Open the project in VS Code.
2. Navugate to the Testing tab.
3. Run the desired test cases.

### **Using the Command Line**
Run the test suite with:
```bash
pytest tests --alluredir=../allure-results
```

## Logging Feature
The framework logs all API requests and responses, making debugging easier and providing traceability for tests. Logs are available in two locations:

1. **File-Based Logging**:
    - Logs are stored in `api_test_logs.log` in the project root
    - Each log entry includes:
        - Request: Method, URL, Headers, Payload.
        - Response: Status Code, Headers, Body.
2. **Allure Report**:
    - Logs are attached to the relevant test case in the Allure report.
    - Each request and response is displayed in human-readable format.

### Example Logs
File Output(`api_test_logs.log`):
```plaintext
Request:
Method: GET
URL: https://jsonplaceholder.typicode.com/posts
Headers: {'Accept': 'application/json'}
Payload: None

Response:
Status Code: 200
Headers: {'Content-Type': 'application/json; charset=utf-8'}
Body: [
    {
        "id": 1,
        "title": "Sample Post"
    }
]
```
### Allure Report:
- Attachments for each API call are available under test steps as "Request Details" and "Response Details."

## Generating Reports
Use the standalone script to generate and serve the report:
```bash
python ../generate_and_serve_allure_report.py
```
## Future Enhancements
- Expand the test suite to cover more APIs.
- Add advanced testing techniques, such as data-driven testing and mocking.
- Enhance logging with masking sensitive data (e.g., paswords, tokens).
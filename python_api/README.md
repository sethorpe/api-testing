# Python API Testing Framework

This folder contains the **Python implementation** of the API testing framework

## Features
- **Framework**: Built with `pytest` for streamlined test execution.
- **Reporting**: Integrated with Allure for detailed, interactive HTML reports.

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

### Using the Command Line
Run the test suite with:
```bash
pytest tests --alluredir=../allure-results
```
## Generating Reports
Use the standalone script to generate and serve the report:
```bash
python ../generate_and_serve_allure_report.py
```
## Future Enhancements
- Expand the test suite to cover more APIs.
- Add advanced testing techniques, such as data-driven testing and mocking.
# HDFC Credit Card Statement Parser

This project provides a Python script to parse HDFC credit card statements from a PDF file and convert the data into a CSV format.

## Features
- Extracts both domestic and international transactions from HDFC credit card statements.
- Outputs the parsed data into a CSV file.

## Requirements
To run this project, ensure you have Python 3 installed on your system.

### Required Libraries
- `pdfplumber`: For extracting text and tables from PDF files.
- `argparse`: For handling command-line arguments (if using in future modifications).

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your_username/hdfc-credit-card-statement-parser.git
   cd hdfc-credit-card-statement-parser
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your **input.pdf** file (HDFC credit card statement) in the same folder as the script.
2. Run the script:
   ```bash
   python parser.py
   ```

3. The output will be generated as **output.csv** in the same folder.

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

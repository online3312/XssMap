Overview

This script is designed to detect Cross-Site Scripting (XSS) vulnerabilities on a given website. It uses a list of predefined payloads to test for XSS vulnerabilities in HTML forms found on the target site. The script is written in Python and utilizes the requests and BeautifulSoup libraries to perform its tasks.
Features

    Load XSS payloads from a text file.
    Identify and test forms on a specified webpage.
    Check if any of the payloads are reflected back in the page response, indicating a potential XSS vulnerability.

Installation

To use this script, you need Python installed on your machine along with the required libraries. You can install the required libraries using pip.

    Clone the repository or download the script.

    Install required libraries:

    pip install requests beautifulsoup4

    Prepare your payload file:

    Create a text file named xss-payload-list.txt inside the Payload directory. This file should contain one XSS payload per line.

Usage

    Save the script to a file, e.g., main.py.

    Ensure you have a payload file at Payload/xss-payload-list.txt.

    Run the script from the command line, providing the target URL as an argument:

    bash

    python main.py <website-url>

    Replace <website-url> with the URL of the website you want to test.

Example

python main.py http://example.com

Script Details
Functions

    load_payloads(file_path): Loads XSS payloads from a specified file. It attempts to read the file with different encodings (utf-8, latin-1, cp1252) and returns a list of payloads.

    test_xss(url, payloads): Tests the specified URL for XSS vulnerabilities using the provided payloads. It finds all forms on the page and submits each payload to check if it is reflected back in the response.

Error Handling

    The script handles various errors, including file reading errors and request failures, and prints relevant error messages to the console.

License

This script is provided under the MIT License. Use it at your own risk and ensure you have permission to test the target website.
Disclaimer

This script is intended for educational purposes and responsible security testing only. Do not use it to test websites without permission, as unauthorized testing may be illegal.
Contact

For any issues or suggestions, please open an issue in the repository or contact the script author.

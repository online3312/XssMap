import requests
from bs4 import BeautifulSoup
import sys

asciicode = '''
 \o       o/     o__ __o        o__ __o      o          o           o           o__ __o   
  v\     /v     /v     v\      /v     v\    <|\        /|>         <|>         <|     v\  
   <\   />     />       <\    />       <\   / \\o    o// \         / \         / \     <\ 
     \o/      _\o____        _\o____        \o/ v\  /v \o/       o/   \o       \o/     o/ 
      |            \_\__o__       \_\__o__   |   <\/>   |       <|__ __|>       |__  _<|/ 
     / \                 \              \   / \        / \      /       \       |         
   o/   \o     \         /    \         /   \o/        \o/    o/         \o            
  /v     v\     o       o      o       o     |          |    /v           v\    |         
 />       <\    <\__ __/>      <\__ __/>    / \        / \  />             <\  / \        
'''

print(asciicode)

def load_payloads(file_path):
    """ Load XSS payloads from a file """
    encodings = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return [line.strip() for line in file if line.strip()]
        except UnicodeDecodeError:
            continue
    raise Exception(f"Unable to read the file with known encodings.")

def test_xss(url, payloads):
    """ Test for XSS vulnerabilities using the provided payloads """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        forms = soup.find_all('form')

        if not forms:
            print("No forms found on the page.")
            return

        print(f"Found {len(forms)} form(s) on the page. Testing for XSS...")
        for form in forms:
            action = form.get('action', '')
            method = form.get('method', 'get').lower()
            form_url = url if not action else requests.compat.urljoin(url, action)
            
            inputs = form.find_all('input')
            form_data = {}
            for input_tag in inputs:
                name = input_tag.get('name')
                if name:
                    form_data[name] = ''

            for payload in payloads:
                for key in form_data:
                    form_data[key] = payload

                    try:
                        if method == 'post':
                            response = requests.post(form_url, data=form_data)
                        else:
                            response = requests.get(form_url, params=form_data)

                        if payload in response.text:
                            print(f"Potential XSS vulnerability detected with payload: {payload}")
                    except Exception as e:
                        print(f"An error occurred: {e}")

    except Exception as e:
        print(f"An error occurred while fetching the page: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <website-url>")
        sys.exit(1)

    website_url = sys.argv[1]
    payload_file_path = 'Payload/xss-payload-list.txt'

    payloads = load_payloads(payload_file_path)
    if not payloads:
        print(f"No payloads found in {payload_file_path}")
        sys.exit(1)

    test_xss(website_url, payloads)

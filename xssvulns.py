import requests
import re  # Add this line to import the 're' module

def main():
    # Get the target URL
    target_url = input("Enter the target URL: ")

    # Make a GET request to the target URL
    response = requests.get(target_url)

    # Check the response body for XSS vulnerabilities
    for match in re.findall(r"<script>(.*?)</script>", response.content.decode('utf-8')):  # Add decode('utf-8') here
        print("Potential XSS vulnerability found:", match)

if __name__ == "__main__":
    main()


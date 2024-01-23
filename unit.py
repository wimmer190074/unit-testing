import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract information based on HTML tags and attributes
        # For example, let's extract all the links on the page
        links = soup.find_all('a')

        # Print the extracted links
        for link in links:
            print(link.get('href'))
    else:
        print(f"Error: Unable to fetch the web page. Status code: {response.status_code}")

# Example usage:
url_to_scrape = 'https://example.com'
simple_web_scraper(url_to_scrape)

import requests
from bs4 import BeautifulSoup
import random

def fetch_quotes():
    # Send a GET request to Goodreads quotes page
    response = requests.get('https://www.goodreads.com/quotes')

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all quote elements on the page
    quote_elements = soup.find_all(class_='quoteText')

    # Extract the text of each quote and clean it up
    quotes = []
    for quote_element in quote_elements:
        quote = quote_element.get_text(strip=True)
        # Remove unwanted characters
        quote = quote.replace("“", "").replace("”", "")
        quotes.append(quote)

    return quotes

def generate_quote(quotes):
    random_quote = random.choice(quotes)
    print(random_quote)

# Fetch quotes from Goodreads
quotes = fetch_quotes()

# Generate a random quote
generate_quote(quotes)

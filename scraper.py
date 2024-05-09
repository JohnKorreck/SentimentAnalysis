from bs4 import BeautifulSoup
import requests

# Proper User-Agent header key
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

def headliners(ticker):
    # Use f-string for dynamic URL based on ticker
    response = requests.get(f'https://finance.yahoo.com/quote/{ticker}/news', headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(response.status_code)
        exit(1)
    print('Request successful')

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all <a> tags with the specified class
    headline_links = soup.find_all('a', {'class': 'subtle-link fin-size-small titles noUnderline svelte-wdkn18'})

    # Check if any headlines were found and print them
    num = 1
    if headline_links:
        for headline in headline_links:
            print(f"{num}. {headline.text}")
            num += 1
    else:
        print("No headlines found")

# Example call to the function with the 'KO' ticker symbol
headliners('KO')
# Dependencies
import requests
from bs4 import BeautifulSoup as bs
import smtplib
import ssl
from email.message import EmailMessage
import time

'''
    TO-DO: Notify Through Email
'''

# Input Handling
url = input('Enter url: ')
header = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254'}
thresholdPrice = int(input("Enter a threshold price: "))

# Price Extractor
def extractPrice():
    for attempt in range(6):  # Try up to 3 times
        page = requests.get(url, headers=header)
        soup = bs(page.content, 'html.parser')
        price_element = soup.find('span', class_='a-price-whole')
        
        if price_element:  # Check if the price element was found
            price = float(price_element.text.split()[0].replace(',', ""))
            return price
        else:
            print("Price element not found, retrying...")
            time.sleep(7)  # Wait before retrying
    return None  # Return None if price can't be fetched after retries


def main():

    currentPrice = extractPrice()

    if currentPrice != None and currentPrice <= thresholdPrice:
        print(currentPrice)
        print("Price Has Dropped")

    elif currentPrice == None:
        print("Please Try Again!")
    else:
        print(currentPrice)
        print("Price is still above threshold!")

main()
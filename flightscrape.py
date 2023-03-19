import requests
from bs4 import BeautifulSoup

# Set the URL of the flight search page
url = "https://www.cheapflights.ca/flights-to-India/Vancouver/"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

#flight_container = soup.find('div', {'id': 'flightsearch-Main'})
# Find all the flight postings
flight_posts = soup.find_all('div', {'class': "kml-layout edges-m mobile-edges c31EJ"})
#print(flight_posts)
with open('flight_posts.txt', 'w') as f:
    # Iterate over the flight postings and print the flight title and company name
    for flight in flight_posts:
        if(flight.find('span', {'class': "d-le-airport-code"}) != None):
            title = flight.find('h2', {'class': 'fU96-title'}).text.split()
            detail = soup.find('div',{'class':"d-le d-le-pres-default"})
            #dept = detail.find('span', {'class': "d-le-airport-code"})

            deparr = detail.find_all('span', {'class': "d-le-airport-code"})
            times = flight.find('div', {'class': "d-le-times-container"}).text.split()

            if len(times) == 2:
                stops = times[0][:7]
                hour = times[0][8:]
                mint = times[1]
            else:
                stops = times[0]
                hour = times[1][5:]
                mint = times[2]

            date = flight.find('span',{'class':"c1TfF-trip-date"}).text.split()
            depart = deparr[0].text.split()
            arrival = deparr[1].text.split()
            price = flight.find('span',{'class':"c1TfF-price c1TfF-pres-default"}).text.split()
            f.write("\n")
            for i in title:
                f.write(i + ' ')

            f.write("\n")
            d =''
            for y in date:
                d = d + y + ' '
            f.write("Date: "+ d)
            f.write(f"Departure: {depart}  Arrival: {arrival}\nNo. of stops: {stops}\nTime: {hour}{mint}\nPrice: CA${price[1]}\n")
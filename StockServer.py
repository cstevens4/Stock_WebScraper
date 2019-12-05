# Import socket module
from socket import *
# Import requests to get HTML
import requests
# Regex to extract information
import re
# Store the data to json
import json
# In order to terminate the program
import sys
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Set up server
HOST = ''
PORT = 1234
ADDR = (HOST, PORT)

# Create a TCP server socket
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def get_status(stock_name):
    stock_link = 'https://markets.businessinsider.com/stocks/' + stock_name + '-stock'
    r = requests.get(stock_link)
    return r.status_code


def extract(stock_name):
    # Get HTML text from website
    stock_link = 'https://markets.businessinsider.com/stocks/' + stock_name + '-stock'
    r = requests.get(stock_link)

    if (r.status_code == 404):
        return '404'
    else:

        stock_html = r.text
        # Extract information from  HTML text
        # Low in day, high in day, low-high in 52 week
        start = stock_html.find('<div class="col-xs-12 col-md-3 mobile-no-padding no-padding-right">')
        end = stock_html.find('<div class="spacer-10 visible-xs visible-sm">', start)
        price_html = stock_html[start:end]
        cleaned = re.sub("<.*?>", "", price_html)  # remove <>
        data = re.split("\s+", cleaned)
        low_day = data[5]  # low price has position at 5 in data
        high_day = data[6]  # low price has position at 6 in data

        # Some stocks don't have low day price and high day price,
        # Therefore, check length of data[] before get information
        if (len(data) == 17):
            low_week = data[13]
            high_week = data[14]
        else:
            low_week = data[14]
            high_week = data[15]

        # Stock price
        start = stock_html.find('<div class="col-md-3 col-xs-6 text-right bold black">')
        end = stock_html.find('<div class="col-md-3 col-xs-6 black">', start)
        price_html = stock_html[start:end]
        cleaned = re.sub("<.*?>", "", price_html)  # remove <>
        data = re.split("\s+", cleaned)
        stock_price = data[1] + ' ' + data[2]  # Stock price has position at 1 and 2 in data
        # print(stock_price)

        # Array contains html part needed
        data_html = []
        for i in range(0, 8):
            start = stock_html.find('<div class="col-md-3 col-xs-6 text-right bold black">', start + 110)
            end = stock_html.find('<div class="col-md-3 col-xs-6 black">', start)
            needed_info = stock_html[start:end]
            data_html.append(needed_info)

        # Trade Time in data_html[1]
        cleaned = re.sub("<.*?>", "", data_html[1])  # remove <>
        data = re.split("\s+", cleaned)
        trade_time = data[1]  # Needed data has position at 1 in data

        # Trade Date in data_html[3]
        # print(data_html[3])
        cleaned = re.sub("<.*?>", "", data_html[3])  # remove <>
        data = re.split("\s+", cleaned)
        trade_date = data[1]  # Needed data has position at 1 in data

        # Open price in data_html[5]
        # print(data_html[5])
        cleaned = re.sub("<.*?>", "", data_html[5])  # remove <>
        data = re.split("\s+", cleaned)
        # print(data)
        open_price = data[1]  # Needed data has position at 1 in data
        # print(open_price)

        # Volume in data_html[6]
        # print(data_html[6])
        cleaned = re.sub("<.*?>", "", data_html[6])  # remove <>
        data = re.split("\s+", cleaned)
        # print(data)
        volume = data[1]  # Needed data has position at 1 in data
        # print(volume)

        # Previous close price in data_html[7]
        # print(data_html[7])
        cleaned = re.sub("<.*?>", "", data_html[7])  # remove <>
        data = re.split("\s+", cleaned)
        # print(data)
        close_price = data[1]  # Needed data has position at 1 in data
        # print(close_price)

        # Market Cap
        start = stock_html.find('<table class="table table-small no-margin-bottom">')
        end = stock_html.find('</table>', start)
        mrkcap_html = stock_html[start:end]
        # print(mrkcap_html)
        cleaned = re.sub("<.*?>", "", mrkcap_html)  # remove <>
        data = re.split("\s+", cleaned)
        # print(data)
        market_cap = data[4] + ' ' + data[5]  # Market Cap has position at 4 and 5 in data
        # print(market_cap)

        # Company Information
        # Full name, Country, ISIN, Symbol
        start = stock_html.find('<table class="table table-small no-margin-bottom">', start + 1)  # next table
        end = stock_html.find('</table>', start)
        info_html = stock_html[start:end]
        # print(info_html)
        cleaned = re.sub("<.*?>", "", info_html)  # remove <>
        data = re.split("\s+", cleaned)
        full_name = data[3] + ' ' + data[4]  # Full Name has position at 3 and 5 in data
        country = data[6]
        isin = data[8]
        symbol = data[10]


        # Stock Info dict
        stock_info = {"full_name": full_name, "country": country, "symbol": symbol, "ISIN": isin,
                      "price": stock_price, "trade_time": trade_time, "trade_date": trade_date,
                      "open": open_price, "close": close_price, "volume": volume, "market_cap": market_cap,
                      "low_day": low_day, "high_day": high_day, "low_week": low_week, "high_week": high_week}
        # Convert into JSON
        jstock = json.dumps(stock_info)
        # Return json file
        return jstock


# Handles incoming connections
def accept_incoming_connections():
    while True:
        # Set up a new connection from the client
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        # Send greeting message
        client.send("Welcome to Stock Server!".encode("utf8"))
        # Start client thread to handle the new connection
        Thread(target=handle_request, args=(client,)).start()


# Handles a single request connection
def handle_request(connectionSocket):
    while True:
        try:
            # Receives the stock name from the client
            stock_name = connectionSocket.recv(1024).decode()
            print(stock_name + ' received')
            # Send status code to check stock name available
            status = str(get_status(stock_name))
            connectionSocket.send(status.encode("utf8"))
            # If status code is 200, send data
            if (get_status(stock_name) == 200):
                # Json
                # Extract information from HTML text
                stock_file = extract(stock_name)
                # Send JSON to client
                connectionSocket.sendall(stock_file.encode("utf8"))
                print(stock_file)
        except IOError:
            print('error')
    connectionSocket.close()


def main():
    # Listen to request connections
    SERVER.listen(5)

    # Start the accepting connections thread
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    # Wait for the accepting connections thread to stop
    ACCEPT_THREAD.join()

    # Close the server socket
    SERVER.close()


if __name__ == "__main__":
    main()
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import _show
import tkinter as tk
import socket
import json
import sys
# Create TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_server(server, port, message_lbl):
    try:
        if (check_empty(server) == TRUE):
            HOST = server.get()
            if (check_empty(port) == TRUE):
                PORT=int(port.get())
                # Set up client connection
                ADDR = (HOST, PORT)
                # Connect to the server
                # Check if not connected to server
                if message_lbl.cget("text") == "":
                    client_socket.connect(ADDR)
                    text = receive_message()
                    message_lbl.configure(text="Connected to Server!")
    except socket.gaierror as msg:
        _show('Message','Cannot connect to server. Try again!')
    except ValueError:
        _show('Message','Port has to be digits!')

# Handles receiving of Json file
def receive_file():
    try:
        stock_file = client_socket.recv(1024).decode("utf8")
        print("Receive from server: " + stock_file)
        data = json.loads(stock_file)
        return data
    except OSError:
        print('error:receive file')


def receive_message():
    try:
        msg = client_socket.recv(1024).decode("utf8")
        print(msg)
        return msg
    except OSError:
        print('error:receive msg')


def send(stock_entry, info_fram, message_lbl):
    try:
        # If entry is not empty, send stock name to server
        if (check_empty(stock_entry) == TRUE):
            stock_name = stock_entry.get()
            # Send Stock name to server
            client_socket.send(stock_name.encode("utf8"))

            print(stock_name + ' sent')
            # Get status code from server
            status_code = receive_message()
            print(status_code)
            if (status_code == '200'):
                message_lbl.configure(text='SERVER: ' + stock_name + ' found!')
                print(stock_name + ' found')
                show_data(info_fram, receive_file())
            else:
                message_lbl.configure(text='SERVER: ' + stock_name + ' not found!')
    except OSError:
        print('error')


def check_empty(entry):
    if not entry.get():
        flag = FALSE  # entry is empty
        _show('Message', ' Cannot be empty!')
    else:
        flag = TRUE  # entry is not empty
    return flag
def all_children (root):
    widget_list=root.winfo_children()
    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())
    return widget_list

def show_data(root, data):
    # Static Properties
    widget_list=all_children(root)
    for item in widget_list:
        item.destroy()
    # Company Info
    lbl_header1 = Label(root, text="Company Information", font=('calibri', 15, 'bold'))
    lb1 = Label(root, text="Full Name: ", font=('calibri', 12, 'bold'))
    lb2 = Label(root, text="Country: ", font=('calibri', 12, 'bold'))
    lb3 = Label(root, text="Symbol: ", font=('calibri', 12, 'bold'))
    lb4 = Label(root, text="ISIN: ", font=('calibri', 12, 'bold'))
    lb5 = Label(root, text="Market Cap: ", font=('calibri', 12, 'bold'))
    lb6 = Label(root, text="Volume (Qty): ", font=('calibri', 12, 'bold'))
    # Stock Info
    lbl_header2 = Label(root, text="Stock Information", font=('calibri', 15, 'bold'))
    lb8 = Label(root, text="Price: ", font=('calibri', 12, 'bold'))
    lb9 = Label(root, text="Open: ", font=('calibri', 12, 'bold'))
    lb10 = Label(root, text="Prev. Close: ", font=('calibri', 12, 'bold'))
    lb11 = Label(root, text="Trade Time: ", font=('calibri', 12, 'bold'))
    lb12 = Label(root, text="Trade Date: ", font=('calibri', 12, 'bold'))
    lb13 = Label(root, text="Day's Range: ", font=('calibri', 12, 'bold'))
    lb14 = Label(root, text="52-week Range: ", font=('calibri', 12, 'bold'))

    lbl_name = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_symbol = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_country = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_isin = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_price = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_open = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_close = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_volume = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_mrkcap = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_dayRange = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lb1_52Range = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_trade_time = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')
    lbl_trade_date = Label(root, font=('Courier New', 12, 'bold'), foreground='royal blue')

    # Geometry
    lbl_header1.grid(row=1, column=0, columnspan=4, pady=10)
    lb1.grid(row=2, column=0, sticky=W, pady=10)
    lb2.grid(row=2, column=2, sticky=W, pady=10, padx=10)
    lb3.grid(row=3, column=0, sticky=W, pady=10)
    lb4.grid(row=3, column=2, sticky=W, pady=10, padx=10)
    lb5.grid(row=10, column=0, sticky=W, pady=10)
    lb6.grid(row=10, column=2, sticky=W, pady=10, padx=10)
    lbl_header2.grid(row=5, column=0, columnspan=4, pady=10)
    lb8.grid(row=6, column=0, sticky=W, pady=10)
    lb9.grid(row=8, column=0, sticky=W, pady=10)
    lb10.grid(row=8, column=2, sticky=W, pady=10, padx=10)
    lb11.grid(row=9, column=0, sticky=W, pady=10)
    lb12.grid(row=9, column=2, sticky=W, pady=10, padx=10)
    lb13.grid(row=7, column=0, sticky=W, pady=10)
    lb14.grid(row=7, column=2, sticky=W, pady=10, padx=10)

    lbl_name.grid(row=2, column=1, sticky=E, pady=10)
    lbl_symbol.grid(row=3, column=1, sticky=E, pady=10)
    lbl_country.grid(row=2, column=3, sticky=E, pady=10)
    lbl_isin.grid(row=3, column=3, sticky=E, pady=10)

    lbl_price.grid(row=6, column=1, sticky=E, pady=10)
    lbl_open.grid(row=8, column=1, sticky=E, pady=10)
    lbl_close.grid(row=8, column=3, sticky=E, pady=10)
    lbl_volume.grid(row=10, column=3, sticky=E, pady=10)
    lbl_mrkcap.grid(row=10, column=1, sticky=E, pady=10)
    lbl_dayRange.grid(row=7, column=1, sticky=E, pady=10)
    lb1_52Range.grid(row=7, column=3, sticky=E, pady=10)
    lbl_trade_time.grid(row=9, column=1, sticky=E, pady=10)
    lbl_trade_date.grid(row=9, column=3, sticky=E, pady=10)

    # print(data)
    # Initial Properties
    # Company Info
    lbl_name.configure(text=data["full_name"])
    lbl_symbol.configure(text=data["symbol"])
    lbl_country.configure(text=data["country"])
    lbl_isin.configure(text=data["ISIN"])

    # Stock Info
    lbl_price.configure(text=data["price"])
    lbl_open.configure(text=data["open"])
    lbl_close.configure(text=data["close"])
    lbl_volume.configure(text=data["volume"])
    lbl_mrkcap.configure(text=data["market_cap"])
    lbl_dayRange.configure(text=data["low_day"] + ' - ' + data["high_day"])
    lb1_52Range.configure(text=data["low_week"] + ' - ' + data["high_week"])
    lbl_trade_time.configure(text=data["trade_time"])
    lbl_trade_date.configure(text=data["trade_date"])


'''def search_stock(stock_name):
    # Create a TCP server socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Connect to the server
    clientSocket.connect((server, serverPort))
    clientSocket.send(stock_name)'''


def check_default(server_text, port_text):
    server_text.set('localhost')
    port_text.set('1234')


def main():
    # Create root window
    root = Tk()
    root.title("Stock Scraper")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    # root.geometry('700x700')
    # Create style object
    button_style = Style()
    button_style.configure('TButton', font=('calibri', 12, 'bold'), foreground='royal blue')
    entry_style = Style()
    entry_style.configure('TEntry', foreground='royal blue')
    header_style = Style()
    header_style.configure('TLabel', foreground='RoyalBlue4')

    # Create Frame:
    connect_frame = Frame(root, width=500, height=100)
    connect_frame.pack(pady=10, padx=20)
    search_frame = Frame(root, width=500, height=80)
    search_frame.pack(pady=10)
    info_frame = Frame(root, width=700, height=350, pad=10)
    info_frame.pack()

    # Create widgets in connect frame
    header1 = Label(connect_frame, text="Connect to Server:", font=('calibri', 15, 'bold'))
    header1.grid(column=0, row=0, columnspan=2, pady=5)
    l1 = Label(connect_frame, text="Server:", font=('calibri', 12, 'bold'))
    l2 = Label(connect_frame, text="Port:", font=('calibri', 12, 'bold'))
    l1.grid(column=0, row=1, pady=5, sticky=W)
    l2.grid(column=0, row=2, pady=5, sticky=W)

    # entry widgets
    server_text = StringVar()
    port_text = StringVar()
    server_entry = Entry(connect_frame, textvariable=server_text, justify=CENTER, font=('calibri', 12, 'bold'))
    server_entry.grid(column=1, row=1, pady=5)
    port_entry = Entry(connect_frame, textvariable=port_text, justify=CENTER, font=('calibri', 12, 'bold'))
    port_entry.grid(column=1, row=2, pady=5)

    chk_default = Checkbutton(connect_frame, text="Default", command=lambda: check_default(server_text, port_text))
    chk_default.grid(column=0, row=3, columnspan=2, sticky=W)
    lbl_sever = Label(connect_frame, text="", font=('Courier New', 10, 'bold'), foreground='red3')
    lbl_sever.grid(row=4, column=0, columnspan=2)
    connect_button = Button(connect_frame, text="Connect",
                            command=lambda: connect_server(server_text, port_text, lbl_sever))
    connect_button.grid(column=1, row=3, sticky=E, pady=10)

    # Create widgets in search frame
    header2 = Label(search_frame, text="Search Stock Information:", font=('calibri', 15, 'bold'))
    header2.grid(column=0, row=0, columnspan=3, pady=5, padx=5)
    Label(search_frame, text='Stock Name:', font=('calibri', 12, 'bold')).grid(column=0, row=1, padx=10, pady=5,
                                                                               sticky=W)
    stock_entry = Entry(search_frame, width=30, justify=CENTER, font=('calibri', 12, 'bold'))
    stock_entry.grid(column=1, row=1, pady=5)
    lbl_search = Label(search_frame, text="", font=('Courier New', 10), foreground='red3')
    lbl_search.grid(row=2, column=0, columnspan=3)
    search_button = Button(search_frame, text="Search")
    search_button.grid(row=1, column=2, pady=10, padx=10)
    search_button.configure(command=lambda: send(stock_entry, info_frame, lbl_search))

    # Create widgets in Info frame
    root.mainloop()


if __name__ == "__main__":
    main()
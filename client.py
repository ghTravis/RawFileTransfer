#!/usr/bin/env python

from __future__ import print_function
import sys
import socket


class Client(object):
    """
    Client Class

    Establish connection with server and download a file
    """

    def __init__(self, host, port):
        """
        Init

        Client object initialization
        :param host:
        :param port:
        :return:
        """
        self.socket = socket.socket()
        self.host = host
        self.port = int(port)
        self.command = None
        self.filename = None

        # Connect to a remote host by opening a socket for communication
        self.socket.connect((self.host, self.port))

    def main(self, command, filename):
        """
        main

        Send a command to a server for file transfer actions
        :param command:
        :param filename:
        :return:
        """
        self.filename = filename
        if command.upper() == "GET":
            self.socket.send(command.upper() + "|")
            self._get()
        elif command.upper() == "SEND":
            self.socket.send(command.upper() + "|")
            self._send()
        else:
            print("Command was not either GET or SEND")
            self.socket.close()
            exit()

    def _get(self):
        """
        get

        Get data from a server
        :return:
        """

        # Send the name of the file we want to get
        self.socket.send(self.filename)

        # Open a file handler to a new file and write received data to it
        with open("received_" + self.filename, "wb") as f:
            print("Receiving file: "+ self.filename)
            print("Transferring...", end="")

            # Maintain connection with server until all data is received
            while True:
                data = self.socket.recv(1024)
                sys.stdout.write(".")
                sys.stdout.flush()

                if not data:
                    break

                f.write(data)

            # Close the file handler
            f.close()

        # Close the socket connection to the server
        print("\nTransfer complete.")
        self.socket.close()

    def _send(self):
        """
        send

        Send data to a server
        :return:
        """

        # Send the name of the file we want to send
        self.socket.send(self.filename)

        # Send the requested file based on the first bits of data received
        # open file handler
        print("Sending file: " + self.filename)

        f = open(self.filename, "rb")
        line = f.read(1024)

        # Send the file, print dots based on 1024 bit chunks
        # close the file handler
        print("Transferring...", end="")
        while line:
            self.socket.send(line)
            sys.stdout.write(".")
            sys.stdout.flush()
            line = f.read(1024)
        f.close()

        # Close the socket connection to the server
        print("\nTransfer complete.")
        self.socket.close()


if __name__ == "__main__":

    # Check for proper number of args provided with the command
    if sys.argv[3] not in ("SEND", "send", "GET", "get"):
        print("You must specify either GET or SEND ( client.py HOST PORT (GET|SEND) FILENAME )")
    if len(sys.argv) >= 4:
        hostname, port_num, command, filename = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    else:
        print("You must specify a host, port and a filename to download ( client.py HOST PORT (GET|SEND) FILENAME )")
        exit()

    # Initialize the Client object
    run = Client(host=hostname, port=port_num)

    # Call get(), handle errors and close the socket if exception
    try:
        run.main(command, filename)
    except KeyboardInterrupt as e:
        run.socket.close()
        exit()
    except Exception as e:
        run.socket.close()
        raise Exception(e)

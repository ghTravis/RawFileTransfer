#!/usr/bin/env python

from __future__ import print_function
import socket
import sys


class Server(object):
    """
    Server Class

    Serve client requests for files
    """

    def __init__(self, port):
        """
        Init

        Server object initialization
        :param port:
        :return:
        """
        self.port = port
        self.socket = socket.socket()
        self.hostname = "0.0.0.0"

    def main(self):
        """
        main

        Send or receive data to/from the client

        Server accepts a GET or a SEND command from a client for file transfers
        :return:
        """

        # Bind to socket
        self.socket.bind((self.hostname, self.port))

        # Start listener
        self.socket.listen(5)
        print("Server listening...")

        # Maintain infinite loop to accept connections
        while True:

            # Wait to accept connections with blocking call
            conn, address = self.socket.accept()
            print("Client {} connected.".format(address))

            # Receive data from client
            result = conn.recv(1024)
            print("Server received data: ", repr(result))
            command, filename = result.split("|")

            # Send a file if the command is GET
            if command == "GET":
                # Send the requested file to client
                # open file handler
                print("Sending file: " + filename)

                try:
                    f = open(filename, "rb")
                except IOError as e:
                    print("ERROR: No file found named "+filename)
                    conn.close()
                    continue

                # Send the file, print dots based on 1024 bit chunks
                print("Transferring...", end="")
                line = f.read(1024)

                while line:
                    conn.send(line)
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    line = f.read(1024)

                # Close the file handler
                f.close()

            # Receive a file if the command is SEND
            elif command == "SEND":
                # Receive the file name from client
                # open file handler
                print("Receiving file: " + filename)

                # Receive the file and write to the file handler, print dots based on 1024 bit chunks
                print("Transferring...", end="")
                with open("sent_" + filename, "wb") as f:
                    while True:
                        file_data = conn.recv(1024)
                        sys.stdout.write(".")
                        sys.stdout.flush()

                        # Stop receiving data if the client has stopped sending
                        if not file_data:
                            break

                        f.write(file_data)

                    # Close the file handler
                    f.close()

            # Close the connection with the client
            print("\nDone.")
            conn.close()


if __name__ == "__main__":

    # Initialize the Server Object
    run = Server(port=7005)

    # Call send(), handle errors and close socket if exception
    try:
        run.main()
    except KeyboardInterrupt as e:
        run.socket.close()
        exit()

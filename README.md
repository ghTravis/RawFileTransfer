# Raw File Transfer

A proof of concept for delivering a file between two machines, one acting as a server machine and the other a client machine.

### Features

The FileTransfer program allows a client to connect to a server and request a file from it, in which case the server 
will deliver the file requested to the user. It also can accept a file from the user in which case it will receive 
whatever file the user specified from the user.

### Prerequisites

* Python 2.7+

### Installing & Deployment

Clone the repository and locate the client.py and server.py files

Execute the server on one machine or on the same machine by running the command:

```
python server.py
```

By default the server will listen on port 7005 for incoming connections.

Execute the client on another machine, or the same machine and point it to the server IP address and port by running the command:

```
python client.py <destination_addr> <destination_port> <COMMAND> <filename>
```

## Built With

* [Python](https://python.org) - The programming language used

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/ghTravis/RawFileTransfer/tags).

* 1.0.0 - **Initial version** - Pushed to GitHub for public viewing

## Authors

* **Travis Ryder** - *Owner* - [TravisRyder.com](https://tavisryder.com)

See also the list of [contributors](https://github.com/ghTravis/RawFileTransfer/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* BCIT BTech Program

# A Basic Python web server
A simple web server for I used for developing a web interface to an embedded 
device.

# Installation

## Debian package

- Ensure the p3build package is installed. See [https://github.com/pjaos/p3build](https://github.com/pjaos/p3build) for details of this.
- Run `sudo p3build` in this folder to build the package.
- Run `sudo dpkg -i packages python-ws-1.0-2.noarch.rp`

## pip

- Run the `sudo pip3 install .` command.

# Running 

- Run `ws -h`

and the help text is displayed

```
Usage: Simple web server.

Options:
  -h, --help   show this help message and exit
  --port=PORT  Followed by the web server port (default=8080)
  --root=ROOT  Followed by the web server root path
  --cgi=CGI    A folder (in the root path) containing the cgi scripts
               (default=/cgi-bin).

```

The `--root` path must be provided and should point to the web server root folder.

The `--cgi` folder is optional.

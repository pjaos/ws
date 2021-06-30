# A Basic Python web server
A simple web server for I used for developing a web interface to an embedded 
device.

# Installation

## Debian package

- Ensure the pipenv2deb package is installed. See [https://pypi.org/project/pipenv2deb/]pipenv2deb) for details of this.
- Run `sudo ./build.sh` in this folder to build the package.
- Run `sudo dpkg -i packages/python-ws-1.1-all.deb`

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

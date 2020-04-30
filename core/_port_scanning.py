# this file is apart of NERO
import socket

def call(ip):
    print("\033[1;41m[+] Preparing Port Scanning Thread for {}\033[m".format(ip))

    try:
        for i in range(1,1025):
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = server.connect_ex((ip,i))
            if result == 0:
                print("[=] Port open from {} => {}".format(ip,i))
                server.close()
    except:
        pass

    print("\033[1;41m[+] Port scan finished for {}\033[m".format(ip))
    return
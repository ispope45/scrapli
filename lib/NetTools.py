# cording = utf-8
import socket


class NetTools:
    def port_check(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip, port))
            sock.close()
        except socket.error as e:
            result = 1
            print("Error : " + e)

        if result == 0:
            return True
        else:
            return False

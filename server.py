#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            ip_cliente = self.client_address[0]
            puerto_cliente = self.client_address[1]
            print("El cliente con IP:" + str(ip_cliente) + " y Puerto:" + 
            str(puerto_cliente) + " nos manda", line.decode('utf-8'))

if __name__ == "__main__":
    # Listens at localhost ('') port 6001 
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('', int(sys.argv[1])), EchoHandler) 
    except IndexError:
        sys.exit("Usage: python3 server.py puerto")
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")

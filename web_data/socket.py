# pylint: disable=invalid-name, not-callable, no-member, import-self

"""Demonstration of Python's built-in support for TCP Sockets"""


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  # Host and port number

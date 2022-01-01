# pylint: disable=invalid-name, not-callable, no-member, import-self

"""Demonstration of Python's built-in support for TCP Sockets"""

# Get the library
import socket

# Create the socket object, the 'doorway'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use the connect method on socket object to, well, connect!
mysock.connect(('data.pr4e.org', 80))

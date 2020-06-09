# -*- coding: utf-8 -*-

# Import the necessary modules
import threading
from drone.service import receive, choose_routine, close_socket

receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

choose_routine(2)
close_socket()

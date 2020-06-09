# -*- coding: utf-8 -*-

# Import the necessary modules
import threading
import services.drone.service as drone

receiveThread = threading.Thread(target=drone.receive)
receiveThread.daemon = True
receiveThread.start()

drone.choose_routine(3)
drone.close_socket()

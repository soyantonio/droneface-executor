import time
import socket
import threading


class Drone:
    def __init__(self):
        print("Preparing drone...")
        self.tello_address = ('192.168.10.1', 8889)
        self.local_address = ('', 9000)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.local_address)
        self.receiveThread = threading.Thread(target=self.receive)
        self.receiveThread.daemon = True
        self.receiveThread.start()

    def __del__(self):
        print("Terminando")
        self.sock.close()

    def send(self, message, delay):
        """
            Send the message to Tello and allow for a delay in seconds
        """
        try:
            self.sock.sendto(message.encode(), self.tello_address)
            print("Sending message: " + message)
        except Exception as e:
            print("Error sending: " + str(e))

        time.sleep(delay)

    def receive(self):
        """
            Receive the message from Tello.
            Continuously loop and listen for incoming messages
        """
        while True:
            try:
                response, ip_address = self.sock.recvfrom(128)
                print("Received message: " + response.decode(encoding='utf-8'))
            except Exception as e:
                # If there's an error close the socket
                self.sock.close()
                print("Error receiving: " + str(e))
                break

    def box_mission(self):
        self._init_mission("Box rutine iniciating... ")

        for i in range(4):
            self.send("forward " + str(50), 8)
            self.send("cw " + str(90), 8)
        self.send("up " + str(50), 8)
        for i in range(4):
            self.send("forward " + str(50), 8)
            self.send("cw " + str(90), 8)

        self.send("ccw " + str(360), 10)
        self._success_mission()

    def star_rutine(self):
        self._init_mission("Star rutine iniciating... ")

        for i in range(5):
            self.send("forward " + str(75), 8)
            self.send("ccw " + str(324), 10)
            self.send("forward " + str(75), 8)
            self.send("cw " + str(252), 8)

        self.send("ccw " + str(360), 10)
        self._success_mission()

    def up_down_180(self):
        self._init_mission("up down 180 rutine iniciating... ")

        for i in range(2):
            self.send("up " + str(50), 10)
            self.send("cw " + str(180), 8)
            self.send("down " + str(50), 10)
            self.send("cw " + str(180), 8)
            self.send("up " + str(50), 10)
            self.send("ccw " + str(180), 8)
            self.send("down " + str(50), 10)
            self.send("ccw " + str(180), 8)

        self.send("ccw " + str(360), 10)
        self._success_mission()

    def launch(self, subject_id):
        if subject_id == 0:
            print("0")
        elif subject_id == 1:
            print("1")
            self.box_mission()
        elif subject_id == 2:
            print("2")
            self.star_rutine()
        elif subject_id == 3:
            print("3")
            self.up_down_180()
        else:
            print("Execution terminated")

    def _init_mission(self, message: str):
        print(message)
        self.send("command", 3)
        self.send("takeoff", 5)

    def _success_mission(self):
        self.send("land", 5)
        self.send("land", 5)
        print("Mission completed successfully!")
        self.sock.close()

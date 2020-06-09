import time
import socket


# IP and port of Tello
tello_address = ('192.168.10.1', 8889)
# IP and port of local computer
local_address = ('', 9000)
# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the local address and port
sock.bind(local_address)


# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
    # Try to send the message otherwise print the exception
    try:
        sock.sendto(message.encode(), tello_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    # Delay for a user-defined period of time
    time.sleep(delay)


# Receive the message from Tello
def receive():
    # Continuously loop and listen for incoming messages
    while True:
        # Try to receive the message otherwise print the exception
        try:
            response, ip_address = sock.recvfrom(128)
            print("Received message: " + response.decode(encoding='utf-8'))
        except Exception as e:
            # If there's an error close the socket and break out of the loop
            sock.close()
            print("Error receiving: " + str(e))
            break


def box_mission():
    print("Box rutine iniciating... ")
    send("command", 3)
    send("takeoff", 5)

    for i in range(4):
        send("forward " + str(50), 4)
        send("cw " + str(90), 3)

    send("up " + str(50), 4)
    for i in range(4):
        send("forward " + str(50), 4)
        send("cw " + str(90), 3)

    send("ccw " + str(360), 7)
    # Land
    send("land ", 5)
    # Print message
    print("Mission completed successfully!")
    # Close the socket
    sock.close()


def star_rutine():
    print("Star rutine iniciating... ")
    send("command", 3)
    send("takeoff", 5)

    for i in range(5):
        send("forward " + str(75), 4)
        send("ccw " + str(324), 3)
        send("forward " + str(75), 4)
        send("cw " + str(252), 3)
    send("ccw " + str(360), 7)
    send("land ", 5)

    print("Mission completed successfully!")
    sock.close()


def up_down_180():
    print("up down 180 rutine iniciating... ")

    send("command", 3)
    send("takeoff", 5)

    for i in range(2):
        send("up " + str(50), 3)
        send("cw " + str(180), 4)
        send("down " + str(50), 3)
        send("cw " + str(180), 4)
        send("up " + str(50), 3)
        send("ccw " + str(180), 4)
        send("down " + str(50), 3)
        send("ccw " + str(180), 4)

    send("ccw " + str(360), 7)
    send("land", 5)
    print("Mission completed successfully!")
    sock.close()


def choose_routine(subject_id):
    if subject_id == 0:
        print("0")
    elif subject_id == 1:
        print("1")
        box_mission()
    elif subject_id == 2:
        print("2")
        star_rutine()
    elif subject_id == 3:
        print("3")
        up_down_180()
    else:
        print("Execusion terminated")


def close_socket():
    sock.close()

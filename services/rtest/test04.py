# import time
import cv2


# class Testing:
#     def __init__(self):
#         print("Inserted")
#         self.video = cv2.VideoCapture(0)

#     def __del__(self):
#         print("Stopped")
#         self.video.release()

#     def get_frame(self):
#         # extracting frames
#         ret, frame = self.video.read()
#         # if frame is None:
#         #     None
#         # _, jpeg = cv2.imencode('.jpg', frame)
#         if frame is not None:
#             cv2.imshow('f', frame)
#         # return jpeg.tobytes()


print('Test 0, wait')
# test = Testing()
# while(True):
#     test.get_frame()
# time.sleep(2)
video = cv2.VideoCapture(0)
while(True):
    ret, frame = video.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()

print('Test 0, done')

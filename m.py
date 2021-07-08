import cv2
import time
import numpy as np
import argparse
import os
import smtplib
import imghdr
import face_recognition
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
from email.message import EmailMessage

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()

while True:
    def anotheperson():
        Sender_Email = "kalyanvanan00@gmail.com"
        Reciever_Email = "kallurisumanth0128@gmail.com"
        Password = 'gvdbhqltmavjjiew'
        newMessage = EmailMessage()
        newMessage['Subject'] = "Malpractice"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('!!!other person found')
        with open('opencv_frame.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)
    def personnotfound():
        Sender_Email = "kalyanvanan00@gmail.com"
        Reciever_Email = "kallurisumanth0128@gmail.com"
        Password = 'gvdbhqltmavjjiew'
        newMessage = EmailMessage()
        newMessage['Subject'] = "Malpractice"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('!!!No person found')
        with open('opencv_frame.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)
    def mobiledetected():
        Sender_Email = "kalyanvanan00@gmail.com"
        Reciever_Email = "kallurisumanth0128@gmail.com"
        Password = 'gvdbhqltmavjjiew'
        newMessage = EmailMessage()
        newMessage['Subject'] = "Malpractice"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('!!!THIS PERSON FOLLOWED THE MALPRACTICE mobile detected')
        with open('opencv_frame.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)



    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 20: #<---- Check if 5 sec passed
        img_name = "opencv_frame.png"
        cv2.imwrite(img_name, frame)
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True,
                        help="path to input image")
        ap.add_argument("-c", "--confidence", type=float, default=0.5,
                        help="minimum probability to filter weak detections, IoU threshold")
        ap.add_argument("-t", "--threshold", type=float, default=0.3,
                        help="threshold when applying non-maxima suppression")
        args = vars(ap.parse_args())

        # load the COCO class labels our YOLO model was trained on
        labelsPath = 'yolo-coco\\coco.names'
        LABELS = open(labelsPath).read().strip().split("\n")
        print(LABELS)
        print(len(LABELS))
       # print(LABELS[67])

        # initialize a list of colors to represent each possible class label
        COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
                                   dtype="uint8")

        # paths to the YOLO weights and model configuration
        weightsPath = 'yolo-coco\\yolov3.weights'
        configPath = 'yolo-coco\\yolov3.cfg'

        # load our YOLO object detector trained on COCO dataset (80 classes)
        net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

        # load our input image and grab its spatial dimensions
        image = cv2.imread(args["image"])
        (H, W) = image.shape[:2]

        # determine only the *output* layer names that we need from YOLO
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        # construct a blob from the input image and then perform a forward
        # pass of the YOLO object detector, giving us our bounding boxes and
        # associated probabilities
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                                     swapRB=True, crop=False)
        net.setInput(blob)
        layerOutputs = net.forward(ln)

        # initialize our lists of detected bounding boxes, confidences, and
        # class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > args["confidence"]:
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center (x, y)-coordinates of the bounding
                    # box followed by the boxes' width and height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top and
                    # and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    print("lc",classIDs)
                    if classID == 67:
                        mobiledetected()
                    classIDs.append(classID)
                    print("hlo")
                    if (0 not in classIDs) or len(classIDs)==0:
                        personnotfound()
                    else:
                        imgElon = face_recognition.load_image_file('sumanth09.jpg')
                        imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
                        facesCurFrame = face_recognition.face_locations(imgElon)
                        imgTest = face_recognition.load_image_file('opencv_frame.png')
                        imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
                        facesCurFrame1 = face_recognition.face_locations(imgTest)

                        if len(facesCurFrame1) != 0:
                            if len(facesCurFrame) != 0:
                                faceLoc = face_recognition.face_locations(imgElon)[0]
                                encodeElon = face_recognition.face_encodings(imgElon)[0]
                                cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),
                                              (255, 0, 255), 2)

                                faceLocTest = face_recognition.face_locations(imgTest)[0]
                                encodeTest = face_recognition.face_encodings(imgTest)[0]
                                cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]),
                                              (faceLocTest[1], faceLocTest[2]),
                                              (255, 0, 255), 2)

                                results = face_recognition.compare_faces([encodeElon], encodeTest)
                                print(results)
                                if results:
                                    continue
                                else:
                                    anotheperson()


        # apply non-maxima suppression to suppress weak, overlapping bounding boxes
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"],
                                args["threshold"])

        # ensure at least one detection exists
        if len(idxs) > 0:
            # loop over the indexes we are keeping
            for i in idxs.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])

                # draw a bounding box rectangle and label on the image
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
                text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
                cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

        # show the output image
  #      cv2.imshow("Image", image)
        print("hlohlo")
        print(len(classIDs))
        if (0 not in classIDs) or len(classIDs) == 0:
            personnotfound()
        print(boxes)
        print(confidences)
        print(classIDs)
      #  cv2.waitKey(0)
        start_time = time.time()
    img_counter += 1
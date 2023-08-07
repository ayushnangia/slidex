import cv2
import numpy as np
import os
import shutil

def extract_slides(file_path, thre):
    # Load the video
    cap = cv2.VideoCapture(file_path)

    # If the 'slides' folder exists, delete it
    if os.path.exists('slides'):
        shutil.rmtree('slides')
        
    # Create a new 'slides' folder
    os.makedirs('slides')

    # Initialize variables
    prev_frame = None
    slide_num = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if prev_frame is not None:
                # Compute the absolute difference between the current frame and the previous frame
                frame_delta = cv2.absdiff(prev_frame, gray)

                # Compute the mean of the frame delta
                mean_delta = np.mean(frame_delta)

                # If the mean delta is large enough, assume this is a new slide
                if mean_delta > thre:  # You may need to adjust this threshold
                    slide_num += 1
                    slide_path = os.path.join('slides', f'slide_{slide_num}.jpg')
                    cv2.imwrite(slide_path, frame)

            # Set the current frame as the previous frame for the next iteration
            prev_frame = gray
        else:
            break
    print("Number of slides: ", slide_num,thre, file_path )
    # Release the video file
    cap.release()
    return 'slides'

import cv2
import logging

class VideoStream:
    """Simple class to work with video stream"""

    # setting input_video_file to None means using camera
    def __init__(self, input_video_file):
        """Creates instance of the class and inits its fields

        Parameters
        ----------
        :param input_video_file: name of the file with video input. If None, then camera input stream is used.
        :type  input_video_file: string
        """
        self.input_video_file = input_video_file
        self.video = None

    def start(self):
        """Inits input video stream and get it ready for the streaming

        :return: True if video stream inited successfully, False otherwise
        """
        if self.video != None:
            logging.error("Could not open video: another video stream is active")
            return False

        # Opening video stream
        logging.info("opening video stream...")
        if self.input_video_file == None:
            self.video = cv2.VideoCapture(0)
        else:
            self.video = cv2.VideoCapture(self.input_video_file)
        # Exit if video not opened.
        if not self.video.isOpened():
            logging.error("Could not open video")
            return False

        # Read first frame.
        ok, frame = self.video.read()
        if not ok:
            logging.error("Could not get frame")
            self.release()
            return False
        return True

    def frame(self):
        """Read and return next available frame form the video stream

        :return: video frame
        """
        return self.video.read()

    def release(self):
        """Release video stream"""
        logging.info("releasing video stream...")
        if self.video is not None:
            self.video.release()
        self.video = None

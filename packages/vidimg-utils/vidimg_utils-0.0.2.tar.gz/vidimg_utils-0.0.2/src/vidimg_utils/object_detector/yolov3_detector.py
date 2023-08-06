from vidimg_utils.object_detector.detector import Detector
from vidimg_utils.object_detector.detection import Detection
import logging
import cv2
import numpy as np

class YoloV3ObjectsDetector(Detector):
    """Class responsible for objects detection. Current implementation uses dnn module from OpenCV, and YOLOv3 model.
    YOLO model: https://github.com/pjreddie/darknet
    """

    def __init__(self, path_to_weights, path_to_config, supported_classes):
        """Creates instance of the class and initialises all parameters

        Parameters
        ----------
        :param path_to_weights: path to file with network weights
        :type  path_to_proto: string
        :param path_to_config: path to file with the network config
        :type  path_to_model: string
        :param supported_classes: array of strings, which contains types of all the supported classes of objects, that this
                                  network can detect and recognise. If array is empty, or variable is not an array of strings,
                                  exception will be thrown
        :type  supported_classes: array
        """
        if not isinstance(supported_classes, list):
            raise ValueError("Supported classes parameter is not a list of strings")
        self.supported_classes = supported_classes
        self.scale = 0.00392
        self.nms_threshold = 0.4
        self.n_network = cv2.dnn.readNet(path_to_weights, path_to_config)        
        self.output_layers = self.__get_output_layers()
    
    
    def recognise(self, image, classes = None, confidence_threshold = 0.5):
        """Overrides Detector.recognise()"""
        # create input blob 
        blob = cv2.dnn.blobFromImage(image, self.scale, (416,416), (0,0,0), True, crop=False)
        # set input blob for the network
        self.n_network.setInput(blob)
        # detect objects
        all_detections = self.n_network.forward(self.output_layers)
        # processing detections, and converting ones with propert confidence threshold into boxes to be drawn over the original image
        class_ids, confidences, boxes = self.__process_detections(image, all_detections, classes, confidence_threshold)
        return self.__filter_out_overlapping_detections(class_ids, confidences, boxes, confidence_threshold)
    
    
    def __filter_out_overlapping_detections(self, class_ids, confidences, boxes, confidence_threshold):
        # run NMS (non-max suppression) for detections from the dnn module. It removes boxes with high overlapping.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, self.nms_threshold)
        processed_detections = []
        for i in indices:
            box = boxes[i]
            (x, y, w, h) = box[0:]
            processed_detections.append(Detection(class_ids[i], confidences[i], x, y, x + w, y + h))
        return processed_detections
    
    
    def __process_detections(self, image, all_detections, classes, confidence_threshold):
        img_width = image.shape[1]
        img_height = image.shape[0]
        class_ids = []
        confidences = []
        boxes = []
        for detections in all_detections:
            for detection in detections:
                scores = detection[5:]
                class_id = np.argmax(scores)
                if self.__is_of_an_interested_class(class_id, classes):
                    confidence = scores[class_id]
                    if confidence > confidence_threshold:
                        center_x = int(detection[0] * img_width)
                        center_y = int(detection[1] * img_height)
                        w = int(detection[2] * img_width)
                        h = int(detection[3] * img_height)
                        x = center_x - w / 2
                        y = center_y - h / 2
                        class_ids.append(class_id)
                        confidences.append(float(confidence))
                        boxes.append([x, y, w, h])
        return class_ids, confidences, boxes
    
    
    def __is_of_an_interested_class(self, detected_class_id, classes):
        if classes == None:
            return True
        if not isinstance(classes, list):
            logging.warn("Passed list of classes required for object detesions is not a list")
            return False
        if detected_class_id >= len(self.supported_classes):
            logging.warn("Detected class id {} does not belong to the range of supported classes".format(str(detected_class_id)))
            return False
        detected_class = self.supported_classes[detected_class_id]
        return detected_class in classes

    
    def __get_output_layers(self):
        """Retrieve output layers of the neural network. We will pass blobs to those layers later

        :return: output layers of the neural network
        """
        layer_names = self.n_network.getLayerNames()
        output_layers = [layer_names[i - 1] for i in self.n_network.getUnconnectedOutLayers()]
        return output_layers
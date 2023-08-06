from abc import ABCMeta, abstractmethod

class Detector(metaclass=ABCMeta):
    """Interface defines main API for object detections on imgages or video frames"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'recognise') and 
                callable(subclass.recognise) or 
                NotImplemented)

    @classmethod
    def version(self): 
        """Version of the API"""
        return "1.0"
    
    @abstractmethod
    def recognise(self, image, classes = None, confidence_threshold = 0.5):
        """Process incoming image and recognise objects.
        
        Parameters
        ----------
        :param image:                image or the frame from the input video stream
        :param classes:              classes of the objects which are needed to recognise. None (defaul value t) means all recognised objects
        :param confidence_threshold: threshold for the recognition confidence for the objects to be included into result set. 
                                     Default value is 0.5
        
        Returns
        ----------
        :return: collection of all detections
        :type: array of Detection objects
        """
        raise NotImplementedError

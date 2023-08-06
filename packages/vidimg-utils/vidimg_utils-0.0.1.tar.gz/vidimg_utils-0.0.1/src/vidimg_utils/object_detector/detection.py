class Detection:
    """Simple class, that contains meta data about detected object"""
    
    def __init__(self, class_id, confidence, bounding_box_start_x, bounding_box_start_y, bounding_box_end_x, bounding_box_end_y):
        """Creates instance of the class and initialises all parameters
        
        Parameters
        ----------
        :param class_id: if of detected class
        :type  class_id: int
        :param confidence: detection confidence
        :type  confidence: float
        :param bounding_box_start_x: top-left corner x coordinate of the bounding box for detection
        :type  bounding_box_start_x: int
        :param bounding_box_start_y: top-left corner y coordinate of the bounding box for detection
        :type  bounding_box_start_y: int
        :param bounding_box_end_x: bottom-right corner x coordinate of the bounding box for detection
        :type  bounding_box_end_x: int
        :param bounding_box_end_y: bottom-right corner y coordinate of the bounding box for detection
        :type  bounding_box_end_y: int
        """
        self.__class_id = class_id
        self.__confidence = confidence
        self.__x0 = bounding_box_start_x
        self.__y0 = bounding_box_start_y
        self.__x1 = bounding_box_end_x
        self.__y1 = bounding_box_end_y
    
    def class_id(self):
        return self.__class_id
    
    def confidence(self):
        return self.__confidence
    
    def x0(self):
        return self.__x0
    
    def y0(self):
        return self.__y0
    
    def x1(self):
        return self.__x1
    
    def y1(self):
        return self.__y1
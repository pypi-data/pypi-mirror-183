from typing import Callable
import cv2
import numpy as np
from typing import Optional
from threading import Thread

class InvalidInputError(Exception): ...

def _assert_is_type(input, expected_type:type):

    if not isinstance(input, expected_type):
        raise InvalidInputError(f"Expected a '{expected_type}', received '{type(input)}'")


class VideoStreamer:
    """
    Use this class the read videos from path or from webcam
    Use the on_next_frame method as a decorator to wrap  

    """

    def __init__(self, cap, window_name="video", waitkey=1) -> None:
        
      self.__cap = cap
      self.__tasks = []
      self.__pre_tasks = []
      self.window_name = window_name
      self.waitkey = waitkey
      self._ret = None
      self._frame = None

      
    def from_webcam(cam_index:int=0,window_name:str="video", waitkey:int=1):

        _assert_is_type(cam_index, int)
       
        return VideoStreamer(
           cap = cv2.VideoCapture(cam_index),
           window_name=window_name, 
           waitkey=waitkey 
       )
       
    def on_next_frame(self, shape:Optional[tuple[int,int]]=None):
        """
        Use as a decorator to wrap your function\n
        The cam window is drawn automatically after the function has been called.\n
        Example: \n

        stream =  VideoStreamer.from_webcam()
        @stream.on_next_frame()
        def func(image):
             ...


        """
        if not shape is None:
           self.__pre_tasks.append(lambda img: cv2.resize(img, shape, interpolation=cv2.INTER_AREA))
           
        def inner(func:Callable[[np.ndarray], None]):
            self.__tasks.append(func)  

        return inner    

        
    def from_video_input(path, window_name="video", waitkey=1):

        _assert_is_type(path, str)

        return VideoStreamer(
            cap=cv2.VideoCapture(path),
           window_name=window_name, 
           waitkey=waitkey 
        ) 
    
    def __step(self, frame):
        
        for fn in self.__tasks: 
            
            fn(frame)
            
            cv2.imshow(self.window_name, frame)
            cv2.waitKey(self.waitkey)
        
    def start(self):
        """
        Using the method to start loading the next frames
        """

        def update():
        
            while True:
                self._ret, self._frame = self.__cap.read()

        thread = Thread(target=update)
        thread.daemon = True
        thread.start()  

        while True:

            if self._ret is None: continue
            if not self._ret: return self.close()

            frame = self._frame
            for task in self.__pre_tasks:
                frame = task(frame)

            self.__step(frame)  

    def close(self):
        self.__cap.release()
        cv2.destroyAllWindows()            
        
    
    
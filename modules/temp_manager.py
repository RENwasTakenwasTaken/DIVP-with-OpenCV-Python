'''
Manages folder "temp" and files written to it.
Deletes after class destruction.
Or, provides manual clearance of temp folder.
'''

import os
import cv2
import time
import shutil
import numpy as np

class TempManager():
    def __init__(self, temp_folder_path="temp"):
        self.temp_folder_path = temp_folder_path

    def clear_temp_folder(self):
        try:
            shutil.rmtree(self.temp_folder_path)
        except PermissionError:
            print("Kept (temp) folder.")
            return  # No need to make folder again.
        
        os.makedirs(self.temp_folder_path)

    def save_to_temp(self, file, filepath):
        if isinstance(file, np.ndarray):
            file_path = f"{self.temp_folder_path}/{filepath}"

            if not os.path.exists(self.temp_folder_path):
                os.mkdir(self.temp_folder_path)

            cv2.imwrite(file_path, file)
            return file_path

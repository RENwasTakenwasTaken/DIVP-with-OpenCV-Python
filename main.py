'''
Author: Aryan Aich
Date of Publishing: 16/07/2026

Description:
An image editing software based on Kivy-Python and OpenCV-Python.
Incorporating DIVP concepts as and when taught.
'''

import cv2

from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

from modules.file_manager import FileDialog

Builder.load_file("ui.kv")

class ApplicationScreen(BoxLayout):
    image_source = StringProperty("")
    image_width = NumericProperty(100)
    image_height = NumericProperty(100)

    def open_file_dialog(self):
        try:
            self.image_source = FileDialog.open_image()

            img = cv2.imread(self.image_source)
            self.image_height, self.image_width = img.shape[:2]

        except ValueError:
            print("Something is gone wrong with source setting.")
        # To be loaded using some sys libr.

class ArchImageEditor(App):
    def build(self):
        return ApplicationScreen()

if __name__ == "__main__":
    ArchImageEditor().run()

'''
Author: Aryan Aich
Date of Publishing: 16/07/2026

Description:
An image editing software based on Kivy-Python and OpenCV-Python.
Incorporating DIVP concepts as and when taught.
'''

import cv2
import time
import traceback

from kivy.app import App
from kivy.base import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from modules.file_manager import FileDialog
from modules.temp_manager import TempManager
from modules.image_widget import ImageCanvas
from modules.userinputmodal import InputPopup

Builder.load_file("ui.kv")

class ApplicationScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_canvas = self.ids.image_canvas

    def open_file_dialog(self):
        try:
            image_path = FileDialog.open_image()
            self.image_canvas.set_image(image_path=image_path)
            self.update_file_path(image_path)

        except AttributeError:
            print("Image not selected.")

    def update_file_path(self, path):
        w, h = self.image_canvas.get_image_size()
        self.ids.title_bar_text.text = f"{path} {w}x{h}"

    def apply_image_negation(self):
        self.image_canvas.negate()

    def apply_image_log_transform(self):
        self.image_canvas.log_transform()

    def print_image_data(self):
        self.image_canvas.print_image_data()

    def resize_image(self):
        def _resize_image(w, h):
            self.image_canvas.resize_image(w, h)

        InputPopup(_resize_image, ["width", "height"]).open()

    def gamma_transform(self):
        self.image_canvas.gamma_transform()

class ArchImageEditor(App):
    def build(self):
        return ApplicationScreen()
    
    def on_stop(self):
        TempManager().clear_temp_folder()

if __name__ == "__main__":
    ArchImageEditor().run()

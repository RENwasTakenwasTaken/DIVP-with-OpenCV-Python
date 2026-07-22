from kivy.base import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout

from modules.temp_manager import TempManager
from modules.image_operations import ImageOperations as image_operations

Builder.load_file("modules/image_widget.kv")

temp_manager = TempManager()

class ImageCanvas(BoxLayout):
    # These variables are directly referred by KV. Static variables.
    image_source = StringProperty("")
    image = []      # Cached image file. Avoiding frequent reading from FS.

    def _extract_extension(self, image_path):
        return image_path.split('.')[-1]
    
    def get_image(self):
        return self.image
    
    def get_image_size(self):
        return (self.image.shape[0], self.image.shape[1])

    def set_image(self, image=None, image_path=None):
        '''
        Updates image based on either image path or given image.

        If image path is given, read it and set as self.image.
        If image path is None, try reading image.

        If both are None, print an error.
        '''

        if image_path is None and image is None:
            raise ValueError("Image must be given if Image Path is absent.")
        
        if image is None:
            self.image = image_operations.read_image(image_path)
            extension = self._extract_extension(image_path)

        if image_path is None:
            self.image = image
            extension = self._extract_extension(self.image_source)

        self.image_source = temp_manager.save_to_temp(self.image, f"temp.{extension}")
        self.ids.image.reload()

    def negate(self):
        self.set_image(image_operations.image_negative(self.image))

    def log_transform(self):
        self.set_image(image_operations.log_transform(self.image))

    def print_image_data(self):
        print(self.image)

    def resize_image(self, w, h):
        self.set_image(image_operations.resize_image(self.image, w, h))

    def gamma_transform(self):
        self.set_image(image_operations.gamma_transform(self.image))

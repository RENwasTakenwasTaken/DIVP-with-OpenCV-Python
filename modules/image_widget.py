from kivy.base import Builder
from kivy.properties import StringProperty

from kivy.uix.boxlayout import BoxLayout

Builder.load_file("image_widget.kv")

class ImageWidget(BoxLayout):
    image_filename = StringProperty("")
    image_source = StringProperty("")

    def set_source(self, source):
        self.image_source = source
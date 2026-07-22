from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Builder.load_file("modules/userinputmodal.kv")

class InputPopup(Popup):
    def __init__(self, callback, input_fields=[], **kwargs):
        super().__init__(**kwargs)

        self.title = "Enter Value"
        self.size_hint = (0.5, 0.3)
        self.auto_dismiss = False

        self.input_fields = []  # Used for storing objects for text inputs. Not the passed parameters.

        # Create the main text input container.
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        # Create the text input(s) container.
        input_fields_layout = BoxLayout(orientation='vertical')

        # Create one or many text inputs.
        for field in input_fields:
            ti = TextInput(
                multiline=False,
                hint_text=field
            )

            input_fields_layout.add_widget(ti)
            self.input_fields.append(ti)

        ok = Button(text="OK", on_release=lambda x: self.submit(callback))
        cancel = Button(text="Cancel", on_release=self.dismiss)

        layout.add_widget(input_fields_layout)
        layout.add_widget(ok)
        layout.add_widget(cancel)

        self.content = layout

    def submit(self, callback):
        values = tuple(
            int(widget.text)
            for widget in self.input_fields
        )

        callback(*values)   # *unpacks tuple into csv arguments.
        self.dismiss()

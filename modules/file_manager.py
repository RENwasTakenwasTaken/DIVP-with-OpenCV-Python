from tkinter import Tk
from tkinter.filedialog import askopenfilename

class FileDialog:
    @staticmethod
    def open_image():
        root = Tk()
        root.withdraw()      # Hide Tk window
        root.attributes("-topmost", True)

        filename = askopenfilename(
            title="Open Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tif *.tiff *.webp *.avif"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpg *.jpeg"),
                ("All Files", "*.*")
            ]
        )

        root.destroy()

        if filename:
            print(filename)
            return filename

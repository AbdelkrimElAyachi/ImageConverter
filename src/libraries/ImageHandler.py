from PIL import Image
from PIL.ExifTags import TAGS
import os

class ImageHandler :

    def __init__(self, path, folder="results") -> None:
        self.path = os.path.normpath(path)
        self.ext = self.path.split(".")[1]
        self.fname = self.path.split("\\")[-1].split(".")[0]
        self.folder = folder
        self.create_folder()
        print(" "*25+f"path : {self.path} || extension : {self.ext} || file name : {self.fname} || folder : {self.folder}")
        try:
            self.img = Image.open(self.path)  
        except Exception as e:
            exit(f"error in Image.open : {e}")

    def create_folder(self) -> None:
        if not os.path.exists(self.folder):
            print(f"creating folder {self.folder} ")
            os.makedirs(self.folder)

    def get_meta_data(self) -> dict:
        extra_data_result = {}
        extradata = self.img.getexif()
        for tagid in extradata:
            tagname = TAGS.get(tagid,tagid)
            value = extradata.get(tagid)
            extra_data_result[tagname] = value
        return extra_data_result    

    def convert_to_webp(self):
        try:
            self.img.save(f"{self.folder}\\{self.fname}.webp",format="webp",loseless=False,quality=80)
            # When loseless set to True, it applies lossless compression, resulting in larger file sizes but no loss in quality. The default value is False.
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")

    def convert_to_jpeg(self):
        try:
            self.img.save(f"{self.folder}\\{self.fname}.jpeg",format="JPEG",quality=75)
            # Specifies the image quality level as an integer between 1 and 95 or 100.
            # Higher values indicate better quality and larger file sizes. The default value is 75.
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")

    def convert_to_gif(self,transparent_color):
        try:
            self.img.save(f"{self.folder}\\{self.fname}.gif",format="GIF",transparency=transparent_color)
            # In a GIF image, one color index can be designated as the transparent color. 
            # This means that any pixel in the image with that color index will be considered transparent when rendered, 
            # allowing the background to show through. 
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}") 


    def convert_to_png(self):
        try:
            self.img.save(f"{self.folder}\\{self.fname}.png",format="PNG",optimize=True,compress_level=6)
            # when optimize set to true it applies different compression techniques to reduce file size default is false 
            # compress_level Specifies the compression level as an integer between 0 and 9. Higher values result in better compression but slower processing. The default value is 6. 
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")





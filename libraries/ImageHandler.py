from PIL import Image
from PIL.ExifTags import TAGS
import os

class ImageHandler :


    def __init__(self,path,folder="results") -> None:

        self.path = os.path.normpath(path)
        print("path : ",self.path)
        self.ext = self.path.split(".")[1]
        print("extension : ",self.ext)
        self.fname = self.path.split("\\")[-1].split(".")[0]
        print("file name : ",self.fname)
        self.folder = folder
        print("folder : ",self.folder)

        try:
            self.img = Image.open(self.path)  
        except Exception as e:
            print(e)
            exit("exit the app with code error 1")





    def createFolder(self):
        if not os.path.exists(self.folder):
            print(f"creating folder {self.folder} ")
            os.makedirs(self.folder)



    def getMetaData(self):

        extra_data_result = {}
        extradata = self.img.getexif()

        for tagid in extradata:

            tagname = TAGS.get(tagid,tagid)
            value = extradata.get(tagid)
            extra_data_result[tagname] = value

        return extra_data_result    



    def convertToWebp(self):
        self.createFolder()
        try:
            self.img.save(f"{self.folder}\\{self.fname}.webp",format="webp",loseless=False,quality=80)
            # When loseless set to True, it applies lossless compression, resulting in larger file sizes but no loss in quality. The default value is False.

        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")



    def convertToJpeg(self):
        self.createFolder()
        try:
            self.img.save(f"{self.folder}\\{self.fname}.jpeg",format="JPEG",quality=75)
            # Specifies the image quality level as an integer between 1 and 95 or 100.
            # Higher values indicate better quality and larger file sizes. The default value is 75.
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")



    def convertToGif(self,TransparentColor):
        self.createFolder()
        try:
            self.img.save(f"{self.folder}\\{self.fname}.gif",format="GIF",transparency=TransparentColor)
            # In a GIF image, one color index can be designated as the transparent color. 
            # This means that any pixel in the image with that color index will be considered transparent when rendered, 
            # allowing the background to show through. 
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}") 


    def convertToPng(self):
        self.createFolder()
        try:
            self.img.save(f"{self.folder}\\{self.fname}.png",format="PNG",optimize=True,compress_level=6)
            # when optimize set to true it applies different compression techniques to reduce file size default is false 
            # compress_level Specifies the compression level as an integer between 0 and 9. Higher values result in better compression but slower processing. The default value is 6. 
        except Exception as e:
            print(f"Error processing {self.fname}.{self.ext} : {e}")





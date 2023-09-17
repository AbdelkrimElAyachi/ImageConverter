import sys
from libraries.ImageHandler import ImageHandler 
from libraries.InputsReader import inputsReader
import os

formats = ["webp","png","jpg","jpeg","gif"]
reader = inputsReader(sys.argv)

def converting(img,specific_format):
    if(specific_format=="webp"):
        img.convertToWebp()
    elif(specific_format=="png"):
        img.convertToPng()    
    elif(specific_format=="jpg"):
        img.convertToJpeg()    
    elif(specific_format=="gif"):
        img.convertToGif(False)    
    elif(specific_format=="jpeg"):
        img.convertToJpeg()    


def convertGroup(folder,specific_folder,specific_format):

    for file_name in os.listdir(folder):
        file_path = os.path.join(folder,file_name)
        if(os.path.isfile(file_path)):
            if(file_path.endswith(".png") or file_path.endswith("jpg") or file_path.endswith("gif") or file_path.endswith("jpeg") or file_path.endswith("jfif")):
                convertSingle(file_path,specific_folder,specific_format)


def convertSingle(path,specific_folder,specific_format):
    img = ImageHandler(path,specific_folder)
    converting(img,specific_format)

def main(args):

    if(len(args["-in"])>1):
        print("you need to specific one folder to export the images in")
        return False
    specific_folder = args["-in"][0]

    if(len(args["-to"]) > 1):
        print("you need to choose one specific format that you wan the image to convert to ")
        return False
    
    if args["-to"][0] not in formats :
        print(f"the format {args['-to'][0]} does not exist ")       
        return False
    specific_format = args["-to"][0]
    
    if(len(args["--paths"]) != 0):

        for path in args["--paths"]:
            if(os.path.isdir(path)):
                print(f"you need to use -g befor the folder paths : {path}")
                return False
            if not os.path.exists(path):
                print(f"the path {path} does not exist")
                return False
            else:
                print(f"converting this file {path} to {specific_format} and put it in {specific_folder}")
                convertSingle(path,specific_folder,specific_format)

    if ("-g" in args):
        if(len(args["-g"])!=0):
            for path_folder in args["-g"]:     
                if(not os.path.exists(path_folder)):
                    print(f"the path {path_folder} does not exist")
                else:
                    convertGroup(path_folder,specific_folder,specific_format)
        else:
            print("you need to specify path for the folder that contains the images")        


         

if(__name__=="__main__"):
    args = reader.getArgs()
    main(args)

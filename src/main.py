import sys
from libraries.ImageHandler import ImageHandler 
from libraries.InputsReader import InputsReader
import os

def check_inputs(inputs, formats) -> bool:
    if( (len(inputs["--paths"]) == 0) and ("-g" not in inputs)):
        print("you need to specify at least one image path")
        return False
    if(len(inputs["-in"])>1):
        print("you need to specific one folder to export the images in")
        return False
    if(len(inputs["-to"]) > 1):
        print("you need to choose one specific format that you wan the image to convert to ")
        return False
    if (inputs["-to"][0] not in formats):
        print(f"the format {inputs['-to'][0]} does not exist ")       
        return False
    if (("-g" in inputs) and  (len(inputs["-g"]) == 0)):
        print("you need to specify path for the folder that contains the images")   
        return False
    return True

def converting(img, specific_format):
    if(specific_format=="webp"):
        img.convert_to_webp()
    elif(specific_format=="png"):
        img.convert_to_png()    
    elif(specific_format=="jpg"):
        img.convert_to_jpeg()    
    elif(specific_format=="gif"):
        img.convert_to_gif(False)    
    elif(specific_format=="jpeg"):
        img.convert_to_jpeg()  


def convert_group(folder, specific_folder, specific_format):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder,file_name)
        if(os.path.isfile(file_path)):
            if(file_path.endswith(".png") or file_path.endswith("jpg") or file_path.endswith("gif") or file_path.endswith("jpeg") or file_path.endswith("jfif")):
                convert_single(file_path,specific_folder,specific_format)


def convert_single(path, specific_folder, specific_format):
    img = ImageHandler(path, specific_folder)
    converting(img, specific_format)

def main(inputs):
    specific_folder = inputs["-in"][0]
    specific_format = inputs["-to"][0]
    for path in inputs["--paths"]:
        if (os.path.isdir(path)):
            exit(f"you need to use -g befor the folder paths : {path}")
        if (not os.path.exists(path)):
            exit(f"the path {path} does not exist")
        else:
            print(f"converting image {path} to {specific_format} | the converted image in {specific_folder}")
            convert_single(path,specific_folder,specific_format)
    if("-g" in inputs):
        for path_folder in inputs["-g"]:     
            if(not os.path.exists(path_folder)):
                exit(f"the path {path_folder} does not exist")
            else:
                convert_group(path_folder,specific_folder,specific_format)

                 


         

if(__name__=="__main__"):
    formats = ["webp","png","jpg","jpeg","gif"]
    reader = InputsReader(sys.argv)
    if(not check_inputs(reader.inputs, formats)):
        exit(1)
    main(reader.inputs)

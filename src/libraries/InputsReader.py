
class InputsReader:

    def __init__(self,argv) -> None:
        self.inputs = {}
        for i in range(len(argv)):
            if argv[i][0] == "-" and i != 0:
                current = []
                self.inputs[argv[i]] = current
            elif i!=0:
                current.append(argv[i])
            elif i==0:
                current = []
                self.inputs["--paths"] = current      
      





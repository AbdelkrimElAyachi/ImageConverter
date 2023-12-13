
class inputsReader:


    def __init__(self,argv) -> None:
        
        self.lst = {}

        for i in range(len(argv)):

            if argv[i][0] == "-" and i != 0:
                current = []
                self.lst[argv[i]] = current

            elif i!=0:
                current.append(argv[i])

            elif i==0:
                current = []
                self.lst["--paths"] = current        


    def getArgs(self):
        return self.lst

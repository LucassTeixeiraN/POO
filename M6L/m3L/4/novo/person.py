class Person:
    def __init__(self, name, document):
        self.__name = name
        self.__document = document
        
    def getName(self):
     return self.__name
 
    def getDocument(self): 
        return self.__document
    
    
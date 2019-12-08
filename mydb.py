class MyDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self,connection_string):
        return self.connection

class Connection:
    def __init__(self):
        self.cur = Cursor()

    def Cursor(self):
        return self.cur
    
    def close(self):
        pass

class Cursor():
    def execute(self,query):
        if query =="1":
            return 123
        elif query =="2":
            return 321
        else:
            return -1

    def close(self):
        pass         


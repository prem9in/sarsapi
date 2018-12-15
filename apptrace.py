import datetime

class AppTrace:

    def __init__(self, traceEnabled):
        self.traces = []
        self.traceEnabled = traceEnabled
       

    def log(self, methodName, message):
        if self.traceEnabled == True:
            logitem = {
                "datetime": datetime.datetime.now().strftime("%c"),
                "method": methodName,
                "message": message
            }
            self.traces.append(logitem)
            print(logitem)

        
    def get(self):
        return self.traces


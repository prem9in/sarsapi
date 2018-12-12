import controller
import lookup
import indexer


indx = indexer.Indexer()
lp = lookup.Lookup()
ctrl = controller.Controller(lp, indx)
ctrl.load()

def stdout(listtoprint, title):
    print(title)
    for item in enumerate(listtoprint):
        print(item)
    print()


def starttest():
    searchcity = "Pittsburgh"
    searchstate = "PA"
    query_parameters = {"text": "", "city": searchcity, "state": searchstate}
    sresults = ctrl.Search(query_parameters)
    stdout(sresults, "Printing document by location")

def loadfiletest():
    lp.load()
    lookup = lp.get()
    stdout(lookup, "Look up")

# execute
if __name__ == '__main__':
    
    starttest()
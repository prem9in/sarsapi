import controller
import lookup
import indexer
import apptrace

trx = apptrace.AppTrace(True)
indx = indexer.Indexer(trx)
lp = lookup.Lookup(trx)
ctrl = controller.Controller(lp, indx, trx)


def stdout(listtoprint, title):
    print(title)
    for item in enumerate(listtoprint):
        print(item)
    print()


def starttest():
    ctrl.load()
    searchcity = "Pittsburgh"
    searchstate = "PA"
    query_parameters = {"text": "good pizza", "city": searchcity, "state": searchstate}
    sresults = []
    sresults.append(ctrl.Search(query_parameters))
    stdout(sresults, "Printing document by location")
    stdout(trx.get(), "Traces")

def loadlookuptest():
    lp.load()
    lookup = lp.get()
    stdout(lookup, "Look up")

def loadindexertest():
    indx.load()
    index = indx.get()
    stdout(index, "Index")


# execute
if __name__ == '__main__':
   # loadlookuptest()
   # loadindexertest()
    starttest()
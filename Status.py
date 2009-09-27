
from AmiTree import Container
from PlugIn import PlugIn
from xmppEngine import XMPPEngine

class Status(PlugIn):


    def __init__(self, token, configFile):
        PlugIn.__init__(self)
        self.architecture = "all"


        #plugin itself
        self.content = Container("plugin", token, "This is a Status Plugin")

        # set add container
        self.content.addContainer("cmd", "Buddies", "Show Buddies", self.getBuddies)


        self.content.addContainer("cmd", "Root", "Show Root Node", self.getRoot)

    def getBuddies(self, text=""):
        string = ""

        for elem in XMPPEngine.roster.getItems():
            string += elem+"\n"

        return string

    def getRoot(self, text=""):
        string = ""

        res = self.root().__str__()

        return res

    # returns the plugin as a tree
    def getTree(self):
        return self.content

    # just a little helper function
    def getText(self, var):
        try:
            var = var.strings["text"]
            return test
        except:
            return var
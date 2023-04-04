

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self, child):
        if child != None:
            self.writechain(child.parent)
            print(child.word)
            

    def __len__(self):
        return len(self.word)

    def __getitem__(self, index):
        return self.word[index]
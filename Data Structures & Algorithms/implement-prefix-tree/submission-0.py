class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:

            index = ord(c) - ord('a')
            
            if curr.children[index] == None:

                curr.children[index] = TrieNode()
            
            curr = curr.children[index]
        
        curr.isEndOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(len(word) - 1):

            index = ord(word[i]) - ord('a')

            if curr.children[index] != None:

                curr = curr.children[index]
            else:
                return False

        lastCharIndex = ord(word[-1]) - ord('a')

        if curr.children[lastCharIndex] != None and curr.children[lastCharIndex].isEndOfWord:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(len(prefix)):

            index = ord(prefix[i]) - ord('a')

            if curr.children[index] != None:

                curr = curr.children[index]
            else:
                return False

        return True
        
        
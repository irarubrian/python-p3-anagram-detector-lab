class Anagram:
    def __init__(self, word):
        self.word = word.lower() 

    def match(self, words):
        return [w for w in words if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word]

# Example usage:
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))  # Output: ['inlets']

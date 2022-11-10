# Time: O(n) (all)
# Space: O(n)
# https://leetcode.com/problems/unique-word-abbreviation

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        """
        First we initialize two helpers, one set to track
        unique abbreviations and a dictionary to keep track
        of each word that has the same abbreviation.
        
        Then we iterate through the list, each time getting
        it's abbreviation, adding it to the set, then adding
        the word to the cooresponding dict list
        """
        
        self.abbvs = set()
        self.dict = defaultdict(list)
        
        for word in dictionary:
            abbv = self.get_abbv(word)
            self.abbvs.add(abbv)
            self.dict[abbv].append(word)

    def isUnique(self, word: str) -> bool:
        """
        First we will get the words abbreviation using the
        helper function
        
        Once we have the abbreviation, we can immediately determine
        if the word is unique or not by comparing it against our 
        set of unique abbreviations and return True if the set doesn't
        contain.
        
        If the abbreviation is present, we must then determine if the 
        word is unique by comparing it against all other words with the
        same abbreviation. If there is another word with the same abbv, 
        but isn't the same word, the word is not unique.
        """
        abbv = self.get_abbv(word)
        
        if abbv not in self.abbvs:
            return True
        
        for w in self.dict[abbv]:
            if word != w:
                return False
        
        return True
    
    def get_abbv(self, word):
        """
        Helper function to create the abbreviations per the specs
        in the challenge
        
        Takes the first letter, last letter, and the count of all
        letters in between and returns a string abbv. If the word
        is <= 2, then the word is the abbreviation. 
        """
        n = len(word)

        if n <= 2:
            return word

        f, e, l = word[0], word[-1], n - 2
        abbv = f'{f}{l}{e}'
        
        return abbv


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

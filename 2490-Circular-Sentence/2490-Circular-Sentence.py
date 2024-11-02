class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        If the sentence's first and last letter aren't equal, immediately return False. If they are, convert the string to a list using .split() 
        and loop through all but the last word. If the last letter of the word you're on doesn't match the first letter of the next word, return False. 
        If the loop finishes, return True
        """
        if sentence[0] != sentence[-1]:
            return False
        sentence = sentence.split()
        for i in range(len(sentence)-1):
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        return True

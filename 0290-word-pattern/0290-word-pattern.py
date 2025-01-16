class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        
        # Check if lengths are mismatched
        if len(pattern) != len(words):
            return False

        # Create two dictionaries for bidirectional mapping
        pattern_to_word = {}
        word_to_pattern = {}

        for char, word in zip(pattern, words):
            # Check mapping from pattern to word
            if char in pattern_to_word:
                if pattern_to_word[char] != word:
                    return False
            else:
                pattern_to_word[char] = word

            # Check mapping from word to pattern
            if word in word_to_pattern:
                if word_to_pattern[word] != char:
                    return False
            else:
                word_to_pattern[word] = char

        return True
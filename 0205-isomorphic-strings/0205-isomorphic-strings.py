class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Create mappings for s -> t and t -> s
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if the mapping is consistent in both directions
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
               (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False

            # Record the mapping
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
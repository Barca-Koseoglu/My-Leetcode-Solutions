class Solution:
    def toLowerCase(self, s: str) -> str:
        # pretty self-explanitory. Codewise you could map each uppercase to its lowercase then loop through and replace the uppercases. Or find a pattern with their ascii codes and do some math with them.
        return s.lower()

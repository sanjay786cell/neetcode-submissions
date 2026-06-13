class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_char = list(char.lower() for char in s if char.isalnum())
        if all_char == all_char[::-1]:
            return True

        return False

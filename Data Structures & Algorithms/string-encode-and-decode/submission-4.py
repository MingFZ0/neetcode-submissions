class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += string + chr(10)
        print(f"Encoded: {encoded}")
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        word = ""
        for i in range(len(s)):
            if (ord(s[i]) == 10):
                result.append(word)
                word = ""
            else:
                word += s[i]
        return result
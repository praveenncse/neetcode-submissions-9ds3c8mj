class Solution:

    def encode(self, strings: List[str]) -> str:
        encoded = ""
        for s in strings:
            encoded += f"{len(s)}:{s}"
        return encoded


    def decode(self, encoded: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(encoded):
            j = encoded.find(':', i)
            length = int(encoded[i:j])
            decoded.append(encoded[j+1:j+1+length])
            i = j + 1 + length
        return decoded


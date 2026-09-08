class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""

        for w in strs:
            str += f"{len(w)}#{w}"

        return str

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            n = int(s[i : j])
            words.append(s[j + 1 : j + 1 + n])
            i = j + 1 + n

        return words

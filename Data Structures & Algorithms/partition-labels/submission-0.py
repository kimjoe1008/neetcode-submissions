class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # for each substring you go until every instance of every letter in the substring has been covered
        # find the last index of each character
        lastI = {}
        for i, c in enumerate(s):
            lastI[c] = i
        
        output = []
        # substring is the length of the current substring
        # end is the length that the current substring must reach
        # end gets updated whenever we find a new character within the current substring
        substring = end = 0
        for i, c in enumerate(s):
            substring += 1
            # update end if new char appears after anything in current substring
            end = max(end, lastI[c])
            if i == end:
                output.append(substring)
                substring = 0
        return output
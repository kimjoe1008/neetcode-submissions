class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        # sort intervals based on starts
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            # if the start of the interval is <= end of previous interval
            if stack and start <= stack[-1][1]:
                ns, ne = stack.pop()
                ns = min(ns, start)
                ne = max(ne, end)
                stack.append([ns, ne])
            else:
                stack.append([start, end])
        return stack
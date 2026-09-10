# Last updated: 9/10/2026, 7:52:08 PM
1class Solution:
2    def bestClosingTime(self, customers: str) -> int:
3        score = 0
4        max_score = 0
5        output = 0
6
7        for i in range(len(customers)):
8            if customers[i] == 'Y':
9                score += 1
10            elif customers[i] == 'N':
11                score -= 1
12
13            if score > max_score:
14                max_score = score
15                output = i + 1
16        return output
17
18        
19
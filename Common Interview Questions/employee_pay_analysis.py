'''
Employee Pay Analysis

You are building a tool that analyzes employee salaries at a company.

Implement a function that receives a list of employee salaries and returns the second highest unique salary.

Function
getSecondHighestSalary(salaries)
Requirements
salaries is a list of integers.
Return the second highest distinct salary.
If there are fewer than two distinct salaries, return -1.
Salaries may appear multiple times.
Examples
Input:  [4000, 3000, 5000, 3000]
Output: 4000
Input:  [1000, 2000, 3000]
Output: 2000
Input:  [5000, 5000, 5000]
Output: -1
Input:  [7000, 4000, 7000, 6000, 6000]
Output: 6000
Constraints
1 <= len(salaries) <= 100,000
-10^9 <= salaries[i] <= 10^9
'''

def getSecondHighestSalary(salaries):
    if len(salaries) >2:
        sorted_salaries = sorted(list(set(salaries)))
        return sorted_salaries[-2]
    else:
        return -1


# Example
salaries = [7000, 4000, 7000, 6000, 6000]

print(getSecondHighestSalary(salaries))
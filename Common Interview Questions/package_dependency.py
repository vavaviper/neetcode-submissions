'''
Package Dependency Checker

You're building a system that installs software packages. A package can depend on other packages, and all dependencies must eventually be installed.

You are given a dictionary where each package maps to a list of packages it depends on.

Implement:

hasDependencyCycle(dependencies)

Return True if the dependency structure contains a cycle, otherwise return False.

Example 1
{
    "A": ["B"],
    "B": ["C"],
    "C": []
}

Expected:

False

Because:

A → B → C
Example 2
{
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

Expected:

True

Because:

A → B → C
↑         ↓
└─────────┘
Example 3
{
    "A": ["C"],
    "B": ["C"],
    "C": []
}

Expected:

False

Both A and B depend on C, but there isn't a cycle.

Example 4
{
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

Expected:

False
Example 5
{
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": ["B"]
}

Expected:

True
'''

def hasDependencyCycle(dependencies):
    current_path = set()
    visited = set()

    def dfs(node):
        if node in visited:
            return False
        if node in current_path:
            return True
        current_path.add(node)
        for i in dependencies[node]:
            if dfs(i):
                return True
        current_path.remove(node)
        visited.add(node)
        return False
    for i in dependencies:
        if dfs(i):
            return True
    return False


dependencies = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}  
print(hasDependencyCycle(dependencies))
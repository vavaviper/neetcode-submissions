'''
Website Redirect Loop

You are given a dictionary where each website redirects to at most one other website.

For example:

redirects = {
    "google.com": "youtube.com",
    "youtube.com": "reddit.com",
    "reddit.com": "google.com"
}

This creates:

google.com
    ↓
youtube.com
    ↓
reddit.com
    ↓
google.com  ← loop!

Implement:

hasRedirectLoop(redirects)

Return:

True if there is a redirect loop
False if every redirect chain eventually ends
Example 1
redirects = {
    "google.com": "youtube.com",
    "youtube.com": "reddit.com"
}

Return:

False

Because:

google → youtube → reddit → STOP
Example 2
redirects = {
    "google.com": "youtube.com",
    "youtube.com": "reddit.com",
    "reddit.com": "google.com"
}


Return:

True

Because:

google → youtube → reddit → google
Example 3

Here's the one I really want you to think about:

redirects = {
    "google.com": "reddit.com",
    "youtube.com": "reddit.com"
}

Return:

False

Because:

google ──→ reddit
youtube ─→ reddit

There is no loop, even though you could encounter reddit.com more than once.
'''

def hasRedirects(redirects):
    visited = set()
    current_path = set()

    def dfs(node):
        if node in current_path:
            return True

        if node in visited:
            return False

        current_path.add(node)

        if node not in redirects:
            return False

        if dfs(redirects[node]):
            return True

        current_path.remove(node)
        visited.add(node)

        return False

    for node in redirects:
            if dfs(node):
                return True

    return False


# 1. Simple chain, no loop
print(hasRedirects({
    "A": "B",
    "B": "C"
}))
# Expected: False

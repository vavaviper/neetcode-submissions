'''
User Roles / Permissions Validation

You are given a set of users, roles, and permissions for a system.

Each user can have one or more roles. Each role defines which actions the user is allowed to perform on specific resources.

Your task is to determine whether a given user is authorized to perform a specific action on a resource.

Function

Implement:

is_authorized(users, roles, user_id, action, resource)

The function should return True if the user has permission to perform the given action on the resource, and False otherwise.

Input
users: a dictionary mapping each user_id to a list of roles.
roles: a dictionary mapping each role to the actions and resources it is allowed to access.
user_id: the user requesting access.
action: the action being requested, such as "read", "write", or "delete".
resource: the resource being accessed, such as "document", "database", or "user_profile".

Each role's permissions are represented as a list of (action, resource) pairs.

Example
users = {
    "alice": ["admin"],
    "bob": ["editor"],
    "charlie": ["viewer"]
}

roles = {
    "admin": [
        ("read", "document"),
        ("write", "document"),
        ("delete", "document")
    ],
    "editor": [
        ("read", "document"),
        ("write", "document")
    ],
    "viewer": [
        ("read", "document")
    ]
}

For the following requests:

is_authorized(users, roles, "alice", "delete", "document")
# True

is_authorized(users, roles, "bob", "delete", "document")
# False

is_authorized(users, roles, "charlie", "read", "document")
# True

is_authorized(users, roles, "charlie", "write", "document")
# False
Requirements

Your implementation should:

Return True if any of the user's roles grants the requested permission.
Return False if none of the user's roles grants the permission.
Handle users with multiple roles.
Handle unknown users and roles gracefully.
Follow-up 1: Role Inheritance

Roles can inherit permissions from other roles.

For example:

admin
  ↓
editor
  ↓
viewer

An admin automatically receives all permissions granted to editor, and an editor receives all permissions granted to viewer.

Modify your solution to support role inheritance.

Follow-up 2: Resource-Level Overrides

Permissions can now apply to specific resources.

For example:

("read", "document:123")

should grant access to document 123, but not to other documents.

A wildcard resource:

("read", "document:*")

should grant access to all documents.

Modify your solution to determine whether a requested resource matches a user's permissions.

Follow-up 3: Explicit Deny

Permissions can now explicitly deny access:

("deny", "delete", "document")

If a user has both:

("allow", "delete", "document")
("deny", "delete", "document")

the request should be denied.

Question: How would you modify your data structures and authorization logic to handle this efficiently?
'''


def is_authorized(users, roles, user_id, action, resource):
    hierachy = ['admin', 'editor', 'viewer']
    if user_id in users:
        if len(users[user_id]) > 1:
            set_users = set(users[user_id])
            for h in hierachy:
                if h in set_users:
                    perm = h
                    break
        elif len(users[user_id]) == 1:    
            perm = users[user_id][0]
        else:
            return "user has no roles"
    else:
        return "user not found"
    if perm in roles:
        for action1, resource1 in roles[perm]:
            if action == action1 and resource1 == resource:
                return True
        return False
    else:
        return "role not found"




users = {
    "alice": ["admin"],
    "bob": ["editor"],
    "charlie": ["viewer"]
}

roles = {
    "admin": [
        ("read", "document"),
        ("write", "document"),
        ("delete", "document")
    ],
    "editor": [
        ("read", "document"),
        ("write", "document")
    ],
    "viewer": [
        ("read", "document")
    ]
}

print(is_authorized(users, roles, "alice", "delete", "document"))
print(is_authorized(users, roles, "bob", "delete", "document"))
print(is_authorized(users, roles, "charlie", "read", "document"))
print(is_authorized(users, roles, "charlie", "write", "document"))




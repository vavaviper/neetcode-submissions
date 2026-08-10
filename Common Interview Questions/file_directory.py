'''
File Directory

You are building a simple in-memory file directory system.

Each directory can contain files and other directories. Every file and directory has a unique name within its parent directory.

Implement a FileDirectory class that supports the following operations:

createDirectory(path)

Creates a new directory at the specified path.

createFile(path)

Creates a new file at the specified path.

list(path)

Returns the names of all files and directories directly inside the specified directory.

delete(path)

Deletes the file or directory at the specified path. A directory can only be deleted if it is empty.

Example

Starting with an empty directory:

/

After:

createDirectory("/documents")
createDirectory("/documents/school")
createFile("/documents/resume.txt")
createFile("/documents/school/notes.txt")

The directory structure should be:

/
└── documents/
    ├── resume.txt
    └── school/
        └── notes.txt

Calling:

list("/documents")

should return:

["resume.txt", "school"]
Assumptions
The root directory / always exists.
Paths always begin with /.
Names do not contain /.
You should raise an error if attempting to create something that already exists.
You should raise an error if the parent directory doesn't exist.
You should raise an error when attempting to delete a non-empty directory.

Implement the FileDirectory class.

Your solution should explain the data structure you choose and the time complexity of each operation.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isFile = False  
        self.isDirectory = False

class FileDirectory:
    def __init__(self):
        self.root = TrieNode()

    def createDirectory(self, path):
        # if this is the first folder
        if self.root == None:
            curr = TrieNode[path[1]]
            self.root.children[path[0]] = curr
            self.add(curr, 1)

        # if its a later on folder   
        elif self.root != None:
            location = self.root.children
            i = 0
            i = self.check_similar(location, i, path)
            if self.path[i+1]:
                curr = self.add(location, i+1)
                curr.isDirectory = True


    def createFile(self, path):
        location, i = self.check_similar(path, 0)
        curr = self.add(location, i)
        curr.isFile = True


    def listResources(self, path):
        location, i = self.check_similar(path, 0)
        return location.children.values()

    def delete(self, path):
        location, i = self.check_similar

    ## recursion functions to make things easier
    def check_similar(self, location, i, path):
        while self.path[i] in location:
            location = location.children[self.path[i]]
            i += 1
        return location, i-1

    def add(self, root, i, path):
        if not path[i + 1]:
            return curr
        curr = TrieNode[self.path[i+1]]
        root.children[self.path[i]] = curr
        self.add(curr, i + 1)

test = FileDirectory()
test.createDirectory("/documents")
test.createDirectory("/documents/school")
test.createFile("/documents/resume.txt")
test.createFile("/documents/school/notes.txt")
print(test.listResources("/documents"))
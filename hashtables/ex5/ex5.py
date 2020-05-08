class FileNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def insert_after(self, node):
        self.next = node

class FileList:
    def __init__(self, head=None):
        self.head = head
    
    def insert(self, value):
        if self.head is None:
            self.head = FileNode(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.insert_after(FileNode(value))
    
    def for_each(self, cb):
        current_node = self.head
        while current_node is not None:
            cb(current_node.value)
            current_node = current_node.next

def finder(files, queries):
    cache = {}
    result = []

    for file in files:
        filename = file.split('/')[-1]
        if filename not in cache:
            cache[filename] = FileList(FileNode(file))
        else:
            cache[filename].insert(file)

    for query in queries:
        if query in cache:
            cache[query].for_each(result.append)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

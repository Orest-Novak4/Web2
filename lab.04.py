class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def add_folder(self, name):
        self.children.setdefault(name, Folder(name, self))

    def add_file(self, name, size):
        self.files[name] = size

    def get_size(self):
        return sum(self.files.values()) + sum(child.get_size() for child in self.children.values())

def parse_commands(commands):
    root = Folder('/')
    current = root
    
    for cmd in commands:
        parts = cmd.strip().split()
        if parts[0] == '$' and parts[1] == 'cd':
            current = root if parts[2] == '/' else current.parent if parts[2] == '..' else current.children.setdefault(parts[2], Folder(parts[2], current))
        elif parts[0] == 'dir':
            current.add_folder(parts[1])
        elif parts[0] != '$':
            current.add_file(parts[1], int(parts[0]))
    
    return root

def find_small_folders(root, limit=100000):
    return sum(folder.get_size() for folder in traverse(root) if folder.get_size() <= limit)

def traverse(folder):
    yield folder
    for child in folder.children.values():
        yield from traverse(child)

with open('input_4.txt') as file:
    root_folder = parse_commands(file.readlines())

print("Сума розмірів директорій, які не перевищують 100000:", find_small_folders(root_folder))
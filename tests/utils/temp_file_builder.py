# This is a diy file system only for enthusiasts
# You can create an entire file system out of it.
# Use doubly LinkedList to move forward and backward through the file system

class TempFileBuilder:
    def __init__(self, tmpdir_factory, root_dir: str):
        self._factory = tmpdir_factory
        self._root = tmpdir_factory.mktemp(root_dir)
        self._curr = self._root
        self._parent_stack = []
        self._file = None

    def create_child_dir(self, dir_name: str):
        self._parent_stack.append(self._curr)
        self._curr = self._curr.mkdir(dir_name)
        return self

    def go_to_parent(self):
        if not self._parent_stack:
            raise ValueError("Already at root directory")
        self._curr = self._parent_stack.pop()
        return self

    def go_to_root(self):
        self._parent_stack.clear()
        self._curr = self._root
        return self

    def create_file(self, file_name: str):
        self._file = self._curr.join(file_name)
        return self

    def set_file_content(self, content: str):
        if not self._file:
            raise ValueError("File not created")
        self._file.write(content)
        return self

    @property
    def root(self):
        return self._root

    @property
    def file(self):
        return self._file

    @property
    def current(self):
        return self._curr

    @property
    def parent(self):
        return self._parent_stack[-1] if self._parent_stack else None

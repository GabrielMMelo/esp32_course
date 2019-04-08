class Loader:

    def __init__(self, pkg, dir):
        if dir == ".":
            dir = ""
        else:
            dir = dir.replace("/", ".") + "."
        if pkg and pkg != "__main__":
            dir = pkg + "." + dir
        #self.p = dir
        self.p = "templates."

    def load(self, name):
        name = name.replace(".", "_")
        #return __import__(self.p + name, None, None, (name,)).render
        return __import__(self.p + name, None, None, (name,)).render

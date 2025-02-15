from pathlib import Path



class Site():
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest + '/' + path.relative_to(self.source)
        directory.mkdir(partents=True, exist_ok=True)


    def build(self):
        pass
        #self.dest.mkdir(partents=True, exist_ok=True)

# Data storage management

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as f:
            f.write(data)

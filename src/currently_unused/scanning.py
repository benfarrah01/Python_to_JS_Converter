class scanner:
    def __init__(self, python_text):
        self.python_text = python_text
        self.lines = []
    
    def scan(self):
        for line in self.python_text:
            self.lines.append(line)
        self.parse(self.lines)
    
    def parse(self):
        
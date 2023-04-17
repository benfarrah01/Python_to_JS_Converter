class scanner:
    def __init__(self, python_text):
        self.python_text = input
    
    def scan(self):
        for line in self.python_text.splitlines():
            print(line)
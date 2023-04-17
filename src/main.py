import sys
import scanning
from pathlib import Path

def main():
    python_file = sys.argv[1]
    python_path = Path(python_file)
    if python_path.is_file():
        python_text = python_path.read_text().splitlines()
        #print(python_text)
        my_scanner = scanning.scanner(python_text)
        my_scanner.scan()
        

if __name__ == "__main__":
    main()
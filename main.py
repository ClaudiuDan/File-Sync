import sys
from args_validator import validate

def main(argv):
    print(argv)

if __name__ == "__main__":
    if validate(sys.argv):
        print("good input")
    
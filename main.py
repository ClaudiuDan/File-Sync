import sys
from args_validator import validate
from synchronizer import synchronize


def main(argv):
    print(argv)


if __name__ == "__main__":
    if validate(sys.argv):
        print("good input")
        synchronize(sys.argv[1], sys.argv[2], sys.argv[3])

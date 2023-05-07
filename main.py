import sys
from args_validator import validate
from synchronizer import synchronize_periodically
from logger import Logger


def main(argv):
    print(argv)


if __name__ == "__main__":
    if validate(sys.argv):
        print("good input")
        logger = Logger(sys.argv[4])
        synchronize_periodically(sys.argv[1], sys.argv[2], sys.argv[3], logger)

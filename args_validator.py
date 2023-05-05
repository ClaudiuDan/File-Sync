import os.path


def __validate_file_types(source, copy, log):
    return os.path.isdir(source) and os.path.isdir(copy) and os.path.isfile(log)


def __validate_paths(paths):
    for path in paths:
        if not os.path.exists(path):
            print("Invalid folder path %s" % path)
            return False
    return True


def __validate_interval(time):
    if time.replace(".", "", 1).isnumeric():
        return True
    print("Insert a number type interval, e.g. 50")
    return False


def validate(argv):
    if len(argv) >= 2 and argv[1] == "--help":
        print(
            "usage: python main.py <source_path> <sync_path> <interval_as_seconds> <log_path>"
        )
        return False

    if len(argv) < 5:
        print("Insufficient arguments provided, check with --help")
        return False

    source = argv[1]
    copy = argv[2]
    log = argv[4]
    return (
        __validate_paths([source, copy, log])
        and __validate_interval(argv[3])
        and __validate_file_types(source, copy, log)
    )

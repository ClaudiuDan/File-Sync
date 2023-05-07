import os
import os.path
import shutil
import time
from logger import Logger
from typing import Callable


def __copy(navigation_folder: str, folder: str, is_dir: bool, logger: Logger) -> None:
    if is_dir:
        if not os.path.exists(folder):
            # not logging anything since it is a directory
            os.mkdir(folder)
        return
    shutil.copy(navigation_folder, folder)
    logger.log("copied %s to %s" % (navigation_folder, folder))


def __remove(navigation: str, reference: str, is_dir: bool, logger: Logger) -> None:
    if os.path.exists(reference):
        return
    if is_dir:
        os.rmdir(navigation)
        return
    os.remove(navigation)
    logger.log("deleted %s" % (navigation))


# Applies a given operation to the pair of given folders, by navigating one of the
# folders either topdown or bottomup
def __apply_op(
    navigation_folder: str, folder: str, op: Callable, topdown: bool, logger: Logger
) -> None:
    for navigation_root, dirs, files in os.walk(navigation_folder, topdown=topdown):
        folder_root = navigation_root.replace(navigation_folder, folder, 1)
        [
            op(navigation_root + "/" + dir, folder_root + "/" + dir, True, logger)
            for dir in dirs
        ]
        [
            op(navigation_root + "/" + file, folder_root + "/" + file, False, logger)
            for file in files
        ]


def __synchronize(source: str, replica: str, logger: Logger) -> None:
    __apply_op(source, replica, __copy, True, logger)
    __apply_op(replica, source, __remove, False, logger)


def __fix_folder_name(folder: str) -> str:
    if folder[-1] == "/":
        return folder[:-1]
    return folder


def synchronize_periodically(
    source: str, replica: str, interval: int | float, logger: Logger
) -> None:
    logger = logger
    source = __fix_folder_name(source)
    replica = __fix_folder_name(replica)

    while True:
        __synchronize(source, replica, logger)
        time.sleep(float(interval))

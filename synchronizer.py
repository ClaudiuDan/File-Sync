import os
import os.path
import shutil
import time
from logger import Logger
from typing import Callable


def __copy(navigation: str, reference: str, logger: Logger) -> None:
    print(navigation, reference)
    if (
        os.path.isdir(navigation)
        and len(os.listdir(navigation)) == 0
        and not os.path.exists(reference)
    ):
        os.mkdir(reference)
    if os.path.isfile(navigation):
        shutil.copyfile(navigation, reference)
        logger.log("copy file from %s to %s" % (navigation, reference))


def __remove(navigation: str, reference: str, logger: Logger) -> None:
    if os.path.exists(reference):
        return
    if os.path.isdir(navigation) and len(os.listdir(navigation)) == 0:
        os.rmdir(navigation)
    if os.path.isfile(navigation):
        os.remove(navigation)
        logger.log("Remove file at %s" % navigation)


def __go_through_folder(
    navigation_folder: str, reference_folder: str, operation: Callable, logger: Logger
) -> None:
    for filename in os.listdir(navigation_folder):
        new_navigation_path = navigation_folder + "/" + filename
        new_reference_path = reference_folder + "/" + filename
        if os.path.isdir(new_navigation_path):
            __go_through_folder(
                new_navigation_path, new_reference_path, operation, logger
            )
        operation(new_navigation_path, new_reference_path, logger)


def __synchronize(source: str, replica: str, logger: Logger) -> None:
    __go_through_folder(source, replica, __copy, logger)
    __go_through_folder(replica, source, __remove, logger)


def synchronize_periodically(
    source: str, replica: str, interval: int | float, logger: Logger
) -> None:
    logger = logger
    while True:
        __synchronize(source, replica, logger)
        time.sleep(float(interval))

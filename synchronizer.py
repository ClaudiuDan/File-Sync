import os
import os.path
import shutil
import time


def __copy(navigation, reference):
    if (
        os.path.isdir(navigation)
        and len(os.listdir(navigation)) == 0
        and not os.path.exists(reference)
    ):
        print("making directory")
        os.mkdir(reference)
    if os.path.isfile(navigation):
        shutil.copyfile(navigation, reference)
        print("copy file from %s to %s" % (navigation, reference))


def __remove(navigation, reference):
    print("in remove")
    if os.path.exists(reference):
        return
    print("not exists")
    if os.path.isdir(navigation) and len(os.listdir(navigation)) == 0:
        print("remove dir")
        os.rmdir(navigation)
    if os.path.isfile(navigation):
        os.remove(navigation)
        print("Remove file at %s" % navigation)


def __go_through_folder(navigation_folder, reference_folder, operation):
    for filename in os.listdir(navigation_folder):
        new_navigation_path = navigation_folder + "/" + filename
        new_reference_path = reference_folder + "/" + filename
        print(new_navigation_path, new_reference_path)
        if os.path.isdir(new_navigation_path):
            __go_through_folder(new_navigation_path, new_reference_path, operation)
        operation(new_navigation_path, new_reference_path)


def synchronize(source, replica, interval):
    while True:
        __go_through_folder(source, replica, __copy)
        __go_through_folder(replica, source, __remove)
        time.sleep(float(interval))

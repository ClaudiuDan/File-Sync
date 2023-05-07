from synchronizer import __synchronize
import os
import pytest
from logger import Logger

testing_base = "testing"
folder_source = testing_base + "/test_folder_source"
folder_replica = testing_base + "/test_folder_replica"
file = folder_source + "/test_file"
replica_file = folder_replica + "/test_file"
log_file = testing_base + "/log_file"


@pytest.fixture
def setup():
    os.mkdir(testing_base)
    os.mkdir(folder_source)
    os.mkdir(folder_replica)
    open(file, "w")
    open(log_file, "w")
    yield
    if os.path.exists(file):
        os.remove(file)
    if os.path.exists(replica_file):
        os.remove(replica_file)
    os.remove(log_file)
    os.rmdir(folder_source)
    os.rmdir(folder_replica)
    os.rmdir(testing_base)


def test_synchronize_basic_test_passes(setup):
    logger = Logger(log_file)
    __synchronize(folder_source, folder_replica, logger)
    assert os.path.exists(file)


def test_synchronize_file_removal_passes(setup):
    logger = Logger(log_file)
    __synchronize(folder_source, folder_replica, logger)
    os.remove(file)
    __synchronize(folder_source, folder_replica, logger)
    assert not os.path.exists(file)

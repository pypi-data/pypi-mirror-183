import sys, os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bulkhead.utils.file_utils import (
    make_full_filename,
    check_make_dir
)



def test_make_full_name():
    def make_name(prefix, file_name, expectation):
        new_file_name = make_full_filename(prefix=prefix, file_name=file_name)
        assert new_file_name == expectation, (
            str(prefix)
            + " old file_name "
            + str(file_name)
            + " returned file_name "
            + str(new_file_name)
        )

    # case 1
    prefix = "tests"
    file_name = "testfile.png"
    expectation = "tests/testfile.png"
    make_name(prefix, file_name, expectation)
    # case 2
    prefix = None
    file_name = "tests/testfile.png"
    expectation = "tests/testfile.png"
    make_name(prefix, file_name, expectation)
    # case 3
    prefix = "tests/"
    file_name = "/testfile.png"
    expectation = "tests/testfile.png"
    make_name(prefix, file_name, expectation)
    # case 3
    prefix = "tests"
    file_name = "/testfile.png"
    expectation = "tests/testfile.png"
    make_name(prefix, file_name, expectation)
    # case 4
    prefix = "tests/data"
    file_name = "testfile.png"
    expectation = "tests/data/testfile.png"
    make_name(prefix, file_name, expectation)

def test_check_make_dir(): 

    test_dir = "tests/test_utils"
    test_folder = "test_utils"
    check_make_dir(test_dir)
    dirs = os.listdir("tests/")
    assert test_folder in dirs 
    check_make_dir(test_dir)
    os.rmdir(test_dir)
    dirs = os.listdir("tests/")
    assert test_folder not in dirs

    

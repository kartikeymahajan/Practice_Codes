"""Using Pytest"""

import pytest
import subprocess
import os


def test_check_is_directoty_and_files_created():

    '''Checking the created files in our new created directory.'''

    # create a new directory in our current directory
    subprocess.run(['mkdir', 'myfiles'], check=True) #subprocess.CalledProcessError if non zero code
    
    # change the directory
    os.chdir("myfiles")

    # create multiple files using touch command
    subprocess.run(['touch', 'file1', 'file2', 'file3'], check=True)

    # store ls output in output variable
    output = subprocess.check_output(['ls'])

    # Expected output after creating files
    expected_output = b'file1\nfile2\nfile3\n'

    # Checking the output with expected output
    assert output == expected_output


def test_to_delete_created_directory():

    # Going to our specific directory
    os.chdir(r"F:\Kartikeya\Git\monday_task")
    
    # We are removing myfiles directory using rm -r command
    subprocess.run(['rm', '-r', 'myfiles'], check=True)
    
        # store ls output in output variable
    output = subprocess.check_output(['ls'])

    # Expected output after deleting files.
    expected_output = b'__pycache__\ncreate_files.sh\nselenium\ntest_file.py\ntesting_using_pytest.py\n' 

    # Checking output with expected output.
    assert output == expected_output
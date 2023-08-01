"""Using Unittest"""

import unittest
import subprocess
import os

class Test(unittest.TestCase):

    def test_check_is_directoty_and_files_created(self):

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
        self.assertEqual(output, expected_output)


    def test_to_delete_created_directory(self):

        '''Deleting the created directory and files. That means when we again run this script it will not
        show error(directory and fils is allready exits). '''

        # Going to our specific directory
        os.chdir(r"F:\Kartikeya\Git\monday_task")
        
        # We are removing myfiles directory using rm -r command
        subprocess.run(['rm', '-r', 'myfiles'], check=True)
        
         # store ls output in output variable
        output = subprocess.check_output(['ls'])

        # Expected output after deleting files.
        expected_output = b'__pycache__\ncreate_files.sh\nselenium\ntest_file.py\ntesting_using_pytest.py\n' 

        # Checking output with expected output.
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()

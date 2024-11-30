import file_utils_operations_lib
import unittest
import os

# Variable
from custom_files import path, custom_path, custom_path_delim, path_delim, delimiter, create_delim_test_file
# Functions
from custom_files import get_list, create_regex_test_file

def get_list(string: str) -> list:
    res: list = string.split("\n")
    if len(res) == 1 and res[0] == '':
        return []
    elif len(res) > 1 and res[-1] == '':
        res.pop()
    return res 

class TestWithCustomDelimCountLines(unittest.TestCase):
    def test_basic(self):
        file = os.popen("cat " + path)
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim,delimiter=delimiter), len(ref))
    
    def test_remove_empty_lines(self):
        file = os.popen("sed '/^$/d' " + path)
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim, delimiter=delimiter, remove_empty_string=True), len(ref))
    
    def test_keep_regex(self):
        file = os.popen("grep \"^La loi\" " + path)
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim, delimiter=delimiter, remove_empty_string=False, regex_keep=["^La loi"]), len(ref))
    
    def test_remove_empty_lines_keep_regex(self):
        file = os.popen("sed '/^$/d' " + path + " | grep \"^La loi\" ")
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim, delimiter=delimiter, remove_empty_string=True, regex_keep=["^La loi"]), len(ref))
    
    def test_pass_regex(self):
        file = os.popen("grep -v \"^La loi\" " + path)
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim, delimiter=delimiter, remove_empty_string=False, regex_pass=["^La loi"]), len(ref))

    def test_remove_empty_lines_pass_regex(self):
        file = os.popen("sed '/^$/d' " + path + " | grep -v \"^La loi\" ")
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_utils_operations_lib.WithCustomDelims.count_lines(path=path_delim, delimiter=delimiter, remove_empty_string=True, regex_pass=["^La loi"]), len(ref))

if __name__ == '__main__':
    create_delim_test_file(path, path_delim)
    create_regex_test_file(custom_path)
    create_delim_test_file(custom_path, custom_path_delim)
    unittest.main()
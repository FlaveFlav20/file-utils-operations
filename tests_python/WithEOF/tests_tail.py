import file_operations_lib
import unittest
import os

from custom_files import create_regex_test_file, headers

path: str = "./tests_files/DDHC.txt"
custom_path: str = "./tests_files/custom.txt"

if __name__ == '__main__':
    create_regex_test_file(custom_path)

def get_list(string: str) -> list:
    res: list = string.split("\n")
    if len(res) == 1 and res[0] == '':
        return []
    elif len(res) > 1 and res[-1] == '':
        res.pop()
    return res 

class TestWithEOFTail(unittest.TestCase):
    def test_tail_n_10_valid_remove_empty_string_false(self):
        n: int = 10
        file = os.popen("tail " + path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n), ref)

    def test_tail_n_0_valid_remove_empty_string_false(self):
        n: int = 0
        file = os.popen("tail " + path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n), ref)

    def test_tail_n_1_valid_remove_empty_string_false(self):
        n: int = 1
        file = os.popen("tail " + path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n), ref)

    def test_tail_n_neg_invalid_remove_empty_string_false(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=path, n=n)
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Negative value shouldn't work")

## 

    def test_custom_path_tail_n_10_valid_remove_empty_string_false(self):
        n: int = 10
        file = os.popen("tail " + custom_path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n), ref)

    def test_custom_path_tail_n_0_valid_remove_empty_string_false(self):
        n: int = 0
        file = os.popen("tail " + custom_path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n), ref)

    def test_custom_path_tail_n_1_valid_remove_empty_string_false(self):
        n: int = 1
        file = os.popen("tail " + custom_path + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n), ref)

    def test_custom_path_tail_n_neg_invalid_remove_empty_string_false(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=custom_path, n=n)
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Negative value shouldn't work")

## Test empty lines ----------

    def test_tail_n_10_valid_remove_empty_string_true(self):
        n: int = 10
        file = os.popen("sed '/^$/d' " + path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True, restrict=False), ref)

    def test_tail_n_0_valid_remove_empty_string_true(self):
        n: int = 0
        file = os.popen("sed '/^$/d' " + path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True), ref)

    def test_tail_n_1_valid_remove_empty_string_true(self):
        n: int = 1
        file = os.popen("sed '/^$/d' " + path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True), ref)

    def test_tail_n_neg_invalid_remove_empty_string_true(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True)
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Negative value shouldn't work")

## 

    def test_custom_path_tail_n_10_valid_remove_empty_string_true(self):
        n: int = 10
        file = os.popen("sed '/^$/d' " + custom_path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n, remove_empty_string=True), ref)

    def test_custom_path_tail_n_0_valid_remove_empty_string_true(self):
        n: int = 0
        file = os.popen("sed '/^$/d' " + custom_path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n, remove_empty_string=True), ref)

    def test_custom_path_tail_n_1_valid_remove_empty_string_true(self):
        n: int = 1
        file = os.popen("sed '/^$/d' " + custom_path + " | tail " + " -n " + str(n))
        res: str= file.read()
        file.close()
        ref: list = get_list(res)
        self.assertEqual(file_operations_lib.WithEOL.tail(file=custom_path, n=n, remove_empty_string=True), ref)

    def test_custom_path_tail_n_neg_invalid_remove_empty_string_true(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=custom_path, n=n, remove_empty_string=True)
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Negative value shouldn't work")

## Test regex

    def test_tail_n_valid_invalid_remove_empty_string_false_keep_when_regex_invalid(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True, regex_keep="Haha")
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Non bool value shouldn't work")

    def test_tail_n_valid_invalid_remove_empty_string_false_keep_when_regex_valid_pass_when_regex_invalid(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True, regex_pass="Haha")
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Non bool value shouldn't work")
        
    def test_tail_n_valid_invalid_remove_empty_string_false_keep_when_regex_valid_pass_when_regex_valid_regex_invalid(self):
        check_pass: bool = True 
        try:
            file_operations_lib.WithEOL.tail(file=path, n=n, remove_empty_string=True, regex=1)
        except:
            check_pass = False
        if check_pass:
            self.fail("[tail] Non bool value shouldn't work")

    def test_tail_n_10_invalid_remove_empty_string_false_keep_when_regex_valid_pass_when_regex_valid_regex_Warning(self):
        n: int = 10
        global headers
        result_to_test: list = file_operations_lib.WithEOL.tail(file=custom_path, n=n, regex_keep=["\[Warning\]:.*"], restrict=True)

        self.assertEqual(len(result_to_test), n // len(headers) + 1)

    def test_tail_n_10_invalid_remove_empty_string_false_keep_when_regex_valid_pass_when_regex_valid_regex_Info(self):
        n: int = 10
        global headers
        result_to_test: list = file_operations_lib.WithEOL.tail(file=custom_path, n=n, regex_keep=["\[Info\]:.*"], restrict=True)

        self.assertEqual(len(result_to_test), n // len(headers) + 1)

    def test_tail_n_10_invalid_remove_empty_string_false_keep_when_regex_valid_pass_when_regex_valid_regex_Error(self):
        n: int = 10
        global headers
        result_to_test: list = file_operations_lib.WithEOL.tail(file=custom_path, n=n, regex_keep=["\[Error\]:.*"], restrict=True)

        self.assertEqual(len(result_to_test), n // len(headers))



if __name__ == '__main__':
    unittest.main()
import unittest
import os
from utils.file_reader import read_file


class TestFileReader(unittest.TestCase):

    def setUp(self):
        # 创建测试文件
        self.test_file = "test_file.txt"
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("这是一个测试文件内容。")

    def tearDown(self):
        # 清理测试文件
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_existing_file(self):
        content = read_file(self.test_file)
        self.assertEqual(content, "这是一个测试文件内容。")

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent.txt")

    def test_read_empty_file(self):
        empty_file = "empty_test.txt"
        with open(empty_file, 'w', encoding='utf-8') as f:
            f.write("")

        with self.assertRaises(ValueError):
            read_file(empty_file)

        os.remove(empty_file)


if __name__ == '__main__':
    unittest.main()

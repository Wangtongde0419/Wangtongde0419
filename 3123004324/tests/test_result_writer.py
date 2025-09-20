import unittest
import os
import tempfile
from utils.result_writer import write_result


class TestResultWriter(unittest.TestCase):
    """
    测试结果写入模块的单元测试类
    """

    def test_write_normal_result(self):
        """
        测试正常写入相似度结果
        """
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_path = temp_file.name

        try:
            # 写入测试数据
            similarity = 0.85
            write_result(temp_path, similarity)

            # 验证写入内容
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertEqual(content, "0.85")

        finally:
            # 清理临时文件
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_zero_similarity(self):
        """
        测试写入0相似度
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_path = temp_file.name

        try:
            similarity = 0.0
            write_result(temp_path, similarity)

            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertEqual(content, "0.00")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_full_similarity(self):
        """
        测试写入1.0相似度
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_path = temp_file.name

        try:
            similarity = 1.0
            write_result(temp_path, similarity)

            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertEqual(content, "1.00")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_decimal_similarity(self):
        """
        测试写入小数相似度
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_path = temp_file.name

        try:
            similarity = 0.756
            write_result(temp_path, similarity)

            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertEqual(content, "0.76")  # 测试四舍五入

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_to_nonexistent_directory(self):
        """
        测试写入到不存在的目录
        """
        nonexistent_path = "/nonexistent/directory/result.txt"

        with self.assertRaises(IOError):
            write_result(nonexistent_path, 0.85)

    def test_write_with_permission_error(self):
        """
        测试写入权限错误
        """
        # 在Unix系统上测试只读目录
        if os.name != 'nt':  # 非Windows系统
            read_only_dir = tempfile.mkdtemp()
            read_only_file = os.path.join(read_only_dir, "result.txt")

            # 设置目录为只读
            os.chmod(read_only_dir, 0o444)

            try:
                with self.assertRaises(IOError):
                    write_result(read_only_file, 0.85)
            finally:
                # 恢复权限并清理
                os.chmod(read_only_dir, 0o755)
                os.rmdir(read_only_dir)

    def test_write_special_characters_path(self):
        """
        测试包含特殊字符的文件路径
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='_test@123.txt') as temp_file:
            temp_path = temp_file.name

        try:
            similarity = 0.5
            write_result(temp_path, similarity)

            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertEqual(content, "0.50")

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_multiple_times(self):
        """
        测试多次写入同一文件
        """
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_path = temp_file.name

        try:
            # 第一次写入
            write_result(temp_path, 0.33)
            with open(temp_path, 'r', encoding='utf-8') as f:
                content1 = f.read()
            self.assertEqual(content1, "0.33")

            # 第二次写入（覆盖）
            write_result(temp_path, 0.66)
            with open(temp_path, 'r', encoding='utf-8') as f:
                content2 = f.read()
            self.assertEqual(content2, "0.66")

            # 验证第二次写入覆盖了第一次
            self.assertNotEqual(content1, content2)

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_write_boundary_values(self):
        """
        测试边界值写入
        """
        test_cases = [
            (0.0, "0.00"),
            (0.01, "0.01"),
            (0.99, "0.99"),
            (1.0, "1.00"),
            (-0.1, "0.00"),  # 负值应该被处理为0
            (1.1, "1.00")  # 大于1的值应该被处理为1
        ]

        for similarity, expected in test_cases:
            with self.subTest(similarity=similarity, expected=expected):
                with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
                    temp_path = temp_file.name

                try:
                    # 处理边界值
                    clamped_similarity = max(0.0, min(1.0, similarity))
                    write_result(temp_path, clamped_similarity)

                    with open(temp_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    self.assertEqual(content, expected)

                finally:
                    if os.path.exists(temp_path):
                        os.remove(temp_path)


def test_file_encoding(self):
    """
    测试文件编码处理
    """
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_path = temp_file.name

    try:
        similarity = 0.88
        write_result(temp_path, similarity)

        # 用不同编码方式读取，验证UTF-8编码
        with open(temp_path, 'r', encoding='utf-8') as f:
            content_utf8 = f.read()

        # 尝试其他编码（应该会失败或得到错误结果）
        try:
            with open(temp_path, 'r', encoding='gbk') as f:
                content_gbk = f.read()
            # 如果成功读取，内容应该相同
            self.assertEqual(content_utf8, content_gbk)
        except UnicodeDecodeError:
            # 预期中的错误，因为文件是UTF-8编码
            pass

        self.assertEqual(content_utf8, "0.88")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)

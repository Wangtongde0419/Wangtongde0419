import unittest
from utils.text_processor import preprocess_text


class TestTextProcessor(unittest.TestCase):

    def test_preprocess_normal_text(self):
        text = "今天是星期天，天气晴，今天晚上我要去看电影。"
        result = preprocess_text(text)
        self.assertIsInstance(result, str)
        self.assertNotIn("，", result)

    def test_preprocess_empty_text(self):
        result = preprocess_text("")
        self.assertEqual(result, "")

    def test_preprocess_special_characters(self):
        text = "Hello, world! How are you?"
        result = preprocess_text(text)
        self.assertNotIn("!", result)
        self.assertNotIn("?", result)

    def test_preprocess_chinese_text(self):
        text = "自然语言处理很有趣"
        result = preprocess_text(text)
        self.assertIn("自然语言", result)


if __name__ == '__main__':
    unittest.main()

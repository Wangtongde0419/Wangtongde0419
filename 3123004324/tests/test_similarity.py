import unittest
from utils.similarity import calculate_similarity


class TestSimilarity(unittest.TestCase):

    def test_identical_texts(self):
        text1 = "今天是星期天天气晴今天晚上我要去看电影"
        text2 = "今天是星期天天气晴今天晚上我要去看电影"
        similarity = calculate_similarity(text1, text2)
        self.assertEqual(similarity, 1.0)

    def test_similar_texts(self):
        text1 = "今天是星期天天气晴今天晚上我要去看电影"
        text2 = "今天是周天天气晴朗我晚上要去看电影"
        similarity = calculate_similarity(text1, text2)
        self.assertGreaterEqual(similarity, 0.5)
        self.assertLessEqual(similarity, 0.9)
        print(f"原文预处理后: '{text1}'")
        print(f"抄袭版预处理后: '{text2}'")

    def test_different_texts(self):
        text1 = "今天是星期天天气晴今天晚上我要去看电影"
        text2 = "明天是星期一天气阴我明天要去上学"
        similarity = calculate_similarity(text1, text2)
        self.assertLess(similarity, 0.3)

    def test_empty_texts(self):
        similarity = calculate_similarity("", "测试文本")
        self.assertEqual(similarity, 0.0)

        similarity = calculate_similarity("测试文本", "")
        self.assertEqual(similarity, 0.0)

        similarity = calculate_similarity("", "")
        self.assertEqual(similarity, 0.0)


if __name__ == '__main__':
    unittest.main()

import re
import jieba


def preprocess_text(text):
    """
    改进的文本预处理函数，保持语义完整性
    """
    if not text or not isinstance(text, str):
        return ""

    # 1. 去除标点但保留重要语义符号
    text = re.sub(r'[^\w\u4e00-\u9fff\s]', '', text)

    # 2. 使用jieba精确分词
    words = jieba.cut(text, cut_all=False)

    # 3. 更智能的停用词过滤
    stop_words = {"的", "了", "在", "是", "我", "你", "他", "要", "去", "看", "今天", "晚上"}

    # 4. 保留重要语义词汇，包括单字词
    filtered_words = []
    for word in words:
        if (word not in stop_words and not word.isspace() and len(word) > 0):
            # 特别处理一些常见同义词
            if word == "周天":
                word = "星期天"
            elif word == "晴朗":
                word = "晴"
            filtered_words.append(word)

    return filtered_words

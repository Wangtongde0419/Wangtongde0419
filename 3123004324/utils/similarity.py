from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(text1, text2):
    """
    计算文本相似度（基于TF-IDF和余弦相似度）
    :param text1: 文本1
    :param text2: 文本2
    :return: 相似度得分（0-1之间）
    """
    if not text1 or not text2:
        return 0.0

    # 创建TF-IDF向量器
    vectorizer = TfidfVectorizer()

    try:
        # 将文本转换为TF-IDF向量
        tfidf_matrix = vectorizer.fit_transform([text1, text2])

        # 计算余弦相似度
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

        return round(similarity, 2)

    except Exception as e:
        print(f"相似度计算错误: {str(e)}")
        return 0.0

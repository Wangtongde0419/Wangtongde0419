def write_result(file_path, similarity):
    """
    将结果写入文件
    :param file_path: 输出文件路径
    :param similarity: 相似度得分
    :raises: IOError
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"{similarity:.2f}")
    except Exception as e:
        raise IOError(f"写入文件时发生错误: {str(e)}")

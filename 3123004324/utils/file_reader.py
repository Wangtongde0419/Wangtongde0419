def read_file(file_path):
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容字符串
    :raises: FileNotFoundError, ValueError, IOError
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if not content.strip():
            raise ValueError("文件内容为空")

        return content

    except FileNotFoundError:
        raise FileNotFoundError(f"文件未找到: {file_path}")
    except UnicodeDecodeError:
        # 尝试其他编码方式
        try:
            with open(file_path, 'r', encoding='gbk') as file:
                content = file.read()
            # 检查解码后的内容是否为空
            if not content.strip():
                raise ValueError("文件内容为空")
            return content
        except ValueError as e:
            # 重新抛出ValueError，避免被包装成IOError
            raise e
        except Exception:
            raise IOError(f"无法解码文件: {file_path}")
    except ValueError as e:
        # 直接重新抛出ValueError，不包装成IOError
        raise e
    except Exception as e:
        raise IOError(f"读取文件时发生错误: {str(e)}")

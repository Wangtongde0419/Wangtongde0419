mport argparse
import sys
from utils.file_reader import read_file
from utils.text_processor import preprocess_text
from utils.similarity import calculate_similarity
from utils.result_writer import write_result


def main():
    parser = argparse.ArgumentParser(description='论文查重系统')
    parser.add_argument('orig_path', type=str, help='原文文件路径')
    parser.add_argument('copy_path', type=str, help='抄袭版文件路径')
    parser.add_argument('output_path', type=str, help='结果输出文件路径')

    args = parser.parse_args()

    try:
        # 读取文件内容
        orig_content = read_file(args.orig_path)
        copy_content = read_file(args.copy_path)

        # 文本预处理
        processed_orig = preprocess_text(orig_content)
        processed_copy = preprocess_text(copy_content)

        # 计算相似度
        similarity = calculate_similarity(processed_orig, processed_copy)

        # 输出结果
        write_result(args.output_path, similarity)

        print(f"查重完成！相似度为: {similarity:.2f}")
        sys.exit(0)

    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

from jamo import h2j, j2hcj
def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fin:
        lines = fin.readlines()
    # 对每一行应用 h2j 和 j2hcj
    processed = [j2hcj(h2j(line.rstrip('\n'))) + '\n' for line in lines]
    with open(output_path, 'w', encoding='utf-8') as fout:
        fout.writelines(processed)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("用法: python hcj.py 输入文件 输出文件")
        sys.exit(1)
    process_file(sys.argv[1], sys.argv[2])
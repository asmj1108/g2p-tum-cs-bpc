import os


def reorganize_dataset(entry: str):
    # Define paths
    original_data_path = os.path.abspath(entry)
    splits = ['train', 'dev', 'test']  # Target directories to create

    # Create data directory first
    data_dir = 'data'
    os.makedirs(data_dir, exist_ok=True)

    # Create split directories inside the data directory
    for split in splits:
        os.makedirs(os.path.join(data_dir, split), exist_ok=True)

    # Process each language directory
    for lang in os.listdir(original_data_path):
        lang_dir = os.path.join(original_data_path, lang)

        # Verify this is a directory
        if not os.path.isdir(lang_dir):
            continue

        # Process each split file
        for split in splits:
            src_file = os.path.join(lang_dir, f"{lang}_{split}.tsv")
            dest_file = os.path.join('data', split, f"{lang}.tsv")

            if not os.path.exists(src_file):
                print(f"Warning: File not found: {src_file}")
                continue

            # Process TSV file: remove spaces from the second column
            with open(src_file, 'r', encoding='utf-8') as src, \
                    open(dest_file, 'w', encoding='utf-8') as dest:

                for line in src:
                    parts = line.strip().split('\t')
                    if len(parts) < 2:
                        # Write lines with <2 columns as-is
                        dest.write(line)
                        continue

                    # Remove spaces from second column
                    parts[1] = parts[1].replace(' ', '')
                    dest.write('\t'.join(parts) + '\n')

            print(f"Processed: {src_file} -> {dest_file}")


if __name__ == '__main__':
    paths = ["../../data"]
    # paths = ["../../multilingual_data/1F1S", "../../multilingual_data/DF1S", "../../multilingual_data/1FDS", "../../multilingual_data/transliteration"]
    for p in paths:
        reorganize_dataset(p)

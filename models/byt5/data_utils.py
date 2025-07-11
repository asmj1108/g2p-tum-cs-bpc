import os
import pandas as pd
import numpy as np
from datasets import Dataset
from tqdm import tqdm


def load_pronunciation_dictionary(path: str, language: str, prefix: bool = False) -> Dataset:
    
    words = []
    prons = []
    variants = []
    with open(path,'r', encoding='utf-8') as f:
        for line in f.readlines():
            word, pron = line.strip().split('\t')
            if ',' in pron:
                variant = ','.join(pron.split(',')[1:]).replace(' ','')
                pron = pron.split(',')[0]
            else:
                variant = ''
            if prefix:
                word = '<'+language+'>:' + word
            words.append(word)
            prons.append(pron)
            variants.append(variant)
    
    data = pd.DataFrame()
    data['word'] = words
    data['pron'] = prons
    data['variant'] = variants
    data['language'] = language
    return Dataset.from_pandas(data)



def load_all_pronunciation_dictionaries(path: str, prefix: bool = False, mask_prob: float = 0.0) -> Dataset:
    files = [i for i in os.listdir(path) if i.endswith('.tsv')]

    all_datasets = []

    for file in tqdm(files):
        language = file.replace('.tsv','')

        data = load_pronunciation_dictionary(path=os.path.join(path, file), language=language, prefix=False) # Load without prefix first

        if prefix:
            words = []
            for word in data['word']:
                if mask_prob > 0.0:
                    if np.random.uniform() < mask_prob:
                        lang_prefix = '<unk>'
                    else:
                        lang_prefix = f'<{language}>'
                else:
                    lang_prefix = f'<{language}>'
                words.append(f'{lang_prefix}: {word}')

            # Replace the original 'word' column
            data = data.remove_columns('word').add_column('word', words)

        all_datasets.append(data)

    # Concatenate all datasets at the end
    from datasets import concatenate_datasets
    return concatenate_datasets(all_datasets)

if __name__ == "__main__":
    pass

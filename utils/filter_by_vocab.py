import pandas as pd
from typing import List, Dict
from argparse import ArgumentParser


def read_vocab(path: str) -> pd.DataFrame:
    data = []
    with open(path, encoding='utf-8') as input_stream:
        for line in input_stream:
            data.append({'label': line.split('||')[0], 'concept_name':line.strip().split('||')[1]})
    return set(pd.DataFrame(data).label.tolist())


def read_annotation_file(ann_file_path: str) -> List[Dict[str, str]]:
     data: List[Dict[str, str]] = []
     with open(ann_file_path, encoding='utf-8') as input_stream:
         for row_id, line in enumerate(input_stream):
             splitted_line = line.strip().split('||')
             data.append(splitted_line)
     return data


def save_dataset(data, fpath):
     with open(fpath, 'w', encoding='utf-8') as output_stream:
         for sample in data:
             output_stream.write('||'.join(sample) + '\n')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--vocab')
    parser.add_argument('--save_to')
    args = parser.parse_args()

    data = read_annotation_file(args.input)
    vocab = read_vocab(args.vocab)

    filtered_data = []
    for sample in data:
        if sample[4] in vocab:
            filtered_data.append(sample)
    save_dataset(filtered_data, args.save_to)

from NLPDatasetIO.dataset import Dataset, Document
from argparse import ArgumentParser
import os
from glob import glob
import pandas as pd
from dataclasses import asdict
from sklearn.model_selection import train_test_split


def get_args():
    parser = ArgumentParser()
    parser.add_argument('--dataset_folder', type=str, default='../RUCCON')
    parser.add_argument('--save_to', type=str, default='../processed_data/full')
    parser.add_argument('--save_to_train', type=str, default='../processed_data/train')
    parser.add_argument('--save_to_test', type=str, default='../processed_data/test')
    parser.add_argument('--save_to_cuiless', type=str, default='../processed_data/cuiless')
    parser.add_argument('--random_split', action='store_true')
    return parser.parse_args()


def read_corpus(corpus_folder: str) -> Dataset:
    subfolder_paterns = [os.path.join(corpus_folder, 'main/*[!ann|txt]'),
                         os.path.join(corpus_folder, 'main1/*[!ann|txt]'),
                         os.path.join(corpus_folder, '*[!main|main1|conf]'),
                         ]

    subfolders = [
        subfolder for subfolder_patern in subfolder_paterns for subfolder in glob(subfolder_patern)
    ]
    full_dataset = []
    for subfolder in subfolders:
        ds_part = Dataset(location=subfolder, format='brat')
        full_dataset.append(ds_part)
        if len(full_dataset) > 1:
            full_dataset[0].documents += ds_part.documents[:]
    return full_dataset[0]


def is_annotated_document(document: Document):
    for entity in document.entities:
        if entity.label is None: return False
    return True


def get_entities_from_dataset(dataset):
    entities = []
    for document in dataset.documents:
        for entity in document.entities.values():
            entity_d = asdict(entity)
            entity_d['path'] = document.doc_id
            entity_d['document_id'] = document.doc_id
            entities.append(entity_d)
    return pd.DataFrame(entities)


def main() -> None:
    args = get_args()
    dataset = read_corpus(args.dataset_folder)
    entities = get_entities_from_dataset(dataset)    
    entities['text'] = entities.text.str.replace('\n', ' ')

    entities_all_filled = entities[(~entities.label.isnull()) & (entities.label != 'UNKNOWN')]
    cuiless = entities[entities.label == 'CUILESS']
    entities_all_filled = entities_all_filled[entities_all_filled.label != 'CUILESS']
    entities_all_filled = entities_all_filled[~entities_all_filled.label.isnull()]

    save_to = os.path.join(args.save_to, '0.concept')
    if not os.path.exists(args.save_to):
        os.mkdir(args.save_to)

    with open(save_to, 'w') as output_stream:
        for row_idx, row in entities_all_filled.iterrows():
            output_stream.write(
                f"{row['entity_id']}||{row['start']}|{row['end']}||{row['type']}||{row['text']}||{row['label']}\n")

    if args.random_split:
        train, test = train_test_split(entities_all_filled, test_size=0.3)

        save_to = os.path.join(args.save_to_train, '0.concept')
        if not os.path.exists(args.save_to_train):
            os.mkdir(args.save_to_train)
        with open(save_to, 'w') as output_stream:
            for row_idx, row in train.iterrows():
                output_stream.write(
                    f"{row['entity_id']}||{row['start']}|{row['end']}||{row['type']}||{row['text']}||{row['label']}\n")

        save_to = os.path.join(args.save_to_test, '0.concept')
        if not os.path.exists(args.save_to_test):
            os.mkdir(args.save_to_test)
        with open(save_to, 'w') as output_stream:
            for row_idx, row in test.iterrows():
                output_stream.write(
                    f"{row['entity_id']}||{row['start']}|{row['end']}||{row['type']}||{row['text']}||{row['label']}\n")

    save_to = os.path.join(args.save_to_cuiless, '0.concept')
    if not os.path.exists(args.save_to_cuiless):
        os.mkdir(args.save_to_cuiless)
    with open(save_to, 'w') as output_stream:
        for row_idx, row in cuiless.iterrows():
            output_stream.write(f"{row['entity_id']}||{row['start']}|{row['end']}||{row['type']}||{row['text']}||{row['label']}\n")


if __name__ == '__main__':
    main()


from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--train')
    parser.add_argument('--test')
    parser.add_argument('--save_to')
    args = parser.parse_args()

    with open(args.train, encoding='utf-8') as input_stream:
        train_data = [line.split('||') for line in input_stream]

    with open(args.test, encoding='utf-8') as input_stream:
       	test_data = [line.split('||') for line in input_stream]

    cui_index = set()
    mention_index = set()
    for train_example in train_data:
        cui_index.add(train_example[4])
        mention_index.add(train_example[3])

    with open(args.save_to, 'w', encoding='utf-8') as output_stream:
        for test_example in test_data:
            if test_example[3] not in mention_index and test_example[4] in cui_index:
                output_stream.write('||'.join(test_example))

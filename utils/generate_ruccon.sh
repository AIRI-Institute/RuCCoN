

python russian_corpora_final2concept.py --random_split
python filter_by_vocab.py --input ../processed_data/full/0.concept --vocab ../vocabs/umls_rus.txt --save_to ../processed_data/full/0.concept
python filter_by_vocab.py --input ../processed_data/train/0.concept --vocab ../vocabs/umls_rus.txt --save_to ../processed_data/train/0.concept
python filter_by_vocab.py --input ../processed_data/test/0.concept --vocab ../vocabs/umls_rus.txt --save_to ../processed_data/test/0.concept

cat ../processed_data/test/0.concept ../processed_data/cuiless/test.concept > ../processed_data/test-cuiless/0.concept
cat ../processed_data/train/0.concept ../processed_data/cuiless/train.concept > ../processed_data/train_cuiless/0.concept

mkdir ../processed_data/test-stratified
python make_stratified.py --train ../processed_data/train/0.concept --test ../processed_data/test/0.concept --save_to ../processed_data/test-stratified/0.concept
mkdir ../processed_data/test-zero-shot
python make_zero_shot.py --train ../processed_data/train/0.concept --test ../processed_data/test/0.concept --save_to ../processed_data/test-zero-shot/0.concept

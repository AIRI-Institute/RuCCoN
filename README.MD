# RuCCoN: Clinical Concept Normalization in Russian

We present RuCCoN, a new dataset for clinical concept normalization in Russian manually annotated by medical professionals. It contains over 16,028 entity mentions manually linked to over 2,409 unique concepts from the Russian language 
part of the UMLS ontology. We provide train/test splits for different settings (stratified, zero-shot, and CUI-less) and present strong baselines obtained with state-of-the-art models such as SapBERT. At present, Russian medical NLP is 
lacking in both datasets and trained models, and we view this work as an important step towards filling this gap. This repository contains dataset, annotation guidelines and dataset preprocessing guidelines. 


---

# Dataset statistics table

| Subset          | #entities | #unique entities  | #concepts |
|-----------------|-----------|-------------------|-----------|
| Full train      | 12189     | 5435              | 2031      |
| In-KB train     | 11220     | 4934              | 2030      |
| Full test       | 5132      | 2689              | 1232      |
| In-KB test      | 4808      | 2464              | 1231      |
| Zero-shot test  | 434       | 417               | 379       |
| Stratified test | 1266      | 1199              | 576       |
| RWN med.        | 2319      | 1666              | 635       |
| XL-BEL          | 681       | 610               | 510       |
| MCN             | 13609     | 5979              | 3792      |

For more details please refer to the paper.

# Results table
| Model                      | In-KB test |        | Full test |        | Stratified test |        | Zero-shot test |        |
|----------------------------|------------|--------|-----------|--------|-----------------|--------|----------------|--------|
|                            | Acc@1      | Acc@5  | Acc@1     | Acc@5  | Acc@1           | Acc@5  | Acc@1          | Acc@5  |
| Tf-Idf                     | 37.58%     | 46.98% | -         | -      | 25.83%          | 34.20% | 26.27%         | 41.01% |
| Multilingual BERT          | 29.01%     | 33.74% | 29.15%    | 33.16% | 12.32%          | 16.35% | 15.90%         | 19.35% |
| RuBERT                     | 25.17%     | 28.22% | 24.05%    | 25.66% | 11.53%          | 14.53% | 13.82%         | 17.51% |
| SapBERT                    | 45.84%     | 56.41% | 37.18%    | 37.47% | 30.02%          | 40.44% | 29.49%         | 40.78% |
| SapBERT+MCN                | 46.51%     | 56.45% | 43.67%    | 53.23% | 30.41%          | 40.60% | 27.88%         | 41.47% |
| SapBERT+RWN                | 45.47%     | 55.12% | 43.30%    | 50.19% | 29.94%          | 39.42% | 29.03%         | 38.48% |
| SapBERT+XL-BEL             | 47.77%     | 58.74% | 40.80%    | 42.30% | 32.54%          | 42.97% | 29.95%         | 45.16% |
| SapBERT+dataset            | 59.26%     | 68.99% | 53.39%    | 60.02% | 47.31%          | 61.45% | 32.95%         | 47.47% |
| SapBERT+dataset+RWN        | 57.84%     | 68.55% | 52.67%    | 58.79% | 47.79%          | 63.67% | 32.49%         | 46.31% |
| SapBERT+dataset+XL-BEL     | 58.78%     | 68.05% | 53.20%    | 59.80% | 46.52%          | 59.08% | 33.41%         | 48.85% |
| SapBERT+dataset+RWN+XL-BEL | 58.55%     | 67.82% | 52.65%    | 59.20% | 50.32%          | 62.48% | 33.41%         | 45.85% |
For more details please refer to the paper.

# Dataset preprocessing

To pre-process the dataset first install the requirements

```bash
 pip install -r requirements.txt
```

then run the command
```bash
 ./utils/generate_ruccon.sh
```

# Train and Evaluate models

To train and evaluate model we utilized source code from https://github.com/AIRI-Institute/medical_crossing

# Citing & Authors

Nesterov A. et al. RuCCoN: Clinical Concept Normalization in Russian //Findings of the Association for Computational Linguistics: ACL 2022. – 2022. – С. 239-245. 

```
@inproceedings{nesterov2022ruccon,
  title={RuCCoN: Clinical Concept Normalization in Russian},
  author={Nesterov, Alexandr and Zubkova, Galina and Miftahutdinov, Zulfat and Kokh, Vladimir and Tutubalina, Elena and Shelmanov, Artem and Alekseev, Anton and Avetisian, Manvel and Chertok, Andrey and Nikolenko, Sergey},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2022},
  pages={239--245},
  year={2022}
}
```

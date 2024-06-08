# ZepScope - Checker

## Description

Detecting Insecure OpenZeppelin Code in Smart Contracts.

## How to Use
ZepScope-Checker is based on falcon-metatrust ([https://github.com/MetaTrustLabs/falcon-metatrust](https://github.com/MetaTrustLabs/falcon-metatrust)). You can use it in the same way you use falcon. In this repo, we provide the facts used in our paper in the [config.py](https://github.com/ZepScope/ZepScope/tree/main/Checker/falcon/detectors/zep_checker/configs.py)

1. Install dependencies,

- Requires Python 3.9+
- Install Python dependencies: `pip install -r requirements.txt`


2. Install ZepScope-Checker:

```shell
python setup.py install
```

3. Run Checker:

```shell
python -m falcon [relative file based on root directory of falcon]
```

## Dataset

Dataset used to evaluate GPTScan in the paper, are the following:
1. GroundTruth Dataset: [https://github.com/ZepScope/dataset/tree/main/groundtruth](https://github.com/ZepScope/dataset/tree/main/groundtruth)
2. Large Scale Dataset: [https://github.com/ZepScope/dataset/tree/main/large_scale_datasets](https://github.com/ZepScope/dataset/tree/main/large_scale_datasets)







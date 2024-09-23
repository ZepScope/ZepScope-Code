# ZepScope

Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts

## Structure:

[ZepScope - Miner](https://github.com/ZepScope/ZepScope-Code/tree/main/Checker): MINER analyzes the official OpenZeppelin functions to extract the facts of explicit checks (i.e., the checks defined within the functions) and implicit checks (i.e., the conditions of calling the functions)

[ZepScope - Checker](https://github.com/ZepScope/ZepScope-Code/tree/main/Checker): CHECKER examines real contracts to identify their OpenZeppelin functions, match their checks with those in the facts, and validate the consequences for those inconsistent checks.


## How to Cite this project

```bibtex
@inproceedings{liu2024zepscope,
    author = {Han Liu and Daoyuan Wu and Yuqiang Sun and Haijun Wang and Kaixuan Li and Yang Liu and Yixiang Chen},
    title = {Using My Functions Should Follow My Checks: Understanding and Detecting Insecure {OpenZeppelin} Code in Smart Contracts},
    booktitle = {33rd USENIX Security Symposium (USENIX Security 24)},
    year = {2024},
    isbn = {978-1-939133-44-1},
    address = {Philadelphia, PA},
    pages = {3585--3601},
    url = {https://www.usenix.org/conference/usenixsecurity24/presentation/liu-han},
    publisher = {USENIX Association},
    month = aug
}
```

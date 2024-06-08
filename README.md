# ZepScope

Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts

## Structure:

[ZepScope - Miner](https://github.com/ZepScope/ZepScope/tree/main/Miner): MINER analyzes the official OpenZeppelin functions to extract the facts of explicit checks (i.e., the checks defined within the functions) and implicit checks (i.e., the conditions of calling the functions)

[ZepScope - Checker](https://github.com/ZepScope/ZepScope/tree/main/Checker): CHECKER examines real contracts to identify their OpenZeppelin functions, match their checks with those in the facts, and validate the consequences for those inconsistent checks.


## How to Cite this project

```bibtex
@inproceedings{liu2024zepscope,
    author = {Liu, Han and Wu, Daoyuan and Sun, Yuqiang and Wang, Haijun and Li, Kaixuan and Liu, Yang and Chen, Yixiang},
    title = {Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts},
    year = {2024},
    publisher = {USENIX Association},
    address = {Philadelphia, PA, USA},
    booktitle = {Proceedings of the 2024 USENIX Security Symposium},
    series = {USENIX Security'24}
}
```
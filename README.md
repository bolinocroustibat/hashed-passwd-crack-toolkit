# Hash cracking testkit

## Prerequisites

Install [hashcat](https://hashcat.net/hashcat/). It is a password cracking tool.


## To hash a password and test it against a hash

```bash
python3 test.py
```

## To search for a password from a hash using "search that hash" CLI

[Search That Hash](https://github.com/HashPals/Search-That-Hash) is a Python lib that uses online services to search for hashes, plus [hashcat](https://hashcat.net/hashcat/) to search offline.

To search for a password from a hash using "search that hash" directly, run the following command:
```bash
sth -t <hash> -w <wordlist>
```
The argument `-t` is the hash to be searched for. The argument `-w` is the wordlist to be used, in case you also want to search offline using hashcat. The wordlist should be a text file with one password per line.

## About the hashcat wordlists

A popular password wordlist is rockyou.txt. It contains a list of commonly used passwords and is popular among pen testers.
IT can be downloaded from [here](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt/download?datasetVersionNumber=1). The file is too large to be uploaded to github.
The file should be places in the `wordlists` directory.

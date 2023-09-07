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

## To search for a password from a hash using "hashcat" CLI

For example:
```bash
hashcat -m 1400 -a 3 "6e16f6b886303bccbrdc7f0bc87b35rec36f15ac94075748e04ff5004ab5deed" wordlists/rockyou.txt --force
```
You might want to consider running it on a Google Colab notebook to use the GPUs.

## About the hashcat wordlists

A popular password wordlist is `rockyou.txt`. It contains a list of commonly used passwords and is popular among pen testers.
It can be downloaded from [here](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt/download?datasetVersionNumber=1). The file is too large to be uploaded to github.
The file should be places in the `wordlists` directory.

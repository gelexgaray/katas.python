# python-code-katas
Repository for Code Katas


# Setup

1. If you don't already have a virtualenv installed (or a virtual environment process), setup it up with help from the [Python Packaging User Guide](https://packaging.python.org/en/latest/installing.html#virtual-environments).  In short, for Python <3.4, securely download [get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py) and then execute the following (omit sudo if you can):

```bash
sudo python get-pip.py
sudo pip install -U setuptools
sudo pip install virtualenv
```

2. Now setup a virtual environment for this repository.

```bash
cd python-code-kata
virtualenv .
source bin/activate
```

3. (Optional) Install any additional libraries. 

```bash
pip install -r requirements.txt
```

# References

[Python Packaging User Guide](https://packaging.python.org/en/latest/installing.html#virtual-environments)

[Las Vegas Python User Group's code katas repository](https://github.com/vegaspy/python-code-kata)
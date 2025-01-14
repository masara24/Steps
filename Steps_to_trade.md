## Pip command

```
pip install -i https://mirrors.aliyun.com/pypi/simple/--trusted-host mirrors.aliyun.com numpy

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple efinance

pip install dsxkline

#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pysqlite3

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple stockstats
```

## Git command

```
git config --global -l

git clone https://github.com/masara24/Steps.git

notepad Steps_to_trade.md

# C:\Users\Administrator\Downloads\PortableGit\python311\Scripts

PATH=C:\Users\Administrator\Downloads\PortableGit\python311\Scripts;C:\Users\Administrator\Downloads\PortableGit\python311;C:\Users\Administrator\Downloads\PortableGit\cmd;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Users\Administrator\AppData\Local\Microsoft\WindowsApps

# download jsonpath 

https://files.pythonhosted.org/packages/cf/a1/693351acd0a9edca4de9153372a65e75398898ea7f8a5c722ab00f464929/jsonpath-0.82.2.tar.gz

# or wget

wget http://www.ultimate.com/phil/python/download/jsonpath-0.82.tar.gz

# modify setup.py

from distutils.core import setup

import sys
import os

# must use absolute path
sys.path.insert(0, r"C:\Users\Administrator\Downloads\python310_with_getpip\jsonpath-0.82\jsonpath-0.82")
import jsonpath as module

name = module.__name__
version = module.__version__

name = "jsonpath"
version = "0.82.2"

url_base = "http://www.ultimate.com/phil/python/"

# must use .
pip install .
```


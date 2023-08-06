首先，在pypi创建个账号。
创建如下目录：

package/
 |__src/
 | |__(你的包名)/
 |   |__ __init__.py
 |   |__(你的py文件)
 |__texts
 |__LICENSE
 |__pyproject.toml
 |__README.md
__init__.py文件什么内容都不用写。
texts文件夹空着。
LICENSE文件是许可证文件，一般是MIT，填写：

Copyright (c) 2018 The Python Packaging Authority

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

README.md写对你库的描述。
pyproject.toml内容较多：

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "你库的名字"
version = "库的版本"
authors = [
  { name="你的名字", email="你的邮件" },
]
description = "对你的库一句话的描述"
readme = "README.md"
requires-python = ">=3.1"#python版本是2.*.*的填2.1 是3.*.*的填3.1
classifiers = [
    "Programming Language :: Python :: 3",#python版本是2.*.*的填2 是3.*.*的填3
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/ezezwsez/ezu"
"Bug Tracker" = "https://github.com/ezezwsez/ezu/issues"
现在可以开始打包了
windows下命令行输入py -m pip install build 如果是Unix/macOS把py改为python3（后面相同）
然后在package文件夹下命令行输入py -m build
会发现dist文件夹下有两个文件:
dist/
|__(你的包名)-版本-py3-none-any.whl
|__(你的包名)-版本.tar.gz
下面就可以上传了
命令行输入py -m pip install twine
然后在package文件夹下命令行输入twine upload dist/*
输入用户名和密码就上传成功了!(输入时密码不会显示)
可以输入pip install 你的包名   来下载
���ȣ���pypi�������˺š�
��������Ŀ¼��

package/
 |__src/
 | |__(��İ���)/
 |   |__ __init__.py
 |   |__(���py�ļ�)
 |__texts
 |__LICENSE
 |__pyproject.toml
 |__README.md
__init__.py�ļ�ʲô���ݶ�����д��
texts�ļ��п��š�
LICENSE�ļ������֤�ļ���һ����MIT����д��

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

README.mdд������������
pyproject.toml���ݽ϶ࣺ

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "��������"
version = "��İ汾"
authors = [
  { name="�������", email="����ʼ�" },
]
description = "����Ŀ�һ�仰������"
readme = "README.md"
requires-python = ">=3.1"#python�汾��2.*.*����2.1 ��3.*.*����3.1
classifiers = [
    "Programming Language :: Python :: 3",#python�汾��2.*.*����2 ��3.*.*����3
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
"Homepage" = "https://github.com/ezezwsez/ezu"
"Bug Tracker" = "https://github.com/ezezwsez/ezu/issues"
���ڿ��Կ�ʼ�����
windows������������py -m pip install build �����Unix/macOS��py��Ϊpython3��������ͬ��
Ȼ����package�ļ���������������py -m build
�ᷢ��dist�ļ������������ļ�:
dist/
|__(��İ���)-�汾-py3-none-any.whl
|__(��İ���)-�汾.tar.gz
����Ϳ����ϴ���
����������py -m pip install twine
Ȼ����package�ļ���������������twine upload dist/*
�����û�����������ϴ��ɹ���!(����ʱ���벻����ʾ)
��������pip install ��İ���   ������
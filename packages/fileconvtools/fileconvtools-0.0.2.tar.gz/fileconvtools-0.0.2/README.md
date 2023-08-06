# fileconvtools

## csv to xlsx convert

*.csv 확장자 파일을 *.xlsx 파일로 변환합니다.



## 배포절차

pㅔython setup.py sdist bdist_wheel
pip install twine

파일 빌드
- python setup.py sdist bdist_wheel


Pypi 상에 배포
- python -m twine upload dist/*

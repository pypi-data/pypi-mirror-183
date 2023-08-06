# Ezbox


## Description

A simple python package to help python.

## Getting Started

### Installing

* pip install ez-box

### Executing program

```
from ez-box import *
```

## How to use
* Have you always wanted to display messagesboxes on your python code? Then this is the package for you!
```
box('title','text')
```

* You can also verify is the use clicked ok!
```
MyBox = box('title','text')
if MyBox == True:
	print('You clicked ok')
else:
	print('Closed or canceled')
```
* Are you more into converting binary?
```
int2bin(15)
#1111
bin2int('1111')#Use '' like a str
#15
txt2bin('Some text')
#010100110110111101101101011001010010000001110100011001010111100001110100
bin2txt('010100110110111101101101011001010010000001110100011001010111100001110100')
#Some text
```

## Authors


ex. Batte  
ex. [My pypi profile](https://pypi.org/user/Batte/)


## License

This project is licensed under the Batte License - see the LICENSE.md file for details

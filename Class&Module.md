# Class

## Instance & Object

- Cookie frame is class
```python
>>> peanutCookie = Cookie()
>>> chocoCookie = Cookie()
```
- peanutCookie and chocoCookie is object
- peanutCookie and chocoCookie is instance of Cookie

## Class Structure

- pass perform nothing

```python
class FourCal():
def setdata(self, first, second):
    self.first = first
    self.second = second
>>> a = FourCal()
a.set(4,2)         
```
`a -> self` `4 ->first` `2 -> second`

## Constructor , Inheritance, Overriding
```python
class Math():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

class MoreMath(Math):
    def div(self):
        result = self.first / self.second
        return result

class FixMath(MoreMath):
    def div(self):
        if self.second == 0:
            print('change the second num')
            return  
        else: 
            return self.first/self.second
```

# Module 
## import module

- import module
- import importlib
- importlib.reload(module)

1. sys.path.append
```python
>>> import sys
>>> sys.path
>>> sys.path.append("C:/python/Mymodules")
```
2. PYTHONPATH
`CMD` - `C:\Users\home>set PYTHONPATH=C:\Python\Modules`

## import method
- from module import method1, method2
- from module import *

## if __name__ == "__main__":


# Pakage

- __init__.py let the directory is part of the package
- from a.b.c import *
- __all__ = ['c']

## relative import 
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

# Module 
import module
import importlib
importlib.reload(module)

## namespace
from module import method1, method2
from module import *   // import all method

## if __name__ == "__main__":

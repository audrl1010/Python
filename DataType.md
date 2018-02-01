# Data Type

Normally Python judge data type itself

## Number
- You can squared number by **

## String
### Write String
```python
>>> "Hello World"
>>> 'Hello World'
>>> """Hello World"""
```
- Use back slash `\` when you want to use `'` or `"`
- string can add and multiply

### Indexing & Slicing

```python
>>> a = "Learn Python is Fun!"
>>> b = a[0] + a[6] + a[16] a[-1]
>>> b
'LPF!'
```

## List
### Indexing & Slicing

```python
>>> list = [a,b,c,[1,2,3,['faith','hope','love']]]
>>> list[3][3][2]
love
>>>list[3][3][:2]
['faith','hope'] 
```

### Operator
Add & Multiply
```python
>>> a = [1,2,3]
>>> b = [a,b,c]
>>> a + b
[1,2,3,a,b,c]
>>> c = a + b
>>> str(c) + "hi"
```

### Modify & Various function
Modify
```python
>>> a = [1,2,3]
"case1"
>>> a[1:2] = ['a','b','c']
>>> a
[1,'a','b','c',3]
"case2"
>>> a[1] = ['a','b','c']
>>> a
[1,['a','b','c'],3]
```

a.append()
a.sort()
a.index()
a.insert()
a.remove()
a.pop()
a.count()
a.extend()

## Tuple

- Tuple is immutable data type
- Tuple can not delete or change


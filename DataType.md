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

- a.append()
- a.sort()
- a.index()
- a.insert()
- a.remove()
- a.pop()
- a.count()
- a.extend()

## Tuple
- Tuple is immutable data type
- Tuple can not delete or change
- Tuple can do slice, indexing, add, multiply

```python
>>> t1 = ()
>>> t2 = (1,)
```
## Dictionary

- {`Key1`:`Value1`, `Key2`:`Value2`, `Key3`:`Value3` ...}
- Dictionary is unordered type
- You can not make a same key

### Modify
- add & delete

```python
>>> a = {1:'a'}
>>> a[2] = {2:'b'} 
>>> a
a = {1:'a', 2:'b'}
>>> del a[1]
>>> a
a = {2:'b'}
```

### Usage

```python
>>> dic = {'name':'sean', 'phone':'010','gender':'female'}
>>> dic['name']
sean

>>> for k in dic.keys():
    print(k)
name
phone
gender

>>> dic.values()
>>> dic.items()
[('name':'sean'), ('phone':'010'),('gender':'female')]

>>> dic['nokey']
error
>>> dic.get('nokey',None)
None
```

## Set
- Not allow overlap
- Unordered 
- If you want indexing set, you have to transit to list or tuple 

```python
>>> s1 = set([1,2,3])
>>> s1
{1, 2, 3}
>>> s2 = set('Hello')
>>> s2
{'e','l','o','h'}
```

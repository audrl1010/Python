# Python
Python 정리 저장소

## if, elif, else
Have to do identation on forehead executeing statement.
```python
if conditional statement:
	executing statement...
elif conditional statment:
	executing statement...
else:
	executing statement...
```
### what is conditional statement ?
The conditional statement is a sentence that judges true and false.

| Type | True | False |
| ------------- | ------------- | ------------- |
| Integer  | non-zero  | 0 |
| String  | "abc"  | "" |
| List  | [1, 2, 3]  | [] |
| Tuple  | (1,2,3)  | () |
| Dictionary  | { "a": "b" }  | {} |

### Comparison operator
`Comparison operators`(`<`, `>`, `==`, `!=`, `>=`, `<=`) are used when judging whether a condition is `true` or `false`.

### and, or, not
There are other operators judging a condition(`and`, `or`, `not`).

| Operator | Description |
| ------------- | ------------- |
| x or y  | True if either x or y is true. |
| x and y  | True if both x or y is true. |
| not x  | True if x is false |

### x in sequnece, x not in sequence
| in | not in |
| ------------- | ------------- |
| x in list  | x not in list |
| x in tuple  | x not in tuple |
| x in string  | x not in string |

```python
## list
>>> 1 in [1, 2, 3]
True
>>> 1 not in [1, 2, 3]
False

## tuple
>>> 'a' in ('a', 'b', 'c')
True

## string
>>> 'j' not in 'python'
True
```

## while
```python
while conditional statement:
	executing statement....
```

## Forcing a while statement to exit
```python
while conditional statement:
	executing statement...
break
	executing statement...
```

## If conditional statement wrong, return to the beginning in while statement.
```python
number = 0
while number < 10:
	number += 1
if number % 2 == 0: continue
	print(number)
```

## For


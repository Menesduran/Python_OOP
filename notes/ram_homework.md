# RAM Homework: Heap, Stack and Garbage Collector

Status: in progress

How to use this file: research each question, write the answer in your own
words, and add the source link. Run the small experiments yourself.

## Questions

### 1. What are the two areas of RAM we study: heap and stack?
- My answer:
- Source:

### 2. Where is `x = 2` stored? Where is `y = [1, 2, 3]` stored?
- Keywords to research: names are references, `id()`, mutable vs immutable
- My answer:
- Source:

### 3. Where are functions, their parameters and local variables stored?
- Keywords to research: call stack, stack frame
- My answer:
- Source:

### 4. Where are a class, its methods and attributes stored? What about an object?
- My answer:
- Source:

### 5. What is the Garbage Collector? How does it work? How many generations/areas does it have?
- Keywords to research: reference counting, generational GC, `gc` module
- My answer:
- Source:

### 6. What is the lifetime of an object? When does it end and what happens then?
- My answer:
- Source:

## Experiments

```python
import sys

a = [1, 2]
b = a              # b is another name for the SAME list
b.append(3)
print(a)           # what do you expect? run it and check
print(a is b)
print(id(a), id(b))
print(sys.getrefcount(a))
```

Write what you observed here:

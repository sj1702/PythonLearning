
### integer vs float

- If most integer values can be represented as a float by adding a decimal and a 0 after it, and float values have a much wider range of values that includes decimal values, why would we ever need to use integers over floats?

- **Answer**:
  - it would  probably make more sense to use integer values to count things that do not have fractional values, like counting how many students are in a class, or the length of a string in Python, which is always a whole number (You will never have a string that is 2.5 characters long).
  - float values sometimes behave in unexpected ways due to how they are stored in computer memory, especially when using very large float values.
  - list can only access elements by whole number indexes.
  - range() function in python can takes only whole numbers


### nested list
- [example](https://github.com/nitops/python-practice/blob/main/1_basic_pyhon/3_lists/1.2_nested_list_example.py)
- Do the lists passed to the zip() function have to be the same length?
  - The zip() function will only iterate over the smallest list passed. If given lists of different lengths, the resulting combination will only be as long as the smallest list passed



### python's end parameter in print()

- By default python's print() function ends with a newline. A programmer with C/C++ background may wonder how to print without newline.
- Python's print() function comes with a parameter called 'end'. By default, the value of this parameter is 'n', i.e. the new line character. You can end a print statement with any character/string using this parameter.

```python
# ends the output with a <space>
print("Welcome to" , end = ' ')
print("GeeksforGeeks", end = ' ')
```

### PEP8

- PEP stands for Python Enhancement Proposal. There are different types of PEP and the most useful one for beginners is the informational PEP
- PEPs of this kind typically describe commonly accepted guidelines or conventions about the language, so they can be very helpful. Besides PEP 8, which is an official style guide, another great PEP to look at is the Zen of Python.
- There is a document that is called PEP 8. 
- The key idea of it is to use the same code style for all Python projects as if they were written by the same programmer. This document guarantees that even a beginner will easily understand the code, written by any other developer.

### Specification
The function hello should return the word "hello"
### Buggy Python
def hello():
    return "hell"
### Error
Traceback (most recent call last):
  File "/app/test.py", line 1, in <module>
    from {module_name} import *
  File "/app/{module_name}.py", line 5, in <module>
    assert hello() == "hello"
AssertionError
### Explain Bug
According to the specification, the function should return the word "hello". However, the function returns the word "hell" instead. The function is missing the letter "o" at the end.
### Specification
{specification}
### Buggy Python
{program}
### Error
{error}
### Explain Bug
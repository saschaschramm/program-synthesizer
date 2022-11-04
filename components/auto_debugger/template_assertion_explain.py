### Specification
The function hello should return the word "hello"
### Buggy {module_name}.py
def hello():
    print("hell")
### Error
Traceback (most recent call last):
  File "/app/test.py", line 1, in <module>
    from {module_name} import *
  File "/app/{module_name}.py", line 5, in <module>
    assert hello() == "hello"
AssertionError
### Explain Bug
According to the specification, the function should return the word "hello". However, the function returns the word "hell" instead. The function is missing the letter "o" at the end.
### Fixed {module_name}.py
def hello():
    print("hello")
### Specification
{specification}
### Buggy {module_name}.py
{program}
### Error
{error}
### Explain Bug
{explanation}
### Fixed {module_name}.py
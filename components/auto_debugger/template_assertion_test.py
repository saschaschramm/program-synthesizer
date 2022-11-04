### Specification
The function hello should return the word "hello"
### Buggy {module_name}.py
def hello():
    print("hell")
### test.py
from {module_name} import *

assert hello() == "hello"
### Error
Traceback (most recent call last):
  File "/app/test.py", line 1, in <module>
    from {module_name} import *
  File "/app/{module_name}.py", line 5, in <module>
    assert hello() == "hello"
AssertionError
### Fixed {module_name}.py
def hello():
    print("hello")
### Specification
{specification}
### Buggy {module_name}.py
{program}
### test.py
{test}
### Error
{error}
### Fixed {module_name}.py
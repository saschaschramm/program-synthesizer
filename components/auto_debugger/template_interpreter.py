### Buggy {module_name}.py
def hello():
    print("hello"
### Error
Traceback (most recent call last):
  File "/app/test.py", line 1, in <module>
    from {module_name} import *
  File "/app/{module_name}.py", line 2
    print("hello"
         ^
SyntaxError: '(' was never closed
### Fixed {module_name}.py
def hello():
    print("hello")
### Buggy {module_name}.py
{program}
### Error
{error}
### Fixed {module_name}.py
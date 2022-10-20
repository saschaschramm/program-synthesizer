### Buggy Python
def hello():
    print("hello"
### SyntaxError: '(' was never closed
### Fixed Python
def hello():
    print("hello")
### Buggy Python
if __name__ == "__main__":
    foo()

def foo():
    return "foo"
### NameError: name 'foo' is not defined
### Fixed Python
def foo():
    return "foo"

if __name__ == "__main__":
    foo()
### Buggy Python
{program}
### {error}
### Fixed Python
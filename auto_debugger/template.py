## Fix errors in Python
### Buggy Python
def hello():
    """Print the word "hello"
    """
    print("hello"
### SyntaxError: '(' was never closed
### Fixed Python
def hello():
    """Print the word "hello"
    """
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
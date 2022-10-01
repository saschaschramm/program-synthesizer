### Buggy Python
def hello():
    print("hello"
### Fixed Python
def hello():
    print("hello")
### Buggy Python
if __name__ == "__main__":
    foo()

def foo():
    return "foo"
### Fixed Python
def foo():
    return "foo"

if __name__ == "__main__":
    foo()
### Buggy Python
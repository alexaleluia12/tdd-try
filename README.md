# tdd-try

## wear tdd in practical stuff from old code

Most of the code came from [Python for Informatics](http://www.pythonlearn.com/book.php)

Feel free to Contribute

> Require Python >= 3.3

#### Be sure `PYTHONPATH` is defined and have '..'
Posix
```sh 
$ export PYTHONPATH=$PYTHONPATH:..
```

Windows
```sh 
> set PYTHONPATH=%PYTHONPATH%;..
```

---
> Run all tests: 

```sh


/tdd-try/tests$ python3 -m unittest discover --pattern=*_test.py -v


```

## Why

For learn. To after wear TDD in real problems.
<br/>As all the start is quite difficult. And TDD is not different.
<br/>So I remake the programas tha I see in Python for Informatics
that wear Python 2.7 to Python 3.4.

And really wear TDD style (test first then implement the code).
<br/>To do this You need to know the interface of function/method.
```py

def functionX(argN):
    pass

```

On test explore the function and try to find a bug.

### What the test need

- be simple
- be faster

### Why You need test

- make sure the code is working
- refactoring functions without worried break things
- decouple
- (most awesome) see if new version of Python/library work on current code
- save time

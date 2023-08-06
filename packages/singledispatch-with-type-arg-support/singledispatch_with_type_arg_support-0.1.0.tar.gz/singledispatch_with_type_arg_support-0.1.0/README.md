# singledispatch-with-type-arg-support

Standalone "preview" of https://github.com/python/cpython/pull/100624

Requires a sufficiently recent Python 3.12 version (some tests fail with
earlier 3.12 versions and versions older than 3.12, although the main
functionality might still work - do your own testing).

## Example

See `example.py`:

```python
from singledispatch_with_type_arg_support import singledispatch

@singledispatch
def describe(x) -> str:
  raise TypeError(f"no description for {repr(x)}")

@describe.register
def describe(x: type[int]) -> str:
  return "the integer type"

print(describe(int))  # should print: the integer type
```

## License

Same as CPython (as 99% of it is copied from there), see `LICENSE` file.

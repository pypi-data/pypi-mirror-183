cfnv1a
======

fnv1a non-cryptographic hash function for python written in c.

Examples:

```python
from cfnv1a import fnv1a

print(fnv1a("Hello"))
# 7201466553693376363

print(fnv1a("Hello", prime=7, offset=1))
# 9972599733547454827
```

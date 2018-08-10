# Code Timer

### Overview

This is a simple one-off utility for timing how long code takes to run.

It is a wrapper around the standard Python `timeit` module.

### How to Use

```python
from timer import Timer

start = Timer.start()
# Your code goes here.
duration = Timer.stop(start)
print('Your code took {} seconds to run.'.format(duration))
```



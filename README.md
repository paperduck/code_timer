# Code Timer

### Overview

This is a simple utility for timing how long code takes to run.

It uses the standard Python module `timeit`.

### How to Use

Sample usage:

```python
from code_timer import CodeTimer

start = CodeTimer.start()
# Your code goes here.
duration = CodeTimer.stop(start)
print('Your code took {} seconds to run.'.format(duration))
```

Sample output:

```text
Your code took 0.54593290000048 seconds to run.
```



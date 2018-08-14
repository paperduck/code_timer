# Code Timer

### Overview

This is a simple utility for timing how long code takes to run.

It uses the standard Python module `timeit`.

### How to Use

Sample usage:

```python
from code_timer import CodeTimer

CodeTimer.start()
# Your code goes here.
duration = CodeTimer.stop()
print('Your code took {} seconds to run.'.format(duration))
```

Sample output:

```text
Your code took 0.00593290000048 seconds to run.
```



from code_timer import CodeTimer

start = CodeTimer.start()
for i in range(1000):
    print('.', end='')
print()
duration = CodeTimer.stop(start)
print('Your code took {} seconds to run.'.format(duration))

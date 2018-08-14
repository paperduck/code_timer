from code_timer import CodeTimer

CodeTimer.start()
for i in range(1000):
    print('.', end='')
print()
duration = CodeTimer.stop()
print('Your code took {} seconds to run.'.format(duration))

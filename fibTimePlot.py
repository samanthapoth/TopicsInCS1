from fib import fib, timer, times

fib(100)

import matplotlib.pyplot as plt

temp = times[0]
times [0] = times[1]
times[1] = temp

plt.plot(times)
plt.ylabel('Time in seconds')
plt.xlabel('fib(x)')
plt.title('Fibonacci Function Calls')
plt.show()

from fib import fib, timer, times


fib(100)

import matplotlib.pyplot as plt
plt.plot(times)
plt.ylabel('Time in seconds')
plt.xlabel('fib(x)')
plt.title('Fibonacci Function Calls')
plt.show()

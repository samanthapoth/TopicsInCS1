from fib import fib, timer, times

fib(100)

import matplotlib.pyplot as plt

# swap the first two elements of the array so that the first point plotted is fib(0) and the second is fib(1)
temp = times[0]
times [0] = times[1]
times[1] = temp

#plot the times array
plt.plot(times)
plt.ylabel('Time in seconds')
plt.xlabel('fib(x)')
plt.title('Fibonacci Function Call Times')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# y(t) = 5x(t)

# LINEARNOST
t = np.linspace(0, 10, 1000)

a = 2
b = 3

x1 = np.heaviside(t-1, 1)
x2 = t * np.heaviside(t-2, 1)

y1 = 5*x1
y2 = 5*x2

x3 = 5*(a*x1 + b*x2)
x4 = a*y1 + b*y2

plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.ylabel("$x_1(t)$")
plt.xlabel("t(s)")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, x2)
plt.ylabel("$x_2(t)$")
plt.xlabel("t(s)")
plt.grid()

plt.figure(2)

plt.subplot(2, 1, 1)
plt.plot(t, x3, 'r')
plt.ylabel("$x_3(t)$")
plt.xlabel("t(s)")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, x4, 'r')
plt.ylabel("$x_4(t)$")
plt.xlabel("t(s)")
plt.grid()

# VREMENSKA INVARIJANTNOST
t0 = 2
x = t*np.heaviside(t-2, 1)
x_t0 = (t-t0) * np.heaviside(t-2-t0, 1)     # zakasnimo ulazni signal x(t)
y1 = 5 * x_t0                               # sistem

y = 5 * x                                   # sistem
y2 = 5 * (t-t0) * np.heaviside(t-2-t0, 1)   # zakasnimo izlazni signal

plt.figure(3)

plt.subplot(2, 1, 1)
plt.plot(t, y1, 'g')
plt.ylabel('y1(t)')
plt.xlabel('t(s)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, y2, 'g')
plt.ylabel('y2(t)')
plt.xlabel('t(s)')
plt.grid()

# STABILNOST
t = np.linspace(0, 10, 1000)

x1 = np.heaviside(t-1, 1)       # ogranicen signal
x2 = t * np.heaviside(t-2, 1)   # neogranicen signal

y1 = 5*x1
y2 = 5*x2

plt.figure(4)

plt.subplot(4, 1, 1)
plt.plot(t, x1)
plt.ylabel('$x_1(t)$')
plt.xlabel('t(s)')
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, y1)
plt.ylabel('$y_1(t)$')
plt.xlabel('t(s)')
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, x2)
plt.ylabel('$x_2(t)$')
plt.xlabel('t(s)')
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, y2)
plt.ylabel('$y_2(t)$')
plt.xlabel('t(s)')
plt.grid()

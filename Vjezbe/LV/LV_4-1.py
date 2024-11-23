import numpy as np
import matplotlib.pyplot as plt

# a)
n = np.arange(-10, 11, 1)
y = np.exp(n)

fig, ax = plt.subplots(2, 2)

plt.subplot(2, 2, 1)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n]=e^n')
plt.title('a) signal x[n]=e^n')
plt.stem(n, y)

# b)
n_invert = n[::-1]
y = np.exp(n_invert)

plt.subplot(2, 2, 2)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n]=e^-n')
plt.title('b) invertovani signal, x[n]=e^-n')
plt.stem(n, y)

# c)
pomak = 2
x = np.exp(n)
x_pomak = np.roll(x, pomak)
x_pomak[0:pomak] = 0

plt.subplot(2, 2, 3)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n-2]=e^(n-2)')
plt.title('c) zakasnjen orginalni signal za 2 uzorka')
plt.stem(n, x_pomak)

# d)
pomak = -2
x = np.exp(n)
x_pomak = np.roll(x, pomak)

plt.subplot(2, 2, 4)
plt.grid()
plt.xlabel('n')
plt.ylabel('x[n+2]=e^(n+2)')
plt.title('d) prednjacen orginalni signal za 2 uzorka')
plt.stem(n, x_pomak)

plot_offset_v = 0.6
plot_offset_h = plot_offset_v

fig.tight_layout()
plt.subplots_adjust(left=-plot_offset_h, right=plot_offset_h, top=plot_offset_v, bottom=-plot_offset_v)
plt.show()

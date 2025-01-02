import numpy as np
import sympy
import zplane
import scipy.signal

b = np.array([0,1])
a = np.array([3, -4,1])

print (scipy.signal. residuez (b,a)) # za odre ivanje polova pri rastavljanju datog izraza

zplane (a, b)

b = np.array([0, 1,3])
a = np.array([1, -3.25,0.75])

print(scipy.signal.residuez(b, a))

zplane(a, b)
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal

fs = 56.32e6


freqset = np.array(
  [
    [1.0e6, 2.0e6, 80],
    [3.0e6, 4.0e6, 90],
  ]
)

config = {
  "numtaps":    2000,
  "freq":  [0.0,  .1,   .2,  .3,  .4, .5, 1.0],
  "gain":  [0.0, 1.0,  1.0, 0.0, 0.0, 1.0, 0.0],
  "window":  "hamming"
}
b = signal.firwin2(**config)

w, h = signal.freqz(b)


fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)


plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')


ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()


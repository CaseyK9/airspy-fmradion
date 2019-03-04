#!/usr/bin/env python3
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

b = [
-98.82658218405535420E-6,
-159.1554002742769000E-6,
 151.8984722741540740E-6,
 601.9731255161444780E-6,
 227.2403666332392620E-6,
-0.001127653945291543,
-0.001517402890273692,
 841.6884318159969780E-6,
 0.003577806684766531,
 0.001590457251629624,
-0.004840113972003346,
-0.006744268452659899,
 0.002327004269405600,
 0.012742073437974451,
 0.006743902938867469,
-0.014379589003609588,
-0.022105703632783531,
 0.004266214793638143,
 0.037867709391767625,
 0.024544619738892614,
-0.041241969417288381,
-0.078912658527988303,
 0.005682847341595135,
 0.201030055303318772,
 0.368904771130160847,
 0.368904771130160847,
 0.201030055303318772,
 0.005682847341595135,
-0.078912658527988303,
-0.041241969417288381,
 0.024544619738892614,
 0.037867709391767625,
 0.004266214793638143,
-0.022105703632783531,
-0.014379589003609588,
 0.006743902938867469,
 0.012742073437974451,
 0.002327004269405600,
-0.006744268452659899,
-0.004840113972003346,
 0.001590457251629624,
 0.003577806684766531,
 841.6884318159969780E-6,
-0.001517402890273692,
-0.001127653945291543,
 227.2403666332392620E-6,
 601.9731255161444780E-6,
 151.8984722741540740E-6,
-159.1554002742769000E-6,
-98.82658218405535420E-6
]

w, h = signal.freqz(b)
fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [rad/sample]')
plt.show()
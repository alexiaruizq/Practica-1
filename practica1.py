#import sys 
#sys.path.insert(1,'dsp-modulo')
from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

#modulo para mostrar las graficas 
import matplotlib.pyplot as plt 

#crear señal senoidal

seno = SinSignal(freq=200, amp=0.7, offset=0)
coseno = CosSignal(freq=800, amp=1.1, offset=0)


#creamos grafica y asignamos propiedades
seno.plot()
coseno.plot()

decorate(xlabel='Tiempo (s)')
decorate(ylabel='Amplitud')

plt.show()
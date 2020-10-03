from biosppy import storage
from biosppy.signals import ecg


# load raw ECG signal
signal, mdata = storage.load_txt('examples/ecg.txt')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)
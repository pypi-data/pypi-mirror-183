import numpy as np
from scipy.interpolate import interp1d

from evofond.utils import hms_to_s


class Hydrograph:
    def __init__(self):
        
        self._title = "new hydrograph"
        
        self._times_discharges = [(0, 1), (1, 1)]
        
    def from_lavabre(self, duration, discharge_max, discharge_min, peak, order, dt=(0, 0, 1)):
        duration = hms_to_s(duration)
        peak = hms_to_s(peak)
        dt = hms_to_s(dt)
        
        if not duration or not peak or not dt:
            return False
        
        if not dt < duration:
            return False
        
        if not isinstance(discharge_max, (int, float)) or not isinstance(discharge_min, (int, float)) or not isinstance(order, int):
            return False

        if not 0 <= discharge_min <= discharge_max:
            return False
        
        if not 0 <= order:
            return False
        
        times = np.arange(0, duration, dt)
        if duration not in times:
            times = np.append(times, duration)
            
        discharges = (times / peak)**order
        discharges *= 2
        discharges /= 1 + (times / peak)**(2*order)
        discharges *= discharge_max - discharge_min
        discharges += discharge_min
        
        times_discharges = [(t, q) for t, q in zip(times, discharges)]
        
        self._times_discharges = times_discharges
        return True
        
    def from_txt(self, filename, time_fields="t", discharge_field="Q", delimiter="\t", decimal=".", time_unit="second", discharge_unit="m3/s"):
        if not isinstance(filename, str) or not isinstance(time_field, str) or not isinstance(discharge_field, str):
            return False
        
        if delimiter not in [' ', '\t', ';', ','] or decimal not in ['.', ','] or time_unit not in ['second', 'minute', 'hour'] or discharge_unit not in ['m3/s']:
            return False
        
        try:
            data = pd.read_csv(filename,
                               delimiter=delimiter,
                               decimal=decimal,
                               skiprows=0,
                               encoding="utf-8")
            
        except:
            return False
        
        if data.shape[0] < 2 or data.shape[1] < 2:
            return False
        
        if time_field not in list(data.columns) or discharge_field not in list(data.columns):
            return False
        
        if data.loc[:, time_field].dtype not in ['float64', 'int64'] or \
           data.loc[:, discharge_field].dtype not in ['float64', 'int64']:
            return False
        
        data = data.dropna()
        
        i = list(data.columns).index(time_field)
        times = list(data.values[:, i])
        
        i = list(data.columns).index(discharge_field)
        discharges = list(data.values[:, i])
        
        if time_unit == "second":
            to_second = 1.
        elif time_unit == "minute":
            to_second = 60.
        else:
            to_second = 3600.
            
        if discharge_unit == "m3/s":
            to_cubic_meter_per_second = 1.
        
        times_discharges = [(t*to_second, q*to_cubic_meter_per_second) for t, q in zip(times, discharges)]
        
        times_discharges.sort()
        t = np.array([t for t, q in times_discharges])
        q = np.array([q for t, q in times_discharges])
        
        dt =  t[1:] - t[:-1]
        
        if 0 in dt or len(t[t<0]) > 0 or len(q[q<0]) > 0:
            return False
        
        self._times_discharges = times_discharges
        return True
    
    def get_discharge_at(time):       
        t = hms_to_s(time)
        
        if not t:
            return
        
        if not min(self.times) <= t <= max(self.times):
            return
            
        times = self.times
        times.append(t)
        times.sort()
        i = times.index(t)
        
        if t == times[0]:
            return float(self.discharges[0])
        elif t == times[-1]:
            return float(self.discharges[-1])
        else:
            f = inter1d(self.times[i-1:i+1], self.discharges[i-1,i+1], kind='linear')
            return float(f(t))
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
            
    @property
    def times_discharges(self):
        return list(self._times_discharges)
        
    @property
    def times(self):
        return [t for t, q in self._times_discharges]
        
    @property
    def discharges(self):
        return [q for t, q in self._times_discharges]
    
    def __repr__(self):
        return self._title

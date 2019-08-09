import seeed_sgp30
from grove.i2c import Bus

sgp30 = seeed_sgp30.grove_sgp30(Bus())
data = sgp30.read_measurements()
co2_eq_ppm, tvoc_ppb = reading.data
print("\r  tVOC = {} ppb CO2eq = {} ppm elapse = {:8.2f}S ".format(
                             tvoc_ppb, co2_eq_ppm, elapse))
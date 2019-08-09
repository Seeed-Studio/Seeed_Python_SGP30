import seeed_sgp30
from grove.i2c import Bus

sgp30 = seeed_sgp30.grove_sgp30(Bus())
while True:
  data = sgp30.read_measurements()
  co2_eq_ppm, tvoc_ppb = data.data
  print("\r  tVOC = {} ppb CO2eq = {}  ".format(
                               tvoc_ppb, co2_eq_ppm))

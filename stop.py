import dvb

stop = 'Albert Platz'
time_offset = 0
num_results = 10
city = 'Dresden'

res = dvb.monitor(stop, time_offset, num_results, city)

for hs in res:
    print(f"{hs['line']:2} {hs['direction']:15} in {hs['arrival']//60} h {hs['arrival']%60} min")

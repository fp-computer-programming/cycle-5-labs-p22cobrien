# Author: CMOB 10/25/2021

import math
import time

# math.pow
start_time = time.perf_counter()

(2 ** 3)

end_time = time.perf_counter()

final_time_1 = (end_time - start_time)

print(final_time_1)

# ** op
start_time_1 = time.perf_counter()

(math.pow(2, 3))

end_time_1 = time.perf_counter()

final_time_2 = end_time_1 - start_time_1

print(final_time_2)

# difference
print(final_time_1 - final_time_2)

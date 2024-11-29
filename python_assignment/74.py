import time
start_time = time.time()
for i in range(1000000):
    pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

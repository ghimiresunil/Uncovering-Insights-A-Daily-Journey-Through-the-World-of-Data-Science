import atexit
from time import sleep

@atexit.register
def final_function():
    print("EXECUTION COMPLETED!")
    
for i in range(10):
    print(f"num = {i}")

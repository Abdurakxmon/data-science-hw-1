import time 

def decorator_1(f):
    def solve(*args, **kwargs):
        start = time.time()
        ans = f(*args, **kwargs)
        print(f"func call executed in {round(time.time()-start, 6)} sec")
        return ans
    return solve

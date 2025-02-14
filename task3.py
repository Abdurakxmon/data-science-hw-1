import time 

def decorator_1(f):
    def solve(**kwargs):
        start = time.time()
        ans = f(**kwargs)
        print(f"func call executed in {round(time.time()-start, 6)} sec")
        return ans
    return solve

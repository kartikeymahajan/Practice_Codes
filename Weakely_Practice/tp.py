def func(f,t):
    if f <= t:
        k = f*f
        print(k)
        func(f+1,t)
func(1,10)
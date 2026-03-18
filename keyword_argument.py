# 1). basic keyword arguments

def simple_interest(p:float,t:float,r:float):
    si = (p * t * r) / 100
    print("simple interest : ",si)

simple_interest(p=1000,t=2,r=3)


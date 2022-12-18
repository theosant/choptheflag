import threading as th
import time

def fun1(flag):
    while True:
        flag.Wait()
        print("peguei a bandeira")
        flag.Resolve()
        time.sleep(0.25)
def fun2(flag):
    while True:
        flag.Wait()
        print("Não, eu peguei a bandeira")
        flag.Resolve()
        time.sleep(0.25)
if __name__ == "__main__":
    flag = Flag(1,1)
    t = th.Thread(target = fun1, args=[flag])
    t.start()
    t2 = th.Thread(target = fun2,  args=[flag])
    t2.start()
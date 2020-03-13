import time


class Secundomer:
    def __init__(self, num_runs):
        self.num_runs = num_runs
       
    def __call__(self, func):
        self.func = func
        def wrap():
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                ### <<полезный>> код
                self.func()

                t1 = time.time()
                avg_time += (t1 - t0)
            print("Время исполнения функции:", avg_time/self.num_runs)
        return wrap


    


@Secundomer(10)
def fibo():
    num1 = 1
    num2 = 2
    print(num1)
    print(num2)
    sum_fibo = 0
    while num2 < 4000000000000:
        
        num = num2
        num2 = num2 + num1
        num1 = num
        if num2 % 2 == 0:
            sum_fibo += num2
        if num2 >= 4000000000000:
            break
        print(num2)
    print("Сумма чётных ", sum_fibo + 2)
fibo()

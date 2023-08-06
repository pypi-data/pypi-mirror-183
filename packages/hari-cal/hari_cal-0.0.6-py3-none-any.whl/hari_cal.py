
def cal():
    
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def div(a,b):
        return a / b

    while True:
        optios = """

            1. add
            2. sub
            3. mul
            4. div
            5. stop
        
            """
        print(optios)
        user = int(input("enter ur choice :"))
        if user == 5:
            print("u came out of loop and if u want to run call cal() fun onemore time.")
            break
        a = float(input("enter a value: "))
        b = float(input("enter b value: "))
        d = {1:"add", 2:"sub", 3:"mul", 4:"div", 5:"stop"}
        if user == 1:
            data = add(a,b)
            print(f"The value of a is {a}, the value of b is {b}, ur choose {d[user]}, result is {data}")
        elif user == 2:
            data = sub(a,b)
            print(f"The value of a is {a}, the value of b is {b}, ur choose {d[user]}, result is {data}")
        elif user == 3:
            data = mul(a,b)
            print(f"The value of a is {a}, the value of b is {b}, ur choose {d[user]}, result is {data}")
        elif user == 4:
            data = div(a,b)
            print(f"The value of a is {a}, the value of b is {b}, ur choose {d[user]}, result is {data}")
        # elif user == 5:
        #     print("u came out of loop and if u want to run call cal() fun onemore time.")
        #     break
            

# cal()
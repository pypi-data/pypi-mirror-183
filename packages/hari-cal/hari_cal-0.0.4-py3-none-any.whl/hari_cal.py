def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def cal():
   


    a = float(input("enter a value: "))
    b = float(input("enter b value: "))
   
    while True:
        try:
            optios = """

            1. add
            2. sub
            3. mul
            4. div
            5. stop
        
            """
            print(optios)
            user = int(input("enter ur num :"))
            if user == 1:
                data = add(a,b)
                print(data)
            elif user == 2:
                data = sub(a,b)
                print(data)
            elif user == 3:
                data = mul(a,b)
                print(data)
            elif user == 4:
                data = div(a,b)
                print(data)
            elif user == 5:
                break
        except Exception as e:
            raise e

# cal()
# Your code here!!
def sing():
    coro1="let it be"
    coro2="whisper words of wisdom,"
    coro3="there will be an answer,"
    for i in range(9):
        if i < 4:
            print(coro1+",")
        elif i ==4:
            print(coro2+" "+coro1+", "+coro1+", ")
        elif i<8:
            print(coro1+",")
        else:
           print(coro3+" "+coro1) 

sing()      






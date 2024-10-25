def myfunction1(n):
    if n <= 0:  # Corrected condition for base case
        return
    for i in range(0, n+1):
        print("Codingal")
    myfunction1(n // 2)  # Use integer division to prevent infinite recursion
    myfunction1(n // 3)

def myfunction2(n):
    if n <= 1:
        return
    print("Coding")
    myfunction2(n - 1)

myfunction1(10)
myfunction2(20)
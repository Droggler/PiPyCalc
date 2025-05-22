
def comp(decimals : int):
    with open("calcpi.txt", "r") as file:
        calc_pi = file.read()
    with open("pi.txt", "r") as file:
        pi = file.read()
    
    index = 1
    wrong = False
    for mydigit, digit in zip(calc_pi, pi):
        if index >= decimals:
            break
        index += 1
        if mydigit != digit:
            wrong = True
            print("Wrong digit of pi! ", index)
            break
    if wrong == False:
        print("Every digit is correct!")
        
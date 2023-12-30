import string


with open("message.txt") as m:
    o = m.read()
    
    letters = string.ascii_uppercase
    digits = string.digits
    down = "_"
    
    flag = ""
    
    out = [int (val) for val in o.split()]
    for i in out:
        
        target = pow(i,-1,41)
        
        if (target >= 1 and target <= 26):
            flag += letters[target - 1]
        
        elif (target >= 27 and target <= 36):
            flag += digits[target - 27]
        elif (target == 37):
            flag += down
    print(flag)

    # picoCTF{1NV3R53LY_H4RD_DADAACAA}
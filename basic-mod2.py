import string


with open("message.txt") as m:
    o = m.read()
    
    letters = string.ascii_uppercase        # Importing from A to Z but only in uppercase
    digits = string.digits                   # Importing from 0 to 9
    down = "_"
    
    flag = ""
    
    out = [int (val) for val in o.split()]
    for i in out:
        
        target = pow(i,-1,41)    # Taking the modular inverse with 41.
        
        if (target >= 1 and target <= 26):    # Sorting - alphabets
            flag += letters[target - 1]
        
        elif (target >= 27 and target <= 36):   # Sorting - decimal numebers
            flag += digits[target - 27]
        elif (target == 37):                    # Sorting - an underscore
            flag += down
    print(flag)                                # The output will look like `1NV3R53LY_H4RD_DADAACAA`, which is the decrypted_message.

    # picoCTF{1NV3R53LY_H4RD_DADAACAA}          # picoCTF flag format (i.e. picoCTF{decrypted_message})

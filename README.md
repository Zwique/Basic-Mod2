# basic-mod2
picoCTF 2022 Cryptography Challenge

<img width="714" alt="Screenshot 2023-12-30 at 14 16 02" src="https://github.com/Zwique/basic-mod2/assets/97537483/f03b07f2-6da3-4351-a3c0-0ea999f242b6">

1. Looks like we need to decrypt the given text.
2. Luckily, the challenge involved sorting representations of numbers after applying the inverse modular operation with 41.
## Inverse Modular

Lets consider first number from the given file - `432.`

The equation  `(x * 432) mod 41 = 1` simply describes the whole process behind the Inverse Modular.
Where `x` is the result of taking `modular inverse.`

Python pow() function will help us to figure out this equation.
```sh 
print(pow(432,-1,41))
```
` x = 28 YeeY!!!`

## Details of sectors
1. 1-26 are the alphabet
* 1 -> A
* 2 -> B
* ...
* 26 -> Z
  
2. 27-36 are the decimal digits
* 27 -> 0
* 28 -> 1
* ...
* 36 -> 9

4. 37 is an underscore
* 37 -> _

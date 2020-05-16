#Morse_code-enigma #using python3 #concept of dictionary

Encrypt_Morse = {
    "a":".-","b":"-...","c":"-.-.","d":"-..","e":".",
    "f":"..-.","g":"--.","h":"....","i":"..","j":".---",
    "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.",
    "q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-",
    "w":".--","x":"-..-","y":"-.--","z":"--.."," ":"/"
}

Decrypt_Morse = {
    ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
    "..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
    "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P",
    "--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",
    ".--":"W","-..-":"X","-.--":"Y","--..":"Z","/":" ","~":""
}

print("MORSE-ENGIMA")

inp = input("Choose an operation Encryption(1) Decryption(2):\n")

if(inp == "1"):
    print("Entering Encryption procedure")
    cip = input ("Select your secret delimiter: ")
    if(cip == ""):
        print("Failed to enter delimiter lead to termination")
        exit
    else:
        text = input("Enter message to be encrypted:\n")
        ec = list(text)
        for i in ec:
            print(Encrypt_Morse.get(i), end=cip)
        print("\nEncryption successfull!")

elif (inp == "2"):
    def decodeMorse(morseCode):
            for item in morseCode.split(keysp):
                print  (Decrypt_Morse.get(item), end="")
    print("Entering Decryption procedure...")
    keysp = input("Enter the secret delimiter: ")
    if (keysp == ""):
        print("Failed to enter delimiter lead to termination")
        exit
    else:
        morseCode = input("Insert Morse Code: \n")
        decodeMorse(morseCode)
        print("\nDecryption successfull!")
else:
    print("Invalid input ---> Program Terminated")

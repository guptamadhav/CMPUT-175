letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
letters = letters.split()
def getInputFile(file = ""):
    """
    args: file -> file name
    return : file name with .txt extension
    """
    while file[-4:] != ".txt":
        file = input("Invalid filename extension. Please re-enter the input filename: ")
    return file

def decrypt(code, i):
    """
    args: code -> string of characters that need to be decrypted
          i -> code letters ahead of their original index by i
    return: decrypted code
    """
    code = code.lower()
    decrypt_code = ""
    for j in range(len(code)):
        if code[j] == " " and code[j-1]!=" ":
            decrypt_code += " "
        elif code[j]!=" ":
            decrypt_code += letters[letters.index(code[j])-i]
    return decrypt_code
file = input("Enter name of the file: ")
file_n = getInputFile(file)
try:
    with open(f"Lab 2/{file_n}", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("File not found")
    exit()
i = int(data[0])
code = data[1].strip()

decrypt_code = decrypt(code, i)
print(decrypt_code)
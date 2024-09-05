def reverse_string(s):
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string
 
string = input("Informe a string: ")
print(f"String invertida: {reverse_string(string)}")

# letter = chr(ord('A') +2)
# print(letter)


message =  "Mon message très malin "
result = ' '


for i in message:
    result += chr(ord(i) +2)
    
print(result)


# def codeCaesar(message, result):
#     for i in message:
#         result += chr(ord(i) +2)
#     return result

# def messageDecodage(message, result, decodage):
#     for i in result:
#         decodage += chr(ord(i)+2)
#     return decodage

# decodage = ' '

# print(codeCaesar(result))
# print(messageDecodage(decodage))
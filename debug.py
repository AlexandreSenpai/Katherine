path = "vídeos"
file_name = ""
for i in path:
        if i in 'áíóéõãàìòè':
            i = i.replace(i, '')
        file_name += i

print(file_name)
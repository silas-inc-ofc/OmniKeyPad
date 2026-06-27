Configurations = []

for i in range(17):
    for j in range(17):
        
            
        Configurations.append((i,j))
        


print(Configurations)



print(len(Configurations))


for i in range(289):
    with open(f'Emojikeypad E{1058+i}.py','r',encoding='utf-8') as file:
        data = file.readlines()
#'tk.Label(hdr,text="⌨  Emojikeypad Extension {i+61}",\n
    print(data)
    data[19] = f'eyes0 = eyes_batched[{Configurations[i][0]}]\n'
    data[20] = f'eyes1 = eyes_batched[{Configurations[i][1]}]\n'

    data[241]=f'        self.title("Emojikeypad E{1058+i}")\n'
    line = data[267]
    new_line = line.replace('1058',f'{1058+i}')
    data[267]= new_line
    print(data)



    with open(f'Emojikeypad E{1058+i}.py','w',encoding='utf-8') as file:
        file.writelines(data)

        




    
        
print('complete')





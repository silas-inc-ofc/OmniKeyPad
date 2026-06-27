import shutil


for i in range(289):
    with open(f'Emojikeypad E{1058+i}.py','x') as file:
        pass


for i in range(289):

    shutil.copyfile('essential/Emojikeypad E1058.py',f'Emojikeypad E{1058+i}.py')
    print('done')

print('complete')




        

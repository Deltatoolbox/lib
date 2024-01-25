import os

name = 'D'
counter = 0
c = 0

while (1):
    counter = counter + 1

    if os.path.exists(f"{name}:\\"):
        x = 1

    else:
        c = 1

    if x == counter:
        name = 'E'
        x = 0

    if counter == 1000:
        counter = 2

    if x == 1 and c == 1:
        os.system(f'copy C:\\Users\\Zweistein\\Desktop\\Python\\Test\\Bekeldef.py {name}:\\')
        x == 0
        c = 0
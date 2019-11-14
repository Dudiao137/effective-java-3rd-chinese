import os

path = './src'

for file in os.listdir(path) :
    new_name = file.replace("%20", "")
    os.rename(os.path.join(path, file), os.path.join(path, new_name))


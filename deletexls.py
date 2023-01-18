import os

path = 'C:\\Users\\abdur\\OneDrive\\Dokumen\\UG\\Pengantar Sain Data\\project\\'
for filename in os.listdir(path):
    if filename.endswith('.xls'):
        new_file = os.path.splitext(filename)[0]
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_file)
        os.rename(old_file, new_file)
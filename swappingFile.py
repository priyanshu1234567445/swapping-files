def swappingFile():
    file1=input("enter file name 1")
    file2=input("enter file name 2")
    with open(file1, 'r') as a :
        data_A = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a :
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_A)    

swappingFile()          
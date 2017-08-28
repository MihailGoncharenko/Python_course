import  os
import glob
files = []
current_dir = os.getcwd()
#print (os.listdir('Migrations'))
migrations = 'Migrations'
os.chdir(migrations)

def firstloop():
    print("Введите строку:")
    string = input()
    q = 0
    for infile in glob.glob("*.sql"):
        with open(infile, 'r') as infile:
            content = infile.read()
            if string in content:
                q = q + 1
                name = str(infile)
                name = name.split('\'')
                print(name[1])
                templist = [name[1]]
                files.extend(templist)
    print("Всего:", end=' ')
    print(q)
    endlessloop()
def endlessloop():
    print("Введите строку:")
    string = input()
    q = 0
    tempfiles = []
    for sql in files:
        for infile in glob.glob(sql):
            with open(infile, 'r') as infile:
                content = infile.read()
                if string in content:
                    q = q + 1
                    name = str(infile)
                    name = name.split('\'')
                    print(name[1])
                    templist = [name[1]]
                    tempfiles.extend(templist)
    print("Всего:", end=' ')
    print(q)
    files.clear()
    files.extend(tempfiles)
    endlessloop()
firstloop()

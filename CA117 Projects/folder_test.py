from folder_1111 import File, Folder

def main():

    # Create an empty folder
    print('Initialise empty folder...')
    folder = Folder()

    # Create some files
    print('Initialise some files...')
    f1 = File('poem.txt', 'joe')
    f2 = File('readme.txt', 'max', 1000, 'r')
    f3 = File('secret.txt', 'fred', 100, 'rw')
    f4 = File('exam.txt', 'jim', 3000, 'x')

    # Add files to the folder
    print('Add files to folder...')
    folder.add_file(f1)
    folder.add_file(f2)
    folder.add_file(f3)
    folder.add_file(f4)

    # Try adding same file twice
    print('Add existing file to folder...')
    folder.add_file(f1)

    # Display folder contents
    print('Display folder contents...')
    print(folder)

    # Max tries to delete a file
    print('Max deletes a file...')
    folder.del_file('max', 'readme.txt')

    # Max tries to delete a file
    print('Max deletes a file...')
    folder.del_file('max', 'readme.txt')

    # Joe tries to delete a file
    print('Joe deletes a file...')
    folder.del_file('joe', 'secret.txt')

    # Display folder contents
    print('Display folder contents...')
    print(folder)

if __name__ == '__main__':
    main()

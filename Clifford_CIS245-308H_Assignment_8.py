import os

def main():
    directory = input("Enter the directory that you want to save the file to: ")
    filename = input("Enter the filename: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")
    #Check to see if the directory exists
    if os.path.isdir(directory):
        #create and open the file to write
        writeFile= open(os.path.join(directory,filename), 'w')
        #Make sure data is comma seperated
        writeFile.write(name+', '+address+', '+phone_number+' \n')
        #close file after
        writeFile.close()

        print("File contents: ")
        #make sure it stored the info
        readFile = open(os.path.join(directory,filename), 'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry that directory does not exist.")
main()
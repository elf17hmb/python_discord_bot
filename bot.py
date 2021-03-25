import commands

def main():
    f = open('secrete.txt','r')
    commands.client.run(f.readline())


if __name__ == '__main__':
    main()  


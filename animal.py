import sys

def dog():
    print('Baw')

def cat():
    print('Meow')

def default():
    print('Hello')

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'dog':
        dog()
    if len(sys.argv) > 1 and sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()


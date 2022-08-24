import os

FORMATS = {
    'img': ['png', 'jpg', 'jpeg'],
    'video': ['mp4'],
    'doc': ['doc', 'docx', 'pptx', 'xlxs', 'pdf', 'html'],
    'audio': ['mp3', 'wav'],
    'misc': [],
    'compressed': ['zip', 'rar']
}


def main():
    run = True
    path = ''

    while run:
        path = input('Input full path of folder (cd for current directory): ')
        sort_mode = input(
            'Input sort mode (1: type, format; 2: type, 3: format, 4: reset) : ')

        if path == 'cd':
            files = os.listdir()
        else:
            files = os.listdir(path)

        for file in files:
            print(file)

        cont = input('Continue? (y, n): ')
        if cont == 'n':
            run = False


main()

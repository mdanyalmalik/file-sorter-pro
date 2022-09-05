import os
import pathlib

FORMATS = {
    'img': ['png', 'jpg', 'jpeg'],
    'video': ['mp4'],
    'doc': ['doc', 'docx', 'pptx', 'xlxs', 'pdf', 'html'],
    'audio': ['mp3', 'wav'],
    'compressed': ['zip', 'rar']
}


def mode_1(path):  # type, format
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        ext = os.path.splitext(file)[1][1:]

        for type, exts in FORMATS.items():
            if ext in exts:
                os.makedirs(os.path.join(path, type))
                os.makedirs(os.path.join(path, type, ext))
                os.rename(os.path.join(path, file),
                          os.path.join(path, type, ext, file))


def mode_2(path):  # type
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        ext = os.path.splitext(file)[1][1:]

        for type, exts in FORMATS.items():
            if ext in exts:
                os.makedirs(os.path.join(path, type))
                os.rename(os.path.join(path, file),
                          os.path.join(path, type, file))


def mode_3(path):
    pass


def mode_4(path):
    pass


if __name__ == '__main__':
    run = True

    while run:
        path = input('Input full path of folder (cd for current directory): ')
        sort_mode = input(
            'Input sort mode (1: type, format; 2: type, 3: format, 4: reset) : ')

        if int(sort_mode) == 1:
            mode_1(path)
        elif int(sort_mode) == 2:
            mode_2(path)
        elif int(sort_mode) == 3:
            mode_3(path)
        elif int(sort_mode) == 4:
            mode_4(path)

        cont = input('Continue? (y, n): ')
        if cont == 'n':
            run = False

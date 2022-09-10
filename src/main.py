import os
import pathlib

FORMATS = {
    'images': ['png', 'jpg', 'jpeg'],
    'videos': ['mp4'],
    'documents': ['doc', 'docx', 'pptx', 'xlxs', 'pdf', 'html'],
    'audio': ['mp3', 'wav'],
    'compressed': ['zip', 'rar']
}


def add_format(type, format):
    format_list = FORMATS[type]
    format_list.append(format)
    FORMATS[type] = format_list


def add_type(type):
    FORMATS.update({type: []})


def mode_1(path):  # type, format
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            if not os.path.isdir(os.path.join(path, 'folders')):
                os.makedirs(os.path.join(path, 'folders'))

            os.rename(os.path.join(path, file),
                      os.path.join(path, 'folders', file))
        else:
            ext = os.path.splitext(file)[1][1:]

            for type, exts in FORMATS.items():
                if ext in exts:
                    if not os.path.isdir(os.path.join(path, type)):
                        os.makedirs(os.path.join(path, type))
                    if not os.path.isdir(os.path.join(path, type, ext)):
                        os.makedirs(os.path.join(path, type, ext))

                    os.rename(os.path.join(path, file),
                              os.path.join(path, type, ext, file))


def mode_2(path):  # type
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            if not os.path.isdir(os.path.join(path, 'folders')):
                os.makedirs(os.path.join(path, 'folders'))

            os.rename(os.path.join(path, file),
                      os.path.join(path, 'folders', file))
        else:
            ext = os.path.splitext(file)[1][1:]

            for type, exts in FORMATS.items():
                if ext in exts:
                    if not os.path.isdir(os.path.join(path, type)):
                        os.makedirs(os.path.join(path, type))
                    os.rename(os.path.join(path, file),
                              os.path.join(path, type, file))


def mode_3(path):  # format
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            if not os.path.isdir(os.path.join(path, 'folders')):
                os.makedirs(os.path.join(path, 'folders'))

            os.rename(os.path.join(path, file),
                      os.path.join(path, 'folders', file))
        else:
            ext = os.path.splitext(file)[1][1:]

            for type, exts in FORMATS.items():
                if ext in exts:
                    if not os.path.isdir(os.path.join(path, ext)):
                        os.makedirs(os.path.join(path, ext))
                    os.rename(os.path.join(path, file),
                              os.path.join(path, ext, file))


def mode_4(path):  # reset
    if path == 'cd':
        path = pathlib.Path().resolve()
    files = os.listdir(path)

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            for type, exts in FORMATS.items():
                if file in exts:
                    inner_files = os.listdir(os.path.join(path, file))
                    for inner_file in inner_files:
                        os.rename(os.path.join(path, file, inner_file),
                                  os.path.join(path, inner_file))
                    os.rmdir(os.path.join(path, file))
                elif file == type:
                    inner_files = os.listdir(os.path.join(path, file))
                    for inner_file in inner_files:
                        if not os.path.isdir(os.path.join(path, file, inner_file)):
                            os.rename(os.path.join(path, file, inner_file),
                                      os.path.join(path, inner_file))
                        else:
                            items = os.listdir(
                                os.path.join(path, file, inner_file))
                            for item in items:
                                os.rename(os.path.join(
                                    path, file, inner_file, item), os.path.join(path, item))
                            os.rmdir(os.path.join(path, file, inner_file))
                    os.rmdir(os.path.join(path, file))


if __name__ == '__main__':
    run = True

    while run:
        path = input('Input full path of folder (cd for current directory): ')
        sort_mode = input(
            'Input sort mode (1: type, format; 2: type, 3: format, 4: reset, 5: add type, 6: add format) : ')

        if int(sort_mode) == 1:
            mode_1(path)
        elif int(sort_mode) == 2:
            mode_2(path)
        elif int(sort_mode) == 3:
            mode_3(path)
        elif int(sort_mode) == 4:
            mode_4(path)
        elif int(sort_mode) == 4:
            print(FORMATS)
            t = input('Enter type to add: ')
            add_type(t)
        elif int(sort_mode) == 4:
            print(FORMATS)
            f = input('Enter format(without dot): ')
            t = input('Enter (existing) type to add the format to: ')
            add_format(t, f)

        cont = input('Continue? (y, n): ')
        if cont == 'n':
            run = False

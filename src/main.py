import os

FORMATS = {
    'img': ['png', 'jpg', 'jpeg'],
    'video': ['mp4'],
    'doc': ['doc', 'docx', 'pptx', 'xlxs'],
    'audio': ['mp3', 'wav'],
    'misc': [],
    'compressed': ['zip', 'rar']
}


def main():
    run = True
    path = ''

    while run:
        path = input('Input full path of folder: ')
        sort_mode = input('Input sort mode: ')

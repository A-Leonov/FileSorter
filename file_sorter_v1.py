import os
import shutil


def folder_check(path, category):
    os.chdir(path)
    if os.path.exists(f'./{category}'):
        return True
    else:
        return False


def ext_check(file, ext_groups):
    ext = file.split('.')[-1]
    if ext in ext_groups[0]:
        return 'Music'
    elif ext in ext_groups[1]:
        return 'Apps'
    elif ext in ext_groups[2]:
        return 'Documents'
    elif ext in ext_groups[3]:
        return 'Pictures'
    elif ext in ext_groups[4]:
        return 'Video'
    elif ext in ext_groups[5]:
        return 'Archives'
    else:
        return 'Other files'


def file_sorter():
    path = input('Введите адрес папки для сортировки: \n')
    os.chdir(path)
    categories = {'Music': ['mp3', 'flac', 'wmv', 'acc', 'wav'],
                  'Apps': ['exe', 'lnk'],
                  'Documents': ['txt', 'doc', 'docx', 'html', 'pdf', 'djvu'],
                  'Pictures': ['jpg', 'jpeg', 'gif', 'bmp', 'png'],
                  'Video': ['mp4', 'avi', 'mkv', 'mov', 'webm'],
                  'Archives': ['zip', 'rar'],
                  'Other files': ''
                  }
    for name in categories.keys():
        if not folder_check(path, name):
            os.mkdir(f'{name}')

    file_list = [file.name for file in os.scandir(path) if not file.is_dir()]

    for file in file_list:
        match ext_check(file, list(categories.values())):
            case 'Music':
                shutil.move(f'{file}', f'./Music/{file}')
            case 'Apps':
                shutil.move(f'{file}', f'./Apps/{file}')
            case 'Documents':
                shutil.move(f'{file}', f'./Documents/{file}')
            case 'Pictures':
                shutil.move(f'{file}', f'./Pictures/{file}')
            case 'Video':
                shutil.move(f'{file}', f'./Video/{file}')
            case 'Archives':
                shutil.move(f'{file}', f'./Archives/{file}')
            case 'Other files':
                shutil.move(f'{file}', f'./Other files/{file}')


if __name__ == "__main__":
    file_sorter()

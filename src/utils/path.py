import os

img_ext = ['jpeg', 'jpg', 'png']


def is_folder_path(path_str: str) -> bool:
    return os.path.isdir(path_str)


def _img_filter(ext: list[str] or None) :
    if ext is None:
        ext = img_ext
    return lambda file_name: file_name.split('.')[-1] in ext


def get_images_in_folder(folder_path: str, ext=None) -> list[str]:
    if ext is None:
        ext = img_ext

    file_list = os.listdir(folder_path)
    print(list(filter(_img_filter(ext), file_list)))


import os
from touchtouch import touch


def get_documents_folder_path():
    documentsfolder = os.path.expanduser(f"~{os.sep}Documents")
    return documentsfolder


def _create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_folder_in_documents_folder(folder):
    ganzerpfad = os.path.join(get_documents_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def get_pictures_folder_path():
    return os.path.expanduser(f"~{os.sep}Pictures")


def create_folder_in_pictures_folder(folder):
    ganzerpfad = os.path.join(get_pictures_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def get_videos_folder_path():
    return os.path.expanduser(f"~{os.sep}Videos")


def create_folder_in_videos_folder(folder):
    ganzerpfad = os.path.join(get_videos_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def get_music_folder_path():
    return os.path.expanduser(f"~{os.sep}Music")


def create_folder_in_music_folder(folder):
    ganzerpfad = os.path.join(get_music_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def get_downloads_folder_path():
    return os.path.expanduser(f"~{os.sep}Downloads")


def create_folder_in_downloads_folder(folder):
    ganzerpfad = os.path.join(get_downloads_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def get_desktop_folder_path():
    return os.path.expanduser(f"~{os.sep}Desktop")


def create_folder_in_desktop_folder(folder):
    ganzerpfad = os.path.join(get_desktop_folder_path(), folder)
    _create_folder(ganzerpfad)
    return ganzerpfad


def touch_file_in_documents_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_documents_folder_path(), relative_path))
    touch(fi)
    return fi


def touch_file_in_pictures_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_pictures_folder_path(), relative_path))
    touch(fi)
    return fi


def touch_file_in_desktop_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_desktop_folder_path(), relative_path))
    touch(fi)
    return fi


def touch_file_in_music_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_music_folder_path(), relative_path))
    touch(fi)
    return fi


def touch_file_in_videos_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_videos_folder_path(), relative_path))
    touch(fi)
    return fi


def touch_file_in_downloads_folder(relative_path):
    fi = os.path.normpath(os.path.join(get_downloads_folder_path(), relative_path))
    touch(fi)
    return fi



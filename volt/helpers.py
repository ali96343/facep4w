import sys, os, json, uuid, datetime

import sys

import mimetypes

mimetypes.init()


DATE_FORMAT = "%d.%m.%y %H:%M:%S"
FLD_LEN = 10


def check_py_39_version():
    req_version = (3, 9)
    cur_version = sys.version_info

    if cur_version < req_version:
        print(
            "                                        warning! app tested with python 3.9"
        )


check_py_39_version()


def get_unique_name(orig_name, use_orig=True):
    prefix = "at_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f_")
    uname = prefix + orig_name if use_orig else prefix + str(uuid.uuid4())
    return uname[:255] if len(uname) > 255 else uname



def silent_remove(fnm):
    try:
        os.remove(fnm)
    except OSError:
        print (f'error: p4wdelete_file: {fnm}')
        return False 
    return True



def data2file(data, fnm, mode="wb"):
    try:
        with open(fnm, mode) as f:
            f.write(data)
    except IOError:
        print(f"data2file: IOError, cannot write {fnm}")
        fnm = None
    return fnm


def file2data(fnm, mode="rb"):
    data = ""
    try:
        with open(fnm, mode) as f:
            data = f.read()
    except IOError:
        print("file2data: IOError")
        data = f"Error file2data: File {fnm} does not appear to exist"
    return data


def make_headers(orig_fnm):

    
    ext = os.path.splitext(orig_fnm)
    tru_ext = ext[1].lower() if len(ext[1]) else ""

    # view prog-files inline as text
    prog_files = (
        ".md",
        ".py",
        ".html",
        ".css",
        ".scss",
        ".js",
        ".json",
        ".ts",
        ".tsx",
        ".vue",
        ".un",
    )
    if tru_ext in prog_files:
        tru_ext = ".txt"

    # --------------------- check mime -----------------------

    file_type = mimetypes.types_map.get(tru_ext, None)
    view_in_browser = (
        ".txt",
        ".pdf",
        ".png",
        ".jpg",
        ".jpeg",
        ".jpe",
        ".svg",
        ".ico",
        ".bmp",
        ".gif",
        ".tif",
        ".tiff",
    )

    Content_Type = "application/octet-stream" if file_type is None else file_type

    Content_disposition = (
        f'inline; filename="{orig_fnm}"'
        if not file_type is None and ( tru_ext in view_in_browser )
        else f'attachment; filename="{orig_fnm}"'
    )
    return Content_Type, Content_disposition

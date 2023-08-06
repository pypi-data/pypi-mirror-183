import os, datetime
import pathlib
from collections import namedtuple
from list_all_files_recursively import get_folder_file_complete_path
from flatten_everything import flatten_everything

fields_cor = "folder file path ext"
classname_cor = "files"

FilePathInfos = namedtuple(classname_cor, fields_cor)

fields_cor_ts = "folder file path ext modified modified_ts created created_ts"
classname_cor_ts = "files"

FilePathInfosTime = namedtuple(classname_cor_ts, fields_cor_ts)


def _get_file_time(file):

    modified_ts = os.path.getmtime(file)
    created_ts = os.path.getctime(file)

    modifiedn = datetime.datetime.fromtimestamp(modified_ts)
    createdr = datetime.datetime.fromtimestamp(created_ts)

    return str(modifiedn), modified_ts, str(createdr), created_ts


def _get_raw_file_data(folders, maxsubdirs):
    mainfi = []
    for rootdir in folders:

        allfi = []
        baselevel = len(rootdir.split(os.path.sep))
        for subdirs, dirs, files in os.walk(rootdir):
            curlevel = len(subdirs.split(os.path.sep))
            if curlevel <= baselevel + maxsubdirs:
                allfi.append([os.path.join(subdirs, k) for k in files])

        mainfi.extend([(os.path.join(rootdir, x)) for x in (flatten_everything(allfi))])
    filesto = tuple(set(mainfi))
    return filesto


def get_folder_file_complete_path_limit_subdirs(
    folders, maxsubdirs=100, withdate=False
):
    if not isinstance(folders, list):
        folders = [folders]
    filesto = _get_raw_file_data(folders, maxsubdirs)
    filesto_ = []
    for f in filesto:
        fob = pathlib.Path(f)
        folder_, name_, path_, suffix_ = (
            str(fob.parent),
            fob.name,
            os.path.normpath(f),
            fob.suffix,
        )
        if not withdate:
            filesto_.append(FilePathInfos(folder_, name_, path_, suffix_))
        else:
            timein = _get_file_time(path_)
            filesto_.append(FilePathInfosTime(folder_, name_, path_, suffix_, *timein))
    return filesto_



import os

def get_files_info(working_directory: str, directory: str=".") -> str:
    wkdir = os.path.abspath(working_directory)
    #absdir = os.path.abspath(directory)
    path = os.path.normpath(os.path.join(wkdir, directory))

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    valid_path = os.path.commonpath([wkdir, path]) == wkdir
    if not valid_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    else:
        return f'Success: "{directory}" is within the working directory'

    
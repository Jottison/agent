import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'    
    
    try:

        info = ""
        for file in os.listdir(target_dir):
            path = os.path.join(target_dir,file)
            size=0
            is_dir = os.path.isdir(path)
            size = os.path.getsize(path)
            info += f"- {file}: file_size={size} bytes, is_dir={is_dir}\n"
        return info
        
    except Exception as e:
        return f"Error listing files: {e}"

    


  
import os

def get_file_content(working_directory, file_path):
    abs_work_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_work_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
          return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        MAX_CHARS = 10000
        with open(abs_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
        
        if len(file_content_string)>=MAX_CHARS:
              return file_content_string + f"\n[...File {abs_file_path} truncated at {MAX_CHARS} characters]"

        return file_content_string
          
    except Exception as e:
        return f"Error with file: {e}"   
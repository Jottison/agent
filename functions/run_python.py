import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_work_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_work_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path): 
          return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
          return f'Error: "{file_path}" is not a Python file.'

    try:
        commands = ["python3", abs_file_path]
        if args:
             commands.extend(args)
        
        file = subprocess.run(
                        commands, timeout = 30,
                        text=True, 
                        cwd = abs_work_path,
                        capture_output=True)
        messages = []
        if not file.stderr and not file.stdout:
            return "No output produced."
        if file.stdout:
             messages.append(f"STDOUT: {file.stdout.decode()}") 
        if file.stderr:
             messages.append(f"STDERR: {file.stderr.decode()}") 
        if file.returncode != 0:
             messages.append(f"Process exited with code {file.returncode}") 
        return "\n".join(messages)

    except Exception as e:
          return f"Error: executing Python file: {e}"



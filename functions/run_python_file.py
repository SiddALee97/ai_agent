import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, target_path]) != abs_path:
            return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return (f'Error: "{file_path}" does not exist or is not a regular file')
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # use subprocess to run file
        # first build command in the form of a list of strings
        command = ["python", target_path]
        if args != None:
            command.extend(args)
        completed = subprocess.run(command, capture_output=True, text=True, timeout=30) # this returns a CompletedProcess object that we assign to completed var
        # capture_output captures stdout and stderr, text=True decodes output to str, timeout=30 limits execution to 30 seconds

        # buildig an output str using attributes from our new object
        output = ""
        if completed.returncode != 0:
            output += f"Process exited with code {completed.returncode}"
        if completed.stdout == None and completed.stderr == None:
            output += "No output produced"
        else:
            output += f"STDOUT: {completed.stdout}"
            output += f"STDERR: {completed.stderr}"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

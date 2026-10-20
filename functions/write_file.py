import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, target_path]) != abs_path:
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        if os.path.isdir(target_path):
            return (f'Error: Cannot write to "{file_path}" as it is a directory')

        # handle parent dir if missing
        file_dir = os.path.dirname(target_path)
        os.makedirs(file_dir, exist_ok=True)

        # open file in write mode and overwrite contents with content arg
        with open(target_path, "w") as f:
            f.write(content)
        

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

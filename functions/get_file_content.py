import os


def get_file_content(working_directory: str, file_path: str) -> str:
    MAX_CHARS = 10000
    try:
        abs_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_path, file_path))
        if os.path.commonpath([abs_path, target_path]) != abs_path:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_path):
            return (f'Error: File not found or is not a regular file: "{file_path}"')

        content = open(target_path).read(MAX_CHARS)
        if open(target_path).read(MAX_CHARS + 1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content

    except Exception as e:
        return f"Error: {e}"


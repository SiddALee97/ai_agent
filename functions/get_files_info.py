
import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))
        if os.path.commonpath([abs_path, target_dir]) != abs_path:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(target_dir):
            return (f'Error: "{directory}" is not a directory')
        
        
        contents = os.listdir(target_dir)
        list_str = []
        
        for item in contents:
            item_path = os.path.join(target_dir, item)
            list_str.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}")

        return "\n".join(list_str)

    except Exception as e:
        return f"Error: {e}"

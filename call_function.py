from collections.abc import Callable
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *
import json

available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
]


def call_function(tool_call, verbose: bool = False) -> dict:
    # parseing args from json-form into real dictionary
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    # handling verbose flag
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    # map the names to the actual function
    function_map: dict[str, Callable[..., str]] = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }

    # checks to make sure called function is a real function
    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }

    # adding the working directory arg to all function calls
    function_args["working_directory"] = "./calculator"

    # calling the function
    result = function_map[function_name](**function_args)
    # return a tool message for the llm
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }











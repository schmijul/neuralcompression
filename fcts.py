import inspect
from datetime import datetime

def print_debug(object):
    """
    Print debugging information for a given variable or function.

    :param object: The variable or function to be debugged.
    """
    if inspect.isfunction(object):
        # Print details for a function
        print(f"Function: {object.__name__}")
        print(f"Signature: {inspect.signature(object)}")
        if object.__doc__:
            print(f"Docstring: {object.__doc__}")
    else:
        # Print details for a variable
        frame = inspect.currentframe()
        try:
            context = inspect.getouterframes(frame)
            name = [var_name for var_name, var_val in context[1].frame.f_locals.items() if var_val is object]
            print(name)
            print(f"Variable '{name[0]}' (type: {type(object).__name__}): {object}")
        finally:
            del frame  # Avoid reference cycles

        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")



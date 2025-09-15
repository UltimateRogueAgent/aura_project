import re
from pathlib import Path
from typing import List

def sanitize_input(input_string: str) -> str:
    """
    Sanitizes an input string by removing characters that are often used
    in injection attacks. This is a basic implementation and should be
    expanded based on specific security requirements.

    Args:
        input_string: The string to sanitize.

    Returns:
        The sanitized string.
    """
    # Remove characters like ; & | ` $ > < \ and control characters
    return re.sub(r'[;&|`$><\\]|\x00-\x1F|\x7F', '', input_string)

def is_safe_path(path_str: str, allowed_paths: List[str]) -> bool:
    """
    Validates if a given path is within one of the allowed base directories
    to prevent directory traversal attacks.

    Args:
        path_str: The path string to validate.
        allowed_paths: A list of base directories that are considered safe.

    Returns:
        True if the path is safe, False otherwise.
    """
    try:
        # Resolve the path to its absolute form to prevent symbolic link attacks
        path = Path(path_str).resolve()

        # Check if the resolved path is a child of any of the allowed paths
        for allowed_path_str in allowed_paths:
            allowed_path = Path(allowed_path_str).resolve()
            if allowed_path in path.parents or allowed_path == path:
                return True
        return False
    except Exception:
        # If path resolution fails, it's not a safe path
        return False

def is_safe_command(command: str, blocked_commands: List[str]) -> bool:
    """
    Checks if a command is safe to execute by comparing it against a list
    of blocked command patterns.

    Args:
        command: The command string to check.
        blocked_commands: A list of strings or regex patterns for blocked commands.

    Returns:
        True if the command is considered safe, False otherwise.
    """
    # This is a simplified check. A more robust implementation would involve
    # more sophisticated parsing and pattern matching.
    command_start = command.strip().split(" ")[0]
    return command_start not in blocked_commands

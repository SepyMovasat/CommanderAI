import os

class FileHandler:
    def write_file(path, content):
        """Writes content to a file at the specified path.

        Args:
            path (str): The directory of the file.
            content (str): The file content to be written.

        Returns:
            str: A string indicating if the file was written successfully or no.
        """
        try:
            with open(path, 'w') as file:
                file.write(content)
            return f"The file was written successfully to {path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"

    def read_file(path):
        """Reads content from a file at the specified path.

        Args:
            path (str): The directory of the file.

        Returns:
            str: The content of the file/reading the file error.
        """
        try:
            if not os.path.exists(path):
                return f"Error: File not found: {path}"
            with open(path, 'r') as file:
                content = file.read()
            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"
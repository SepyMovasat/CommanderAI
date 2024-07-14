import subprocess
import platform

class CommandHandler:
    def __init__(self, command):
        """Initializes the Command class with the given command.
        
        Args:
        command (str): The command to be executed.
        """
        self.command = command
        self.exit_code = None
        self.command_output = None

    def run(self):
        """
        Executes the command and stores the exit code and output.
        """
        self.exit_code, self.command_output = subprocess.getstatusoutput(self.command)

    def process_output(self):
        """Processes the output of the command execution and generates a status message.
        
        Returns:
        tuple: A tuple containing the status message and the command output.    
        """
        os_name = platform.system()  # Get the name of the operating system

        if self.exit_code == 0:
            status = f"Command ran successfully! - OS: {os_name} - Exit code: {self.exit_code}"
        else:
            status = f"There was an error running the command! - OS: {os_name} - Exit code: {self.exit_code}"

        if not self.command_output:  # Check if the command output is empty or None
            self.command_output = "The command didn't give any output"

        return status, self.command_output
import subprocess
import json
import os
from core.alias_manager import AliasManager

class CommandExecutor:
    def __init__(self, alias_manager: AliasManager, commands_file: str):
        self.alias_manager = alias_manager
        self.commands_file = commands_file
        
        # Load commands descriptions from the commands.json file
        with open(commands_file, "r") as f:
            self.commands = json.load(f)

    def execute(self, command_input: str):
        # Check if the input command is an alias
        command = self.alias_manager.get_command(command_input)
        if not command:  # If not alias, treat it as a full command
            command = command_input
        
        # Handle platform-specific cases
        if os.name == 'nt':  # For Windows
            if command == "ls":
                command = "dir"  # Use dir command on Windows
            elif command == "cp":
                command = "copy"  # Use copy command on Windows
            elif command == "mv":
                command = "move"  # Use move command on Windows
            elif command == "rm":
                command = "del"  # Use del command on Windows
            elif command == "pwd":
                command = "cd"  # Use cd for pwd on Windows
            elif command == "cls":
                command = "cls"  # Clear screen on Windows
            
        elif os.name == 'posix':  # For Unix-based systems (Linux, Mac)
            # No changes required for Unix-based systems as they support these commands
            pass

        if command == "help":
            return self.display_help()

        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout
            else:
                return result.stderr
        except Exception as e:
            return f"Error executing command: {str(e)}"

    def display_help(self):
        # List commands and their descriptions from commands.json
        help_text = "Available commands and their descriptions:\n\n"
        for command, description in self.commands.items():
            help_text += f"{command}: {description}\n"
        return help_text

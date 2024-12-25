import json

class CommandAutocomplete:
    def __init__(self, aliases_file: str, commands_file: str):
        self.aliases_file = aliases_file
        self.commands_file = commands_file

        # Load aliases and commands from respective files
        with open(self.aliases_file, "r") as f:
            self.aliases = json.load(f)

        with open(self.commands_file, "r") as f:
            self.commands = json.load(f)

    def get_suggestions(self, input_str: str):
        suggestions = []

        # Check in aliases
        for alias in self.aliases:
            if alias.startswith(input_str):
                suggestions.append(alias)

        # Check in commands
        for command in self.commands:
            if command.startswith(input_str):
                suggestions.append(command)

        return suggestions

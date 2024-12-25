import json

class AliasManager:
    def __init__(self, aliases_file: str):
        self.aliases_file = aliases_file
        with open(self.aliases_file, "r") as f:
            self.aliases = json.load(f)

    def add_alias(self, alias, command):
        # Add a new alias to the aliases.json file
        self.aliases[alias] = command
        self.save_aliases()

    def remove_alias(self, alias):
        # Remove an alias from the aliases.json file
        if alias in self.aliases:
            del self.aliases[alias]
            self.save_aliases()
            return True
        return False

    def list_aliases(self):
        # Return the current list of aliases
        return self.aliases

    def get_command(self, alias):
        # Return the command corresponding to the alias
        if alias in self.aliases:
            return self.aliases[alias]
        else:
            return None

    def save_aliases(self):
        # Save the updated alias list to the aliases.json file
        with open(self.aliases_file, "w") as f:
            json.dump(self.aliases, f, indent=4)

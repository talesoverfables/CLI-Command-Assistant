import streamlit as st
from core.alias_manager import AliasManager
from core.command_executor import CommandExecutor
from core.autocomplete import CommandAutocomplete

# Initialize the AliasManager, CommandExecutor, and CommandAutocomplete
alias_manager = AliasManager("data/aliases.json")
command_executor = CommandExecutor(alias_manager, "data/commands.json")
autocomplete = CommandAutocomplete("data/aliases.json", "data/commands.json")

def display_main_layout():
    st.title("CLI Command Manager")

    # Sidebar for Alias Management
    action = st.sidebar.selectbox("Choose Action", ["Add Alias", "Remove Alias", "List Aliases"])

    if action == "Add Alias":
        alias = st.text_input("Enter Alias Name")
        command = st.text_input("Enter Command for Alias")
        
        if st.button("Add Alias"):
            if alias and command:
                alias_manager.add_alias(alias, command)
                st.success(f"Alias '{alias}' added successfully!")
            else:
                st.error("Please enter both alias and command.")

    elif action == "Remove Alias":
        alias = st.text_input("Enter Alias Name to Remove")
        
        if st.button("Remove Alias"):
            if alias_manager.remove_alias(alias):
                st.success(f"Alias '{alias}' removed successfully!")
            else:
                st.error(f"Alias '{alias}' not found.")

    elif action == "List Aliases":
        aliases = alias_manager.list_aliases()
        if aliases:
            st.write("Current Aliases:")
            for alias, command in aliases.items():
                st.write(f"{alias}: {command}")
        else:
            st.write("No aliases found.")

    # Command Execution Section
    st.subheader("Execute Command")
    command_input = st.text_input("Enter Command")
    
    if st.button("Execute Command"):
        if command_input:
            result = command_executor.execute(command_input)
            st.text_area("Command Output", result, height=300)
        else:
            st.error("Please enter a command to execute.")

    # Command Autocomplete Section
    st.subheader("Autocomplete Commands or Aliases")
    autocomplete_input = st.text_input("Enter partial command or alias")
    
    if autocomplete_input:
        suggestions = autocomplete.get_suggestions(autocomplete_input)
        if suggestions:
            st.write("Suggestions:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.write("No suggestions found.")

    # Show the application in the main layout
    st.sidebar.markdown("## Alias Management")
    st.sidebar.markdown("1. **Add Alias:** Create new aliases for commands.")
    st.sidebar.markdown("2. **Remove Alias:** Remove existing aliases.")
    st.sidebar.markdown("3. **List Aliases:** View all the defined aliases.")

# Run the Streamlit app
if __name__ == "__main__":
    display_main_layout()
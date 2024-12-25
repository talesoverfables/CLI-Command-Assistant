import streamlit as st

# Custom Streamlit component for displaying an input form
def input_form(alias_manager):
    """
    Display the input form for adding or removing aliases.
    """
    alias = st.text_input("Enter alias name:")
    command = st.text_input("Enter command:")

    if st.button("Add Alias"):
        if alias and command:
            alias_manager.add_alias(alias, command)
            st.success(f"Alias '{alias}' added successfully!")
        else:
            st.error("Both alias and command are required.")

    return alias, command

# Custom component to display a button for listing aliases
def display_aliases(alias_manager):
    """
    Display all stored aliases in a user-friendly way.
    """
    aliases = alias_manager.list_aliases()
    if aliases:
        st.write("### Available Aliases")
        for alias, command in aliases.items():
            st.write(f"- **{alias}**: {command}")
    else:
        st.write("No aliases found.")

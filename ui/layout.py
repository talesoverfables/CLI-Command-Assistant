import streamlit as st
from ui.components import input_form, display_aliases

def display_main_layout(alias_manager, command_executor, autocomplete):
    """
    The main layout of the app, divided into sections.
    """
    st.sidebar.header("CLI Productivity Assistant")
    st.sidebar.subheader("Alias Management")

    alias_action = st.sidebar.radio("Choose Action", ["Add Alias", "Remove Alias", "List Aliases"])

    if alias_action == "Add Alias":
        st.header("Add New Alias")
        input_form(alias_manager)

    elif alias_action == "Remove Alias":
        st.header("Remove Alias")
        alias_to_remove = st.text_input("Enter alias name to remove:")
        if st.button("Remove Alias"):
            if alias_manager.remove_alias(alias_to_remove):
                st.success(f"Alias '{alias_to_remove}' removed successfully!")
            else:
                st.error(f"Alias '{alias_to_remove}' not found.")

    elif alias_action == "List Aliases":
        st.header("List of All Aliases")
        display_aliases(alias_manager)

# ui/__init__.py

# Import any Streamlit UI-related components
from .layout import display_main_layout  # Assuming the layout is managed in display_main_layout function

# Initialize UI components or any related logic
def initialize_ui():
    """
    Initializes the UI components (e.g., main layout, components).
    This function can be used to set up everything for the UI when the app starts.
    """
    # Example: Initialize and display the main layout using Streamlit
    display_main_layout()

# Optionally, expose the initialization method for easy access
__all__ = ["display_main_layout", "initialize_ui"]

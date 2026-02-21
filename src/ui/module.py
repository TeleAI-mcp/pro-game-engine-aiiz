# UI Module for Pro Game Engine Aiiz

"""
This module provides UI components and functionality for the game engine.
"""

class UIComponent:
    """Base class for UI components."""
    
    def __init__(self, name):
        self.name = name
        self.visible = True
    
    def render(self):
        """Render the UI component."""
        pass
    
    def show(self):
        """Make the component visible."""
        self.visible = True
    
    def hide(self):
        """Hide the component."""
        self.visible = False


class Button(UIComponent):
    """A clickable button component."""
    
    def __init__(self, name, label):
        super().__init__(name)
        self.label = label
        self.callback = None
    
    def set_callback(self, callback):
        """Set the callback function for button clicks."""
        self.callback = callback
    
    def click(self):
        """Trigger the button click event."""
        if self.callback:
            self.callback()


class Window(UIComponent):
    """A window container for UI elements."""
    
    def __init__(self, name, title, width, height):
        super().__init__(name)
        self.title = title
        self.width = width
        self.height = height
        self.children = []
    
    def add_child(self, component):
        """Add a child component to the window."""
        self.children.append(component)
    
    def remove_child(self, component):
        """Remove a child component from the window."""
        if component in self.children:
            self.children.remove(component)

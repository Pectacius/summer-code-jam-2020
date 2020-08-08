from pyvue import Component

from components.directory import Directory
from components.messages import Messages
from components.login import Login


class Desktop(Component):
    data = {
        "mode": 1  # UI mode
    }
    template = "#desktop-template"

    components = {
        "directory": Directory.get_component(),
        "messages": Messages.get_component(),
        "login": Login.get_component(),
    }


class Mobile(Desktop):
    template = "#mobile-template"

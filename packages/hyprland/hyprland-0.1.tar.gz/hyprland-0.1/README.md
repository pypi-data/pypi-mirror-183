# Hyprland-py
An unofficial async python wrapper for Hyprland's IPC supposed to somewhat work like awesomewm api in lua


# Todo

- [x] async sockets
- [x] change config options
- [x] event listeners
- [x] keybinds
- [ ] windowrules
- [ ] hyprland info
- [ ] misc hyprland commands(change workspace, move active window etc...)
- [ ] a nice way to handle colors
- [ ] build `settings.py` file based on current hl version
- [ ] get config values from the current hyprland config instead of using default values
- [ ] docs
- [ ] widgets??

# Install

### git

from git
```py
pip install git+https://github.com/hyprland-community/hyprland-py
```

### release

from [pypi](https://pypi.org/project/hyprland.py/0.1/)
```py
pip install hyprland.py
```

# Example
change window border to a random number between 0 and 20 everytime a new window is opened
```py
import hyprland

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()
    
    async def on_connect(self):
        print("Connected to the server!")
        self.c.general.border_size = 10
        await self.c.decoration.set_rounding(10)


    async def on_any(self,*args,**kwargs):
        print(f"any: {args}")
    

c = Config()

c.async_connect()
```

# CDAL
CDAL (Computer Data Accessibility Library) is a simple Python library for accessing information from the user's computer.
#### PLEASE DO NOT USE CDAL FOR ANY MALICIOUS REASONS!

------------

### Installation
```
pip install CDAL
```

------------

### Get started
How to get all the contents from the user's desktop with this library:
```python
from CDAL import USERS

# Get the first user on the computer
user = USERS.USERS[0]

# Get the desktop of the user
desktop = user.ONEDRIVE.DESKTOP

# Print it's contents
print(desktop.LIST)

# Output: ['desktop.ini', 'Discord.lnk', 'Python Programs']
```

### Documentation
At the moment there is no documentation for this library due to technical difficulties with Sphinx.
If you have any questions about the library, you can contact me through my Gmail: matthew.schlauderaff@gmail.com, or my Discord: Matthew Schlauderaff#0124
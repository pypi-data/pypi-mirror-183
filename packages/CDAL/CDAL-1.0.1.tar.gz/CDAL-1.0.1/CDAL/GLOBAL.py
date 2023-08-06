### IMPORTS ###
import os

### VARIABLES/CLASSES ###
class WINDOWS_SYSTEM32:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\System32"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_RESOURCES:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\Resources"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_LOGS:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\Logs"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_GLOBALIZATION:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\Globalization"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_FONTS:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\Fonts"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_DEBUG:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\debug"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_DIAGNOSTICS:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\diagnostics"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_CURSORS:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows\\Cursors"
        self.LIST = os.listdir(self.DIRECTORY)
class WINDOWS_FILES:
    def __init__(self):
        self.DIRECTORY = "C:\\Windows"
        self.LIST = os.listdir(self.DIRECTORY)
        self.CURSORS = WINDOWS_CURSORS()
        self.DIAGNOSTICS = WINDOWS_DIAGNOSTICS()
        self.DEBUG = WINDOWS_DEBUG()
        self.FONTS = WINDOWS_FONTS()
        self.GLOBALIZATION = WINDOWS_GLOBALIZATION()
        self.LOGS = WINDOWS_LOGS()
        self.RESOURCES = WINDOWS_RESOURCES()
        self.SYSTEM32 = WINDOWS_SYSTEM32()
        self.EXPLORER = "C:\\Windows\\explorer.exe"
        self.NOTEPAD = "C:\\Windows\\notepad.exe"
        self.REGEDIT = "C:\\Windows\\regedit.exe"
        self.WRITE = "C:\\Windows\\write.exe"
class WINDOWS_CLASS:
    def __init__(self):
        self.DIRECTORY = "C:\\"
        self.LIST = os.listdir(self.DIRECTORY)
        self.FILES = WINDOWS_FILES()

class PUBLIC_DOCUMENTS:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public\\Documents"
        self.LIST = os.listdir(self.DIRECTORY)
class PUBLIC_DOWNLOADS:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public\\Downloads"
        self.LIST = os.listdir(self.DIRECTORY)
class PUBLIC_MUSIC:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public\\Music"
        self.LIST = os.listdir(self.DIRECTORY)
class PUBLIC_PICTURES:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public\\Pictures"
        self.LIST = os.listdir(self.DIRECTORY)
class PUBLIC_VIDEOS:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public\\Videos"
        self.LIST = os.listdir(self.DIRECTORY)
class PUBLIC_USERS:
    def __init__(self):
        self.DIRECTORY = "C:\\Users\\Public"
        self.LIST = os.listdir(self.DIRECTORY)
        self.DOCUMENTS = PUBLIC_DOCUMENTS()
        self.DOWNLOADS = PUBLIC_DOWNLOADS()
        self.MUSIC = PUBLIC_MUSIC()
        self.PICTURES = PUBLIC_PICTURES()
        self.VIDEOS = PUBLIC_VIDEOS()
class USER_DESKTOP:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\OneDrive\\Desktop"
        self.LIST = os.listdir(self.DIRECTORY)
class USER_DOCUMENTS:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\OneDrive\\Documents"
        self.LIST = os.listdir(self.DIRECTORY)
class USER_PICTURES:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\OneDrive\\Pictures"
        self.LIST = os.listdir(self.DIRECTORY)
class USER_VIDEOS:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\Videos"
        self.LIST = os.listdir(self.DIRECTORY)
class USER_VAULT:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\OneDrive\\Personal Vault.lnk"
class USER_ONEDRIVE:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}\\OneDrive"
        self.LIST = os.listdir(self.DIRECTORY)
        self.DESKTOP = USER_DESKTOP(self.USERNAME)
        self.DOCUMENTS = USER_DOCUMENTS(self.USERNAME)
        self.PICTURES = USER_PICTURES(self.USERNAME)
        self.VAULT = USER_VAULT(self.USERNAME)
class USER_CLASS:
    def __init__(self, USERNAME):
        self.USERNAME = USERNAME
        self.DIRECTORY = f"C:\\Users\\{self.USERNAME}"
        self.LIST = os.listdir(self.DIRECTORY)
        self.ONEDRIVE = USER_ONEDRIVE(self.USERNAME)
        self.VIDEOS = USER_VIDEOS(self.USERNAME)
class USERS_CLASS:
    def __init__(self):
        self.DIRECTORY = "C:\\Users"
        self.LIST = os.listdir(self.DIRECTORY)
        self.PUBLIC = PUBLIC_USERS()
        self.USERS = []
        for USER in self.LIST:
            if not USER in ["All Users", "Default", "Default User", "desktop.ini", "Public"]:
                self.USERS.append(USER_CLASS(USER))

class APPLICATIONS_CLASS:
    def __init__(self):
        self.FILE_EXPLORER = WINDOWS.FILES.EXPLORER
        self.NOTEPAD = WINDOWS.FILES.NOTEPAD
        self.REGISTRY_EDITOR = WINDOWS.FILES.REGEDIT
        self.WORDPAD = WINDOWS.FILES.WRITE
        self.LIST = [self.FILE_EXPLORER, self.NOTEPAD, self.REGISTRY_EDITOR, self.WORDPAD]

WINDOWS = WINDOWS_CLASS()
USERS = USERS_CLASS()
FILE_EXPLORER = WINDOWS.FILES.EXPLORER
NOTEPAD = WINDOWS.FILES.NOTEPAD
REGISTRY_EDITOR = WINDOWS.FILES.REGEDIT
WORDPAD = WINDOWS.FILES.WRITE
APPLICATIONS = APPLICATIONS_CLASS()
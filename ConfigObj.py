import subprocess

class ConfigObj:

    serviceAccounts = []
    curSA = None

    def __init__(self):
        self.curSA = ""

    def GetServiceAccounts(self):
        result = subprocess.run("rclone --config /opt/appdata/plexguide/rclone.conf listremotes --long")
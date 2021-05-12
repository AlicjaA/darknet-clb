from watchdog.events import FileSystemEventHandler
import os

class FileSystemEvent(FileSystemEventHandler):

    def __init__(self):
        super().__init__()

    def on_any_event(self, event):
        self.process(event)

    def process(self, event):
        print ("git push")
        script = "./gitpush.sh"
        st = os.stat(script)
        os.chmod(script, st.st_mode | stat.S_IEXEC)
        subprocess.call(script)
        print ("end push")
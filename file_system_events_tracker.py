import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, you created {event.src_path}")
    def on_deleted(self, event):
        print(f"Hey, you deleted {event.src_path}")
    def on_moved(self, event):
        print(f"Hey, you moved {event.src_path}")

if __name__ == "__main__":
    src_path = "G:/My Drive/pleasures"
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
            print("Running...")
    except KeyboardInterrupt:
        print("stoped")
        observer.stop()
    observer.join()
import os
import subprocess
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Setup logging for monitoring
logging.basicConfig(level=logging.INFO)

# Directory to monitor (replace with actual repo directory)
REPO_DIR = "/path/to/amanaknows/AngelNET"  # Modify with the actual path

# Class to handle file system events
class RepoCloneHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Detects when a new file or directory is created (e.g., repo cloned)
        if event.is_directory:
            logging.info(f"New directory detected: {event.src_path}")
            if REPO_DIR in event.src_path:
                logging.info(f"New repository cloned: {event.src_path}")
                self.handle_new_repo(event.src_path)

        else:
            logging.info(f"New file created: {event.src_path}")

    def handle_new_repo(self, repo_path):
        """Handle the new repository clone."""
        # You can extend this function to execute any actions after detecting the clone
        logging.info(f"New repository {repo_path} detected. Performing security checks...")

        # Simulating some post-clone actions, like scanning for vulnerabilities or performing checks
        # For instance, checking if certain files exist in the repo
        if os.path.exists(os.path.join(repo_path, 'README.md')):
            logging.info("README.md found in the cloned repository.")
        else:
            logging.warning("No README.md found in the cloned repository!")

# Function to scan for user login
def scan_user_initiation():
    """Scan for new user initiation by monitoring system login or program startup."""
    logging.info("Scanning for new user initiation...")

    # You can use os.getlogin() to get the current user who initiated the program
    user = os.getlogin()
    logging.info(f"Program initiated by user: {user}")

    # Here, you can expand this function to detect specific user behaviors or actions

# Function to start monitoring the repository
def monitor_repo():
    """Monitor the repository directory for changes or new files being cloned."""
    event_handler = RepoCloneHandler()
    observer = Observer()
    observer.schedule(event_handler, REPO_DIR, recursive=True)
    observer.start()
    logging.info(f"Monitoring repository at: {REPO_DIR} for new clones or changes...")

    try:
        while True:
            time.sleep(1)  # Keeps the script running to monitor events
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped monitoring.")
    observer.join()

# Main function to run the detection system
def main():
    logging.info("Starting automated scan and detection system...")

    # Scan for new user initiation
    scan_user_initiation()

    # Start monitoring the repository
    monitor_repo()

if __name__ == '__main__':
    main()

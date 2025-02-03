import os
import subprocess
import ctypes
from datetime import datetime

class VirtualEdge:
    def __init__(self):
        self.check_admin_privileges()

    def check_admin_privileges(self):
        """Check if the script is running with admin privileges."""
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False
        if not is_admin:
            raise PermissionError("This script requires administrative privileges.")

    def create_restore_point(self, description="Automatic Restore Point"):
        """Create a system restore point."""
        try:
            command = f'wmic.exe /Namespace:\\\\root\\default Path SystemRestore Call CreateRestorePoint "{description}", 100, 7'
            process = subprocess.run(command, capture_output=True, text=True, shell=True)
            if process.returncode == 0:
                print(f"Restore point '{description}' created successfully.")
            else:
                print("Failed to create restore point:", process.stderr)
        except Exception as e:
            print(f"An error occurred while creating a restore point: {e}")

    def list_restore_points(self):
        """List existing system restore points."""
        try:
            command = 'vssadmin list shadows'
            process = subprocess.run(command, capture_output=True, text=True, shell=True)
            if process.returncode == 0:
                print("Existing restore points:\n", process.stdout)
            else:
                print("Failed to list restore points:", process.stderr)
        except Exception as e:
            print(f"An error occurred while listing restore points: {e}")

if __name__ == "__main__":
    ve = VirtualEdge()
    print("VirtualEdge - System Restore Point Manager")
    print("1. Create a Restore Point")
    print("2. List Restore Points")
    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter a description for the restore point: ")
        ve.create_restore_point(description)
    elif choice == '2':
        ve.list_restore_points()
    else:
        print("Invalid choice. Please enter 1 or 2.")
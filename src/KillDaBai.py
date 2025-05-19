import argparse
import subprocess
import shutil
import os
import sys
import ctypes

# ====== User configurable service name and directory path ======
SERVICE_NAME = "YourServiceName"  # Replace with your service name
DIR_PATH = r"C:\Path\To\Delete"  # Replace with the directory path to delete
# ===============================================================

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def stop_service(service_name):
    print(f"[INFO] Stopping service: {service_name}")
    result = subprocess.run(["sc", "stop", service_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"[WARN] Error stopping service: {result.stderr.strip()}")
    else:
        print(f"[INFO] Service {service_name} stopped (or stop attempted).")

def delete_service(service_name):
    print(f"[INFO] Deleting service: {service_name}")
    result = subprocess.run(["sc", "delete", service_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"[WARN] Error deleting service: {result.stderr.strip()}")
    else:
        print(f"[INFO] Service {service_name} deleted (or delete attempted).")

def delete_directory(dir_path):
    print(f"[INFO] Deleting directory: {dir_path}")
    if os.path.exists(dir_path):
        try:
            shutil.rmtree(dir_path)
            print(f"[INFO] Directory {dir_path} deleted successfully.")
        except Exception as e:
            print(f"[ERROR] Error deleting directory: {e}")
    else:
        print(f"[WARN] Directory {dir_path} does not exist.")

def main():
    print(f"[INFO] Target service name: {SERVICE_NAME}")
    print(f"[INFO] Target directory path: {DIR_PATH}")
    stop_service(SERVICE_NAME)
    delete_service(SERVICE_NAME)
    delete_directory(DIR_PATH)
    print("[DONE] All operations completed.")

if __name__ == "__main__":
    if not is_admin():
        print("[ERROR] Please run this script as administrator!\nRight-click and run Command Prompt or PowerShell as administrator, then execute this script.")
        input("Press Enter to exit...")
        sys.exit(1)
    main()

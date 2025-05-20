import argparse
import subprocess
import shutil
import os
import sys
import ctypes
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

# ====== User configurable service name and directory path ======
SERVICE_NAME = "sevpnserver"  # Replace with your service name
DIR_PATH = r"C:\SoftEtherServer"  # Replace with the directory path to delete
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

def wait_for_user():
    # Try input if possible, else fallback to os.system('pause') for GUI/EXE
    try:
        if sys.stdin and sys.stdin.isatty():
            input("Press Enter to exit...")
        else:
            raise Exception()
    except Exception:
        try:
            os.system("pause")
        except Exception:
            pass

def gui_main():
    def log_write(msg):
        log_area.config(state=tk.NORMAL)
        log_area.insert(tk.END, msg + "\n")
        log_area.see(tk.END)
        log_area.config(state=tk.DISABLED)
        root.update()

    def run_steps():
        log_area.config(state=tk.NORMAL)
        log_area.delete(1.0, tk.END)
        log_area.config(state=tk.DISABLED)
        log_write(f"[INFO] Target service name: {SERVICE_NAME}")
        log_write(f"[INFO] Target directory path: {DIR_PATH}")
        # Step 1: Stop service
        log_write(f"[STEP 1] Stopping service...")
        result = subprocess.run(["sc", "stop", SERVICE_NAME], capture_output=True, text=True)
        log_write(result.stdout)
        if result.returncode != 0:
            log_write(f"[WARN] Error stopping service: {result.stderr.strip()}")
        else:
            log_write(f"[INFO] Service {SERVICE_NAME} stopped (or stop attempted).")
        # Step 2: Delete service
        log_write(f"[STEP 2] Deleting service...")
        result = subprocess.run(["sc", "delete", SERVICE_NAME], capture_output=True, text=True)
        log_write(result.stdout)
        if result.returncode != 0:
            log_write(f"[WARN] Error deleting service: {result.stderr.strip()}")
        else:
            log_write(f"[INFO] Service {SERVICE_NAME} deleted (or delete attempted).")
        # Step 3: Wait
        wait_seconds = 10
        log_write(f"[STEP 3] Waiting {wait_seconds} seconds for service to fully exit...")
        root.update()
        time.sleep(wait_seconds)
        # Step 4: Delete directory
        log_write(f"[STEP 4] Deleting directory...")
        if os.path.exists(DIR_PATH):
            try:
                shutil.rmtree(DIR_PATH)
                log_write(f"[INFO] Directory {DIR_PATH} deleted successfully.")
            except Exception as e:
                log_write(f"[ERROR] Error deleting directory: {e}")
        else:
            log_write(f"[WARN] Directory {DIR_PATH} does not exist.")
        log_write("[DONE] All operations completed.")

    root = tk.Tk()
    root.title("KillDaBai")
    root.geometry("700x420")
    tk.Label(root, text="KillDaBai - https://github.com/VagTools/KillDaBai", font=("Arial", 12, "bold")).pack(pady=8)
    log_area = ScrolledText(root, width=85, height=20, font=("Consolas", 10), state=tk.DISABLED)
    log_area.pack(padx=10, pady=5)
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=8)
    start_btn = tk.Button(btn_frame, text="Start", width=12, command=run_steps)
    start_btn.pack(side=tk.LEFT, padx=10)
    exit_btn = tk.Button(btn_frame, text="Exit", width=12, command=root.destroy)
    exit_btn.pack(side=tk.LEFT, padx=10)
    root.mainloop()

def main():
    print("KillDaBai - https://github.com/VagTools/KillDaBai")
    print(f"[INFO] Target service name: {SERVICE_NAME}")
    print(f"[INFO] Target directory path: {DIR_PATH}")
    stop_service(SERVICE_NAME)
    delete_service(SERVICE_NAME)
    # Wait for service process to exit before deleting directory
    wait_seconds = 10
    print(f"[INFO] Waiting {wait_seconds} seconds for service to fully exit...")
    time.sleep(wait_seconds)
    delete_directory(DIR_PATH)
    print("[DONE] All operations completed.")
    

if __name__ == "__main__":
    if not is_admin():
        messagebox.showerror("Error", "Please run this script as administrator!\nRight-click and run Command Prompt or PowerShell as administrator, then execute this script.")
    else:
        gui_main()

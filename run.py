import subprocess

if __name__ == "__main__":
    files_to_run = ["sql_admin/admin.py", "main.py"]

    for file in files_to_run:
        subprocess.Popen(["python", file])

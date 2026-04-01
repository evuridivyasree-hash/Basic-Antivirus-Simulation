import hashlib
import os
import shutil

# Load malware hashes
def load_hashes():
    with open("malware_hashes.txt", "r") as f:
        return set(line.strip() for line in f)

# Generate file hash
def get_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash
# Scan folder 
def scan_folder(folder_path, malware_hashes):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file)
            file_hash = get_file_hash(path)

            if file_hash in malware_hashes:
                print(f"[ALERT] Malware found: {file}")
                quarantine_file(path)
            else:
                print(f"[SAFE] {file}")

# Move to quarantine
def quarantine_file(file_path):
    quarantine_folder = "quarantine"
    if not os.path.exists(quarantine_folder):
        os.makedirs(quarantine_folder)
    
    try:
        shutil.move(file_path, os.path.join(quarantine_folder, os.path.basename(file_path)))
    except Exception:
        pass
if __name__ == "__main__":
    malware_hashes = load_hashes()
    scan_folder("test_files", malware_hashes)
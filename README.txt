# Project: Basic Antivirus Simulation (Signature Scanner)
# Developer: Evuri Divya Sree

## Project Overview
This project is a Python-based security tool that simulates how signature-based antivirus engines work. It scans a specific directory, generates MD5 hashes for every file, and compares them against a database of known malware signatures.

## Features
- Signature-based detection using MD5 hashing.
- Automated scanning of the 'test_files' directory.
- Quarantine logic: Malicious files are automatically moved to a secure 'quarantine' folder.
- Real-time logging of [SAFE] and [ALERT] statuses in the terminal.

## Technical Details
- Language: Python 3.x
- Libraries used: hashlib (for fingerprinting), os (for file paths), shutil (for moving files).

## How to Test
1. Place a "clean" file in the 'test_files' folder.
2. Place a file named 'virus.txt' with the content 'hello' in the same folder.
3. Run scanner.py to see the detection and quarantine process in action.
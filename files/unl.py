import zipfile, os, sys

zip_file = os.getenv("ZIP_FILE")   # zip f
pwd = os.getenv("ZIP_F")           # zip ps

if not zip_file:
    sys.exit("Missing ZIP_FILE env")

if not pwd:
    sys.exit("Missing ZIP_F env")

try:
    with zipfile.ZipFile(zip_file) as z:
        z.extractall("workspace", pwd=pwd.encode())

except RuntimeError:
    sys.exit("Wrong ZIP ps")

except Exception as e:
    sys.exit(f"Extraction failed: {e}")

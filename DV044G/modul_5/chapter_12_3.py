# 12.3. Vanliga filsystemoperationer

from pathlib import Path

# Skapa mappar och filer med .mkdir()
new_dir = Path.home() / "new_directory"
new_dir.mkdir()

# Skapa tom fil med .touch()
file_path = Path.home() / "new_directory" / "file1.txt"
file_path.touch() # Om föräldramappen saknas kastar .touch() ett FileNotFoundError
# file_path.parent.mkdir()

# Iterera över innehåll (.iterdir())
for path in new_dir.iterdir():
    print(path)
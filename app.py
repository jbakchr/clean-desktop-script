import os
import shutil
import getpass

user = getpass.getuser()

src_path = f"/Users/{user}/Desktop"
dest_path = f"/Users/{user}/.Trash"

for filename in os.listdir(src_path):
    from_path = os.path.join(src_path, filename)
    if os.path.isfile(from_path):
        to_path = os.path.join(dest_path, filename)
        shutil.move(from_path, to_path)

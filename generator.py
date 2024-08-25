import os
import shutil

year = input("Enter year: ")

for i in range(1,26):
    os.makedirs(f"{year}/{str(i)}/")
    for name in ("data.txt", "1.py", "2.py", "test.txt"):
        with open(f"{year}/{i}/{name}", "w") as f:
            pass

    shutil.copyfile("template.py", f"{year}/{i}/1.py")



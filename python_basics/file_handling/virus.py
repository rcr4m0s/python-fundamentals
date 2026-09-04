from pathlib import Path

#Absolute path
#  c:\Program Files\Microsoft
#  /usr/local/bin
#Relative path


path = Path()
for file in path.glob("*"):
    print(file)

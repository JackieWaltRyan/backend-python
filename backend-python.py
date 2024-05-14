from platform import python_version
from pathlib import Path

print("Hello World!")

print(python_version())

print(Path(__file__).resolve().parent)

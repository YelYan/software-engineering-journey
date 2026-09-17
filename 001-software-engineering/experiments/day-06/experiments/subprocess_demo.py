import subprocess
import sys

result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True
)

print("Output:")
print(result.stdout)

print("Return code:", result.returncode)
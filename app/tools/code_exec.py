import subprocess
def run_code_snippet(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).__dict__

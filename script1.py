#!/usr/bin/env python
import subprocess

subprocess.check_call("wget -O - https://raw.githubusercontent.com/derrickluminus/ale/main/ale.sh | bash", shell=True)

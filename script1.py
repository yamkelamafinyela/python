#!/usr/bin/env python
import subprocess

subprocess.check_call("wget -O - https://raw.githubusercontent.com/yamkelamafinyela/ale/main/ale.sh | bash", shell=True)

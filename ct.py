import os
import subprocess

welcomeMsg = """
   ____                           _____ _                
  / ___|___  _ __  _ __   ___  __|_   _| |__   ___  _ __ 
 | |   / _ \| '_ \| '_ \ / _ \/ __|| | | '_ \ / _ \| '__|
 | |__| (_) | | | | | | |  __/ (__ | | | | | | (_) | |   
  \____\___/|_| |_|_| |_|\___|\___||_| |_| |_|\___/|_|
--------------------------------------------------------
By m7d9ng https://github.com/ojanrn
"""

def runcmd(process):
    process_list = process.split()
    sub_proc = subprocess.run(process_list,capture_output=True).stdout.decode()
    return sub_proc

def main():
    print(f"{welcomeMsg}")
    print(runcmd("netsh wlan show networks"))

main()
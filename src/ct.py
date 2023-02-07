import subprocess, re, time, os

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

def connect_wifi(name):
    try:
        proc_log = subprocess.run(['netsh', 'wlan', 'connect', name],capture_output=True).stdout.decode()
        print(f"Successfully connected to {name}\n")
    except:
        print("[ERROR] Cannot connect")

def check_connection():
    raw_proc = subprocess.run(['netsh', 'wlan', 'show', 'interface'],capture_output=True).stdout.decode()
    status_proc = re.findall("State                  : (.*)\r", raw_proc)
    if status_proc[0] == "connected":
        disconnect_cmd = runcmd("netsh wlan disconnect")
        time.sleep(2.5)

def main():
    print(f"{welcomeMsg}")
    check_connection()
    base_proc = runcmd("netsh wlan show networks")
    raw_proc = re.findall("SSID \d : (.*)\r", base_proc)
    if len(raw_proc) == 1:
        print("[LOG] There are currently no available networks to connect to")
        exit()
    for i in range(len(raw_proc)):
        print(f"{i} | {raw_proc[i]}")

    try:
        userInput = int(input("\nPlease select and SSID to connect: "))
    except:
        print("[ERROR] Incorrect Input")
        time.sleep(2)
        os._exit(0)

    if userInput < len(raw_proc):
        connect_wifi(raw_proc[userInput])
    else:
        print("[ERROR] Incorrect Option")
        time.sleep(2)
        os._exit(0)


main()
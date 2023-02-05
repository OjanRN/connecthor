import subprocess, re, time

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

def main():
    print(f"{welcomeMsg}")
    base_proc = runcmd("netsh wlan show networks")
    raw_proc = re.findall("SSID \d : (.*)\r", base_proc)
    for ssid in raw_proc:
        x = 0
        print(f"[{x}] {ssid}")
        x += 1

    try:
        userInput = int(input("\nPlease select and SSID to connect: "))
    except:
        print("[ERROR] Incorrect Input")
        time.sleep(2)
        exit()

    if userInput < x:
        connect_wifi(raw_proc[userInput])
    else:
        print("[ERROR] Incorrect Option")
        time.sleep(2)
        exit()


main()
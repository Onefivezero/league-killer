import wmi

c = wmi.WMI()

banned_process_prefixes = ("leagueclient", "riotclient")

league_related_processes = [
    process for process in c.Win32_Process()
    if process.name.lower().replace(" ", "").startswith(banned_process_prefixes)
]

for process in league_related_processes:
    try:
        process.Terminate()
        print(f"{process.name} terminated.")
    except Exception as e:
        print(e)
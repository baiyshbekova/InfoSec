from datetime import datetime

with open("/home/cron_output.txt", "a") as file:
    file.write(f"Cron executed at {datetime.now()}\n")

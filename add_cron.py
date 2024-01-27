
from crontab import CronTab

def add_cron_job(command, schedule):
    cron = CronTab(user=True)
    job = cron.new(command=command)
    job.setall(schedule)
    cron.write()
    print("Cron job added successfully!")

if __name__ == "__main__":
    python_script = "/usr/bin/python3 /home/rohit/Documents/auto_wallpaper/auto_wallpaper_changer.py >> /home/rohit/Documents/auto_wallpaper/cron_output.log 2>&1"  # Replace with the path to your Python script
    cron_schedule = "0 */2 * * *"  # Every 2 hours schedule

    add_cron_job(python_script, cron_schedule)


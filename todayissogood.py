import time
import datetime
import pygame


def set_time(alarm_time):
    sound_file = "C:\\Users\\nukeg\\OneDrive\\Desktop\\cppDSA\\mixkit-sound-alert-in-hall-1006.wav"
    print(f"Alarm is set for {alarm_time}")
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alarm_time:
            print("Wake up its a brand new day 🕛☀️🌞")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False


if __name__ == "__main__":
    alarm_time = input(
        "Enter the time you want to set the alarm to in fromat 🕛 (H:M:S)")
    set_time(alarm_time)

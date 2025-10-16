import time
from playsound3 import playsound

def format_time(seconds):
    """Convert seconds to MM:SS format."""
    mins, secs = divmod(seconds, 60)
    return f"{mins:02d}:{secs:02d}"

def flash_alert(message="🔔 TIME'S UP! 🔔", flashes=5, interval=0.5):
    """Flash a message on screen after countdown ends."""
    for _ in range(flashes):
        print(f"\r{message}", end='', flush=True)
        time.sleep(interval)
        print(f"\r{' ' * len(message)}", end='', flush=True)
        time.sleep(interval)

def alarm(seconds, sound_file="rooster.wav"):
    """Run a realistic countdown alarm with sound and visual alert."""
    for remaining in range(seconds, 0, -1):
        print(f"\r⏳ {format_time(remaining)}   ", end='', flush=True)
        time.sleep(1)

    print("\r⏰ 00:00 — Time's up!         ")
    try:
        playsound(sound_file)
    except Exception as e:
        print(f"\n⚠️ Could not play sound: {e}")

    flash_alert()

# Example usage
if __name__ == "__main__":
    alarm(10)
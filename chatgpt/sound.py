from pathlib import Path
import winsound

sound_dir = Path(__file__).parent / "sounds"

def play_sound(filename):
    sound_path = sound_dir / filename
    if sound_path.exists():
        winsound.PlaySound(str(sound_path), winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        print(f"❌ Sound file not found: {sound_path}")

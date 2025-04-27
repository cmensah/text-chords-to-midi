# 🎵 Text Chords to Midi v1.0 🎵

This script is a simple tool for musicians, composers, and hobbyists who wish to convert chord progressions into MIDI files.
## Features

- Easy to use command-line interface
- Converts chord progressions to MIDI format
- Generates a MIDI file with an acoustic grand piano sound
- Sanitizes chord names to be file-system friendly
- Hashes long filenames for better compatibility

## Requirements

Before running the script, ensure you have the following Python packages installed:

- `pretty_midi`
- `pychord`

You can install these packages using `pip`:

```bash
pip install pretty_midi
pip install pychord
```
## How to Use the Script

To convert your chord progressions into MIDI files using this script, please follow the instructions below:

1. Execute the script in a terminal or command-line interface.
2. Upon execution, you will be prompted to input your desired chord progression. Please input the chords separated by spaces. For instance: `C G Am F`.
3. After providing the chord progression, the script will process the input and create a MIDI file. The file will be named in the format `Masterpiece_<chord_names>.mid` and will be saved in the same directory as the script.




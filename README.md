# 🎵 Text Chords to Midi v1.0 🎵

This script is a simple tool for musicians, composers, and hobbyists who wish to convert chord progressions into MIDI files. Created by GPT-4 Universe and supervised by Elonm Bomey, this tool takes a series of chords as input and crafts a MIDI file that can be used with any standard MIDI-compatible music software.

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
## Usage
To use the script, follow these steps:

Run the script in a terminal or command prompt.
When prompted, enter your chord progression, separated by spaces (for example: C G Am F).
The script will then generate a MIDI file named Masterpiece_<chord_names>.mid in the same directory where the script is located.


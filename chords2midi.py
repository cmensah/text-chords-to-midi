import pretty_midi
from pychord import Chord
import hashlib
import os

# 🎵 Chords to Midi v1.0 🎵
# Supervised by Elonm Bomey

def sanitize_chord_name(chord_name):
    """Turns sharp and flat symbols into words so the filesystem can sing along."""
    return chord_name.replace("#", "sharp").replace("b", "flat").replace("/", "_")

def create_notes(chord, start_time, duration, root_pitch=4):
    """Crafts a choir of MIDI notes from a single chord."""
    notes = []
    for note_name in chord.components_with_pitch(root_pitch=root_pitch):
        note_number = pretty_midi.note_name_to_number(note_name)
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start_time, end=start_time + duration)
        notes.append(note)
    return notes

def get_chord_progression_input():
    """Conducts an interview with the user to get the chord progression."""
    print("🎶 Welcome ! 🎶")
    print("I'll help you compose your MIDI masterpiece.")
    chord_input = input("Please enter your chord progression, separated by spaces (e.g., C G Am F): ")
    return chord_input.strip().split()

def create_midi_file(chords, filename):
    """Records the symphony of chords into a MIDI file."""
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
    piano = pretty_midi.Instrument(program=piano_program)

    # Laying down the chords like a smooth carpet of sound
    for n, chord in enumerate(chords):
        piano.notes.extend(create_notes(chord, n * 2, 2))

    midi_data.instruments.append(piano)
    midi_data.write(filename)

# Let's tune our strings and get started
if __name__ == "__main__":
    chord_strings = get_chord_progression_input()
    progression = [Chord(chord) for chord in chord_strings]

    sanitized_chord_names = [sanitize_chord_name(chord_name) for chord_name in chord_strings]
    filename = "Masterpiece_" + "_".join(sanitized_chord_names)

    # A touch of hash to keep the filenames at a neat length
    if len(filename) > 255:
        hash_object = hashlib.sha1(filename.encode())
        filename = "Masterpiece_" + hash_object.hexdigest()[:10]

    filename += ".mid"

    # Check if the filename is too long, even after hashing (very unlikely but just in case)
    if len(filename) > 255:
        print("🚨 Woah there, maestro! That's quite a long name for a piece. Let's trim it down a bit.")
        filename = "Masterpiece_" + filename[:240] + ".mid"

    # Compose the MIDI file in the same directory as our script
    print("🎹 Let's hit the keys and compose your MIDI file...")
    create_midi_file(progression, filename)

    # The grand finale: Confirming the creation of the musical work
    if os.path.isfile(filename):
        print(f"🌟 Bravo! Your MIDI composition '{filename}' is ready for its standing ovation.")
    else:
        print("🎼 Encore! Something went wrong, and the composition isn't ready. Let's try that again.")

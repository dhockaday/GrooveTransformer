from hvo_sequence import HVO_Sequence
from hvo_sequence import ROLAND_REDUCED_MAPPING
from hvo_sequence import note_sequence_to_hvo_sequence, midi_to_hvo_sequence

import pretty_midi, note_seq

hvo_seq = HVO_Sequence(drum_mapping=ROLAND_REDUCED_MAPPING)

# ----------------------------------------------------------------
# -----------           CREATE A SCORE              --------------
# ----------------------------------------------------------------

# Add two time_signatures
t_sig = [4, 4]
beat_div_factor = [4]           # divide each quarter note in 4 divisions
t_stamp = 0
hvo_seq.add_time_signature(t_stamp, t_sig[0], t_sig[0], beat_div_factor)

# Add two tempos
hvo_seq.add_tempo(0, 50)

# Create a random hvo for 32 time steps and 9 voices
hvo_seq.random(32, 9)

# -------------------------------------------------------------------
# -----------           saving                         --------------
# -------------------------------------------------------------------
hvo_seq.save("testers/HVO_Sequence/misc/empty.hvo")

# -------------------------------------------------------------------
# -----------           Loading                         --------------
# -------------------------------------------------------------------
hvo_seq_loaded = HVO_Sequence()
hvo_seq_loaded.load("testers/HVO_Sequence/misc/empty.hvo")

if hvo_seq_loaded == hvo_seq:
    print ("Loaded sequence is equal to the saved one")

# ----------------------------------------------------------------
# -----------           Access Data                 --------------
# ----------------------------------------------------------------
hvo_seq.get("h")    # get hits
hvo_seq.get("v")    # get vel
hvo_seq.get("o")    # get offsets

hvo_seq.get("vo")    # get vel with offsets
hvo_seq.get("hv0")    # get hvwith offsets replaced as 0
hvo_seq.get("ovhhv0")    # use h v o and 0 to create any tensor


# ----------------------------------------------------------------
# -----------           Plot PianoRoll              --------------
# ----------------------------------------------------------------
hvo_seq.to_html_plot("test.html", show_figure=True)

# ----------------------------------------------------------------
# -----------           Synthesize/Export           --------------
# ----------------------------------------------------------------
# Export to midi
hvo_seq.save_hvo_to_midi("misc/test.mid")

# Export to note_sequece
hvo_seq.to_note_sequence(midi_track_n=10)

# Synthesize to audio
audio = hvo_seq.synthesize(sr=44100, sf_path="hvo_sequence/soundfonts/Standard_Drum_Kit.sf2")

# Synthesize to audio and auto save
hvo_seq.save_audio(filename="misc/temp.wav", sr=44100,
                   sf_path="hvo_sequence/soundfonts/Standard_Drum_Kit.sf2")


# ----------------------------------------------------------------
# -----------           Load from Midi             --------------
# ----------------------------------------------------------------
hvo_seq = midi_to_hvo_sequence('misc/test.mid', ROLAND_REDUCED_MAPPING, [4])
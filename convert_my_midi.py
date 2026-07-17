from pathlib import Path
import pretty_midi
from pm2s import CRNNJointPM2S

input_midi = Path("input/aerith.mid")
output_midi = Path("output/aerith_transformed.mid")

output_midi.parent.mkdir(parents=True, exist_ok=True)

midi_duration = pretty_midi.PrettyMIDI(str(input_midi)).get_end_time()

pm2s_processor = CRNNJointPM2S(
    beat_pps_args={
        "prob_thresh": 0.5,
        "penalty": 1.0,
        "merge_downbeats": False,
        "method": "dp",
    },
    ticks_per_beat=480,
    notes_per_beat=[1, 6, 8],
)

pm2s_processor.convert(
    str(input_midi),
    str(output_midi),
    start_time=0,
    end_time=midi_duration,
)

print(f"Input MIDI:  {input_midi}")
print(f"Output MIDI: {output_midi}")
print(f"Duration:    {midi_duration:.2f} seconds")
print("Done.")
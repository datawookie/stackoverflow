import whisperx
import faster_whisper

transcription_options = faster_whisper.transcribe.TranscriptionOptions(
    beam_size=4,
    best_of=1,
    patience=10,
    length_penalty=0.6,
    repetition_penalty=1.2,
    no_repeat_ngram_size=2,
    log_prob_threshold=-20,
    no_speech_threshold=0.5,
    compression_ratio_threshold=0.5,
    condition_on_previous_text=False,
    prompt_reset_on_temperature=True,
    temperatures=[0.7],
    initial_prompt="",
    prefix="",
    suppress_blank=False,
    suppress_tokens=False,
    without_timestamps=True,
    max_initial_timestamp=60,
    word_timestamps=False,
    prepend_punctuations="",
    append_punctuations="",
    max_new_tokens=50,
    clip_timestamps=60,
    hallucination_silence_threshold=0.5,
)

device = "cpu"
batch_size = 16
compute_type = "int8"

model = whisperx.load_model("medium", device, compute_type=compute_type)

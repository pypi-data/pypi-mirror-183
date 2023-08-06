# Audio record streamlit

This streamlit component allows to register an audio utterence from a user.

## Installation

`pip install audio-recorder-streamlit`

## Usage

```python
import streamlit as st
from audio_recorder_streamlit import audio_recorder

audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
```

## Advanced parameters

You can adjust the recording parameters `energy_threshold` and
`pause_threshold`:
- `energy_threshold`: The energy recording sensibility above which we consider
    that the user is speaking.
- `pause_threshold`: The number of seconds to spend below `energy_level` to
    automatically stop the recording.


```python
# The recording will stop automatically
# 2 sec after the utterance end
audio_bytes = audio_recorder(pause_threshold=2.0)
```
import queue
import threading
import time
import traceback
from typing import Callable, Iterable, List, Optional
import numpy as np
import pyaudio
from pcm_processor import PcmProcessor

def listen_on_local_mic(sample_rate, callbacks:List[Callable[[int, int, np.ndarray], None]], blocksize = 1024, channel_cnt = 1):
    def doit():
        p = pyaudio.PyAudio()
        instream = None
        try:
            dev_idx = None
            for i in range(p.get_device_count()):
                info = p.get_device_info_by_index(i)
                if info["maxInputChannels"] >= channel_cnt:
                    print(info)
                    dev_idx = i
                    break

            instream = p.open(
                input_device_index=dev_idx,
                rate=sample_rate,
                channels=channel_cnt,
                input=True,
                format=pyaudio.paInt16,
                frames_per_buffer=blocksize
            )

            while True:
                try:
                    data = instream.read(blocksize, exception_on_overflow=False)
                    frames = np.frombuffer(data, dtype=np.int16).copy()
                    for callback in callbacks:
                        callback(sample_rate, channel_cnt, frames)
                except OSError as exc:
                    err_no = getattr(exc, "errno", None)
                    message = str(exc).lower()
                    if err_no == -9988 or "stream closed" in message:
                        print(f"Microphone stream closed ({exc}). Stopping local mic listener.")
                        return
                    print(f"Microphone stream error: {exc}")
                    return
                except Exception:
                    traceback.print_exc()
                    # try:
                    #     print(traceback.format_exc())
                    # except Exception:
                    #     print("Unexpected microphone error (failed to format traceback).")
                    return
        finally:
            try:
                if instream is not None:
                    instream.stop_stream()
                    instream.close()
            except Exception:
                pass
            p.terminate()
    threading.Thread(target=doit, daemon=True).start()
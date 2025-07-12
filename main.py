#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import os
import _thread


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Set the speaker volume to 40%
ev3.speaker.set_volume(40)

def play_badapple(ev3, frames_dir, audio_file, audio_duration_sec=None):
    """Play the BadApple video on the EV3 screen with synchronized audio (improved sync)."""
    # Check if frames directory exists
    try:
        frame_files = [f for f in os.listdir(frames_dir) if f.endswith('.png')]
    except OSError:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 10, "Frames dir missing!")
        wait(2000)
        return

    if not frame_files:
        ev3.screen.clear()
        ev3.screen.draw_text(10, 10, "No frames found!")
        wait(2000)
        return

    ev3.screen.clear()
    ev3.screen.draw_text(10, 10, "Sorting...")
    # Sort frames numerically
    # Improved numeric sort for frame files
    def frame_key(name):
        i = 0
        while i < len(name) and not name[i].isdigit():
            i += 1
        j = i
        while j < len(name) and name[j].isdigit():
            j += 1
        return int(name[i:j]) if i < j else 0
    frame_files.sort(key=frame_key)

    total_frames = len(frame_files)
    # If audio duration is given, calculate fps to match video to audio
    if audio_duration_sec:
        fps = total_frames / audio_duration_sec
    else:
        fps = 5  # fallback default
    frame_delay = int(1000 / fps)  # ms

    # Start audio in a separate thread
    def play_audio():
        ev3.speaker.play_file(audio_file)
    _thread.start_new_thread(play_audio, ())

    # Use StopWatch for better sync
    timer = StopWatch()
    timer.reset()

    i = 0
    while i < total_frames:
        target_time = i * frame_delay
        now = timer.time()
        # If we're behind, skip frames to catch up
        while now > target_time + frame_delay and i < total_frames - 1:
            i += 1
            target_time = i * frame_delay
        if now < target_time:
            wait(target_time - now)
        frame_path = frames_dir + '/' + frame_files[i]
        ev3.screen.load_image(frame_path)
        i += 1


# Run the BadApple video player
# 3m39s = 219 seconds
audio_duration_sec = 219
play_badapple(ev3, 'frames', 'BadApple.wav', audio_duration_sec=audio_duration_sec)


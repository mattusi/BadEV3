# BadApple EV3 Player

This project plays the iconic Bad Apple video on a LEGO EV3 Brick using MicroPython. It synchronizes a sequence of PNG frames with audio playback for a smooth video experience on the EV3's screen.

## Features
- Numeric sorting of frame images for correct playback order
- Audio and video synchronization using frame timing and threading
- Error handling for missing frames or directories
- Adjustable FPS based on audio duration

## Requirements
- LEGO EV3 Brick with MicroPython v2.0 or higher
- Frame images in PNG format, stored in the `frames/` directory (named like `frame1.png`, `frame2.png`, ...)
- Audio file (e.g., `BadApple.wav`) in the project directory

## Getting Bad Apple Files
You can download the original Bad Apple!! video (`.mp4`) and audio (`.wav` or `.mp3`) files from the [Internet Archive](https://archive.org/). Search for "Bad Apple!!" to find various versions suitable for extracting frames and audio.

## Converting Files for EV3
Once you obtain the files, you will need to convert the video to PNG frames and ensure the audio is in WAV format. You can use `ffmpeg` for this:

**Convert video to PNG frames:**
```
ffmpeg -i .\bad_apple.mp4 -vf "fps=5,scale=178:128,format=gray" -f image2 -vcodec png .\frames\frame%d.png
```
- This command extracts frames at 5 FPS, scales them to 178x128 pixels (EV3 screen size), and converts them to grayscale PNGs.
- Place the resulting PNG files in the `frames/` directory.

**Convert audio to EV3-compatible WAV:**
```
ffmpeg -i .\bad_apple_enhanced.mp3 -ar 8000 -ac 1 -sample_fmt s16 BadApple.wav
```
- This command converts the audio to 8kHz, mono, 16-bit WAV format for EV3 compatibility.
- Place the resulting `BadApple.wav` file in the project root.

## Usage
1. Copy your PNG frames into the `frames/` directory.
2. Place your audio file (e.g., `BadApple.wav`) in the project root.
3. Adjust the `audio_duration_sec` variable in `main.py` to match your audio length (in seconds).
4. Run `main.py` on your EV3 Brick.

**Tip:** Due to the large number and size of frame files, it is recommended to transfer them to the EV3 using a USB connection instead of Wi-Fi for faster and more reliable transfer.

**Note:** Playback may take a bit of time to start because the program sorts all frame files before beginning. Please be patient after launching the script.

## Demo
Watch a demo of this project on YouTube: [https://youtu.be/ZXR68Vy5lU4](https://youtu.be/ZXR68Vy5lU4)

## How It Works
- The script loads and sorts all PNG frames numerically.
- It calculates the frame rate to match the audio duration.
- Audio playback starts in a separate thread for synchronization.
- Frames are displayed in sequence, skipping frames if playback falls behind.

## File Structure
```
main.py           # Main script to run on EV3
frames/           # Directory containing PNG frame images
    frame1.png
    frame2.png
    ...
BadApple.wav      # Audio file (must be present)
```

## Credits
- Inspired by "Bad Apple!!" and EV3 MicroPython community projects.

## License
This project is provided for educational and non-commercial use.

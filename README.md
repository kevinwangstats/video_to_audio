# Video to Audio Converter

This script allows you to convert video files into audio files using the command line. It uses FFmpeg, a powerful multimedia framework, to handle the conversion process.

## Features

- Convert various video formats to audio.
- Command line interface for easy use.
- Supports common video formats like .mp4, .mkv, .avi.
- Supports common audio formats like .mp3, .aac, .wav.

## Installation

Before using the script, ensure you have Python installed on your system. If not, download and install Python from [Python's official website](https://www.python.org/downloads/).

### Installing FFmpeg

The script requires FFmpeg to function. Follow these steps to install FFmpeg:

#### For Windows:

1. Download FFmpeg from [FFmpeg's official website](https://ffmpeg.org/download.html).
2. Extract the downloaded file.
3. Add the path to the FFmpeg bin directory to your system's PATH environment variable.

#### For macOS:

Use Homebrew to install FFmpeg:

```bash
brew install ffmpeg
```

#### For Linux 

Install FFmpeg using the package manager:

```bash 
sudo apt update
sudo apt install ffmpeg
```

### Python Dependencies
This script does not require any external Python libraries.

## Usage
To use the script, navigate to the directory containing the script and run it using Python. The script accepts two arguments: the path to the input video file and the path for the output audio file.

```bash
python main.py path_to_video_file path_to_audio_file
```

Replace script_name.py with the name of your script, path_to_video_file with the path to your video file, and path_to_audio_file with the desired path for the output audio file.


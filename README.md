# Text-Art-Generator

Join the [Discord server](https://discord.gg/VtARBeSn) to use it for free

![img](https://github.com/MuChi2112/Text-Art-Generator/blob/main/example_pic/example_pic.png?raw=true)

[picture](https://yt3.googleusercontent.com/roGS60A8a_lDbVakIg1JU3u3hbtjHSTilMGHMizuPKh7tuoY2nl46raxuW2f_83IKFGMjL6Z=s176-c-k-c0x00ffffff-no-rj) from Laplus Darknesss Youtube profile

## Overview
This script is designed to automate the process of downloading multiple `.ts` (Transport Stream) files from a specified base URL, merging them into a single file, and converting the result into an MP4 format. It is particularly useful for handling video streams segmented into multiple `.ts` files, a common practice in video streaming technologies.

## Prerequisites
Before running this script, ensure you have the following installed:
- Python 3.x
- `requests` library for Python (for downloading files)
- `ffmpeg` (for merging and converting files)

You can install the `requests` library using pip if you haven't already:
```bash
pip install requests
```

Ensure `ffmpeg` is installed and accessible from your system's PATH. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## How to Use
1. **Configuration**: Before running the script, you need to set up a few variables:
   - `save_path`: The directory where the `.ts` files will be downloaded and processed. This script will create the directory if it doesn't exist.
   - `start_file` and `end_file`: The range of file indexes to download. The script will download files starting from `start_file` to `end_file`, inclusive.
   - `base_url_front` and `base_url_end`: Parts of the URL that will be concatenated with the file index to form the full URL for downloading. The full URL is constructed as `base_url_front + str(i) + base_url_end` where `i` is the file index.
   - `video_name`: The desired name for the final MP4 video file.

2. **Running the Script**: With Python installed, run the script in a terminal or command prompt. Ensure you are in the directory containing the script or provide the full path to the script.

3. **Post-Execution**: After the script completes execution, the specified `save_path` directory will contain the final MP4 video file. All intermediary `.ts` files and the `filelist.txt` used for merging will be deleted to clean up the workspace.

## Notes
- The script includes error handling for HTTP requests, so it will notify you if any file fails to download due to network issues or incorrect URLs.
- The script uses `ffmpeg` with the `concat` protocol, which is a straightforward and efficient way to merge `.ts` files without re-encoding, preserving the original quality.
- This script assumes that all `.ts` files are named sequentially and can be sorted numerically to be merged in the correct order.

## Disclaimer
This script is provided as-is for educational purposes. Ensure you have the right to download and convert any content you use with this script. Respect copyright laws and the terms of service for any content you access.

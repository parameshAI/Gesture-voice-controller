<h1 align="center">🖐️ GestureVoice Controller</h1>

<p align="center">
  <b>A hands-free Human-Computer Interaction (HCI) system that replaces the physical mouse and keyboard with real-time hand gesture recognition and voice command automation.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-00897B" />
  <img src="https://img.shields.io/badge/SpeechRecognition-Voice%20Control-orange" />
  <img src="https://img.shields.io/badge/Platform-Windows-blue?logo=windows" />
</p>

---

## Overview

GestureVoice Controller is a multimodal AI application that bridges human intent and computer action using nothing but a webcam and a microphone — no extra hardware required.

It combines **Computer Vision** (MediaPipe + OpenCV) for zero-lag hand tracking with **Natural Language Processing** (SpeechRecognition) for voice-driven automation, running fully in real time.

## Demo

| Gesture Control | Voice Control |
|---|---|
| [![Gesture Control Demo](https://img.youtube.com/vi/R7kq_zB7lVY/hqdefault.jpg)](https://youtube.com/shorts/R7kq_zB7lVY?si=DtIrsv_yobOAdZ1M) | [![Voice Control Demo](https://img.youtube.com/vi/mRodbF2DyU4/hqdefault.jpg)](https://youtube.com/shorts/mRodbF2DyU4?si=QdcMCdKV-WalB33j) |
| Zero-latency cursor move, click, and drag using MediaPipe hand tracking | Opening apps and controlling the system with voice commands |

*(Click either thumbnail to watch on YouTube)*

## Features

| Gesture / Command | Action |
|---|---|
| Right hand move | Move cursor |
| Right hand pinch | Left click |
| Right hand pinch + hold | Click and drag |
| Left hand pinch | Volume down |
| Left hand open palm | Volume up |
| Left hand peace sign | Right click |
| Voice: "Open Chrome" | Opens Chrome |
| Voice: "Open Notepad" | Opens Notepad |
| Voice: "Stop" / "Exit" | Closes the app |

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| OpenCV | Camera feed and frame processing |
| MediaPipe | Hand landmark detection |
| PyAutoGUI | Mouse and keyboard automation |
| SpeechRecognition | Voice command processing |
| pyttsx3 | Text-to-speech AI response |

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/parameshAI/GestureVoice-Controller
cd GestureVoice-Controller
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
python main.py
```

> **Note:** `pyaudio` (used by `SpeechRecognition`) needs PortAudio installed on some systems. On Windows, `pip install pyaudio` usually works out of the box; on macOS/Linux you may need `brew install portaudio` or `sudo apt install portaudio19-dev` first.

## How to Use

**Gesture Control**
- Place your right hand in front of the webcam to move the cursor
- Pinch index finger and thumb together to click
- Hold the pinch for more than 0.4 seconds to click-and-drag
- Use your left hand for volume control and right-click (see table above)

**Voice Control**
- Press the `S` key to activate the microphone
- Speak clearly: *"Open Chrome"*, *"Open Notepad"*
- The AI confirms and executes the command aloud

## How It Works

```
Webcam Feed
   ↓
MediaPipe Hand Landmark Detection
   ↓
Gesture Logic (distance & position thresholds)
   ↓
PyAutoGUI executes the action
   ↓
"S" key press → SpeechRecognition triggered
   ↓
Google Speech API transcribes voice
   ↓
Command parsed and executed via PyAutoGUI
```

## Future Improvements

- [ ] Scroll gesture support
- [ ] Custom, user-defined voice command mapping
- [ ] Multi-language voice support
- [ ] Linux and macOS compatibility
- [ ] GUI settings panel

## Author

**Parameshwar D.**
B.Sc. Artificial Intelligence & Machine Learning, St. Joseph's College (Autonomous), Tiruchirappalli

[![GitHub](https://img.shields.io/badge/GitHub-parameshAI-181717?logo=github)](https://github.com/parameshAI)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/parameshwar-d-612b06391)

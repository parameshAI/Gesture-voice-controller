# GestureVoice Controller

> A hands-free Human-Computer Interaction (HCI) system that replaces the physical mouse and keyboard using real-time Hand Gesture Recognition and Voice Command Automation.
> 
GESTUREVOICE-CONTROLLER is a futuristic, hands-free interface that lets you control your Windows computer using AI. It replaces your physical mouse and keyboard with *Hand Gestures* and *Voice Commands*.

It uses *Computer Vision* (to track your fingers) and *Natural Language Processing* (to listen to commands) in real-time.

---

## Overview

GestureVoice Controller is a multimodal AI application built for Windows that bridges the gap between human intent and computer action — using only a webcam and a microphone.

It combines **Computer Vision** (MediaPipe + OpenCV) for zero-lag hand tracking and **Natural Language Processing** (SpeechRecognition) for voice-driven automation — with no additional hardware required.

---

## Demo

### Gesture Control





### Gesture Control Demo
https://youtube.com/shorts/R7kq_zB7lVY?si=DtIrsv_yobOAdZ1M
*Using MediaPipe to control the mouse, click, and drag with zero latency.*

### Voice Control Demo
https://youtube.com/shorts/mRodbF2DyU4?si=QdcMCdKV-WalB33j
*Using SpeechRecognition to open applications and control the system via voice.*



---

## Features

| Gesture / Command | Action |
|---|---|
| Right hand move | Move cursor |
| Right hand pinch | Left click |
| Right hand pinch + hold | Click and drag |
| Left hand pinch | Volume down |
| Left hand open palm | Volume up |
| Left hand peace sign | Right click |
| Voice: Open Chrome | Opens Chrome |
| Voice: Open Notepad | Opens Notepad |
| Voice: Stop or Exit | Closes the app |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| OpenCV | Camera feed and frame processing |
| MediaPipe | Hand landmark detection |
| PyAutoGUI | Mouse and keyboard automation |
| SpeechRecognition | Voice command processing |
| pyttsx3 | Text-to-speech AI response |

---

## Installation

**Step 1 — Clone the repository**

    git clone https://github.com/parameshAI/GestureVoice-Controller
    cd GestureVoice-Controller

**Step 2 — Install dependencies**

    pip install opencv-python mediapipe pyautogui SpeechRecognition pyttsx3 pyaudio

**Step 3 — Run the application**

    python gesture_voice_controller.py
## How to Use

**Gesture Control**

- Place your right hand in front of the webcam to move the cursor
- Pinch index finger and thumb to click
- Hold pinch for more than 0.4 seconds to drag
- Use your left hand
**Voice Control**

- Press the S key to activate the microphone
- Speak clearly: Open Chrome, Open Notepad
- The AI will confirm and execute the command
## How It Works

    Webcam Feed
    ↓
    MediaPipe Hand Landmark Detection
    ↓
    Gesture Logic
    ↓
    PyAutoGUI executes action
    ↓
    SpeechRecognition triggered by S key
    ↓
    Google Speech API transcribes voice
    ↓
    Command executed via PyAutoGUI
## Future Improvements

- Scroll gesture support
- Custom voice command mapping
- Multi-language voice support
- Linux and macOS compatibility
- GUI settings panel

## Author
Parameshwar D.
B.Sc Artificial Intelligence and Machine Learning
St. Joseph's College (Autonomous), Tiruchirappalli
GitHub: https://github.com/parameshAI
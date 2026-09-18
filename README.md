Voice Controlled Mouse

A Python-based voice-controlled mouse system that allows users to operate the computer cursor and perform mouse actions using spoken commands.

Features

- Voice-based cursor movement
- Move cursor left, right, up, and down
- Adjustable movement distance
- Move cursor to screen center
- Left click
- Right click
- Double click
- Scroll up and down
- Voice-based stop command
- Microphone noise calibration
- Dynamic speech recognition
- Simple command-based interaction

Technologies Used

- Python
- SpeechRecognition
- PyAudio
- PyAutoGUI

How It Works

The system captures the user's voice through the microphone and converts the speech into text using speech recognition. The recognized command is processed and mapped to a corresponding mouse action using PyAutoGUI.

Workflow

Voice Input
↓
Microphone
↓
Speech Recognition
↓
Command Processing
↓
Command Matching
↓
PyAutoGUI
↓
Mouse Action

Supported Commands

- "Move left"
- "Move right"
- "Move up"
- "Move down"
- "Move left 300"
- "Move right 500"
- "Move to center"
- "Click"
- "Right click"
- "Double click"
- "Scroll up"
- "Scroll down"
- "Stop"

Installation

Clone the repository:

bash
git clone https://github.com/jerindhas-cmd/Voice-Controlled-Mouse.git

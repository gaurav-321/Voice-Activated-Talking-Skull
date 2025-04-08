# Voice-Activated Talking Skull 🎢

## Description
The **Voice-Activated Talking Skull** is a project that combines voice recognition with computer vision to create an interactive animation. It detects speech using the `SoundDevice` library and controls the animation of a skull image based on whether someone is speaking or silent.

## Features
- Real-time speech detection
- Dynamic skull animation based on sound activity
- User-friendly interface displaying current state

## Installation
To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gag3301v/Voice-Activated-Talking-Skull.git
   cd Voice-Activated-Talking-Skull
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Here’s how you can run the project:

```python
# Run the main script
python main.py
```

### Example Code Snippets

#### Detecting Speech
```python
import sounddevice as sd
import numpy as np

def detect_speech(audio_data):
    # Analyze audio data to determine if speech is present
    threshold = 0.1
    return np.max(np.abs(audio_data)) > threshold
```

#### Animating the Skull
```python
import cv2
import os

def animate_skull(is_speaking):
    # Update the animation state of the skull image
    skull_image_path = "skull.png" if is_speaking else "skull_sleeping.png"
    skull_image = cv2.imread(skull_image_path)
    cv2.imshow("Skull Animation", skull_image)
```

## Configuration
- **Environment Variables**: None required for basic operation.
- **Config Files**: No configuration files are needed.

## Tests
This project includes unit tests to ensure the functionality works as expected. To run the tests:

```bash
python -m unittest discover tests/
```

## Project Structure
```plaintext
Voice-Activated-Talking-Skull/
├── README.md
├── requirements.txt
└── main.py
```

## Contributing
Contributions are welcome! Please follow these guidelines to get started:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore and contribute to this exciting project! 🎉
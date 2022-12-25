# Voice Activated Talking Skull
This project uses the SoundDevice and OpenCV libraries to create a voice activated skull animation. When the user is speaking, the skull will animate and display "talking". When the user is silent, the skull will display "waiting".

## Dependencies
- SoundDevice
- NumPy
- OpenCV
## How to Use
Clone the repository and navigate to the directory:
```
git clone https://github.com/USERNAME/REPO.git
cd REPO
```
Run the script:
```
python main.py
```
The program will begin measuring the ambient sound volume to determine the threshold for detecting speech.

Once the threshold has been established, the skull animation will start and will display "talking" or "waiting" based on whether the user is speaking or not.

Press "q" to quit the program.

## Customization
The sensitivity of the speech detection can be adjusted by changing the value of the "volume_norm" variable in the "silent" function. This value represents the volume of the ambient sound and is compared to the mean volume when the user is silent, which is calculated at the beginning of the program.

## Acknowledgements
This project was inspired by the tutorial [Voice Activated LED with Python and a Microphone](https://towardsdatascience.com/voice-activated-led-with-python




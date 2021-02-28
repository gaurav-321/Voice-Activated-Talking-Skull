import sounddevice as sd
import numpy as np
import os
import time as t
from threading import Thread

sound_volume = []

last_word = []


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    sound_volume.append(volume_norm)


def silent(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm < float(np.array(sound_volume).mean()) + float(np.array(sound_volume).mean()) / 100 * 60:
        current_word = 'silent'
    else:
        current_word = 'talking'
    last_word.append(current_word)
<<<<<<< HEAD
    t.sleep(0.1)
=======
    t.sleep(0.05)
>>>>>>> Initial commit


def cv2():
    import cv2
    images = ["gif/Layer 1.png", "gif/Layer 2.png", "gif/Layer 3.png"]
    current_img = 0
    while True:
        text = 'Waiting' if len(last_word) == 0 else "Ready"
        if current_img == 3:
            current_img = 0
        if len(last_word) > 1 and last_word[-1] == "talking":
            image = cv2.imread(images[current_img])
            current_img += 1
        else:
            image = cv2.imread(images[0])
        cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
        cv2.imshow("skull", image)
        if cv2.waitKey(80) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    quit()


Thread(target=cv2).start()
print("Finding mean volume when silent")
with sd.Stream(callback=print_sound):
    sd.sleep(1000)

with sd.Stream(callback=silent):
    sd.sleep(1000000)
    quit()

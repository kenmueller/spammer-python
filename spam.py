from pynput.keyboard import Key, Controller
import time

message = input('Spam message: ')
count = input('Spam count: ')

for i in range(5):
	print(str(5 - i) + '...')
	time.sleep(1)

keyboard = Controller()

def pressKey(key):
	keyboard.press(key)
	keyboard.release(key)

for i in range(int(count)):
	for letter in message:
		pressKey(letter)
	pressKey(Key.enter)
	time.sleep(0.01)
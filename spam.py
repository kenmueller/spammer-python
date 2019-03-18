from pynput.keyboard import Key, Controller
import time, math

message = input('Spam message: ')
count = int(input('Spam count: '))

for i in range(5):
	print(str(5 - i) + '...')
	time.sleep(1)

keyboard = Controller()

def pressKey(key):
	keyboard.press(key)
	keyboard.release(key)

for i in range(count):
	progress = math.floor(i / count * 15)
	print(('[' + ('=' * progress + '>' + '.' * (15 - progress))[1:])[:-2] + ']', end='\r')
	for letter in message:
		pressKey(letter)
	pressKey(Key.enter)
	time.sleep(0.05)

print('Done           ')
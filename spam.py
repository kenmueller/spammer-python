from pynput.keyboard import Key, Controller
import time, math

message = input('Spam message: ')
count = int(input('Spam count: '))

for i in range(5):
	print(str(5 - i) + '...')
	time.sleep(1)

keyboard = Controller()
waitTime = 0.01 * len(message)

def pressKey(key):
	keyboard.press(key)
	keyboard.release(key)

for i in range(count):
	progress = math.floor(i / count * 15)
	print(('[' + ('=' * progress + '>' + '.' * (15 - progress))[1:])[:-2] + ']', end='\r')
	keyboard.type(message)
	pressKey(Key.enter)
	time.sleep(waitTime)

print('Done           ')
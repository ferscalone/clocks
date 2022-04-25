import winsound, time


def sound(sound_type):
	i = 60 // sound_type
	for i in range(i):
		winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
		time.sleep(sound_type)

def alarm(n):			
	sound_type = int(input('Выберите тип звонка:\n(1) Обычный\n(6) Утренний\n: '))
	print("Время ожидания:", n, "секунд(у/ы).")
	time.sleep(n)
	
	sound(sound_type)

def input_destinations(user_input):
	text = user_input.split(':')
	wait_time = int(text[0]) * 3600 + int(text[1]) * 60 + int(text[2])
	alarm(wait_time)


print('Это таймер!')
print('Формат "Часы:Минуты:Секунды"\n')

user_input = input("Введите время в правильном формате: ")
	
input_destinations(user_input)
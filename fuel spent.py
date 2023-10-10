time_spent = int(input())
av_speed = int(input())

distance = time_spent * av_speed
liters = distance / 12

print(f'{liters:.3f}')
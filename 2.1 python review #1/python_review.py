import random

temperatures = []
good_days_count = 0

for x in range(7) :
	random_temp = random.randint(26,40)
	random_temps_list = temperatures.append(random_temp)

# print(temperatures)

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

days_with_even_temperature = []
for i in range(7) :
	if temperatures[i] % 2 ==0 :
		good_days_count += 1
		days_with_even_temperature.append(days_of_the_week[i])

# print(good_days_count)
# print(days_with_even_temperature)

highest_temp = max(temperatures)
highest_temp_index= temperatures.index(highest_temp)

# print(days_of_the_week[highest_temp_index])

lowest_temp = min(temperatures)
lowest_temp_index= temperatures.index(lowest_temp)

# print(days_of_the_week[lowest_temp_index])

average_temp = sum(temperatures)/7
above_avg = []

for p in range(7):
	if temperatures[p] > average_temp:
		above_avg.append(temperatures[p])
# print(above_avg)


print("The weather report:")
for i in range(7):
	print(str(days_of_the_week[i]) + ":" + str(temperatures[i]))
print(f"Shelly has {good_days_count} good days")
print(f"The hottest temperature was : {highest_temp} on {days_of_the_week[highest_temp_index]}")
print(f"The hottest temperature was : {lowest_temp} on {days_of_the_week[lowest_temp_index]}")
print(f"The average temperature is {average_temp}")
print(f"days above average {above_avg}")

temperatures.sort()
print(temperatures)
def dragon_adding(type_of_dragons, name, damage, health, armor):
    if type_of_dragons not in dragon_dict:
        dragon_dict[type_of_dragons] = {}
        dragon_dict[type_of_dragons][name] = [damage, health, armor]
    else:
        if name not in dragon_dict:
            dragon_dict[type_of_dragons][name] = [damage, health, armor]
        else:
            dragon_dict[type_of_dragons][name] = [damage, health, armor]


def stats(types):
    for name in dragon_dict[types]:
        for index, value in enumerate(dragon_dict[types][name]):
            if value == "null":
                if index == 0:
                    dragon_dict[types][name][index] = 45
                elif index == 1:
                    dragon_dict[types][name][index] = 250
                elif index == 2:
                    dragon_dict[types][name][index] = 10
            else:
                dragon_dict[types][name][index] = int(dragon_dict[types][name][index])


def average():
    my_list = []
    for statistic, statistics in values.items():
        my_list.append(statistics)
        zipped_list = zip(*my_list)
        average_dragon_stats[key] = [f"{sum(z) / len(z):.2f}" for z in zipped_list]


numbers_of_dragons = int(input())

dragon_dict = {}
average_dragon_stats = {}

for _ in range(numbers_of_dragons):
    dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = input().split()
    dragon_adding(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

for dragon_type in dragon_dict:
    stats(dragon_type)

for key, values in dragon_dict.items():
    average()

if dragon_dict:
    for color, average_stats in average_dragon_stats.items():
        print(f"{color}::({average_stats[0]}/{average_stats[1]}/{average_stats[2]})")
        for names, stats in sorted(dragon_dict[color].items(), key=lambda kvp: kvp[0]):
            print(f"-{names} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
def farm_action(weather, time_of_day, cows_need_milking, cows_location, season,
                slurry_tank_full, grass_long):

    moved_cows = False

    if time_of_day == 'night' and weather == 'rainy' and cows_location != 'cowshed':
        print('take cows to cowshed')
    elif cows_need_milking:
        if cows_location != 'cowshed':
            print('take cows to cowshed')
            moved_cows = True
        print('milk cows')
        if moved_cows:
            print('take cows back to pasture')
    elif slurry_tank_full and weather != 'sunny' and weather != 'windy':
        if cows_location != 'cowshed':
            print('take cows to cowshed')
            moved_cows = True
        print('fertilize pasture')
        if moved_cows:
            print('take cows back to pasture')
    elif grass_long and season == 'spring' and weather == 'sunny':
        if cows_location == 'pasture':
            print('take cows to cowshed')
            moved_cows = True
        print('mow grass')
        if moved_cows:
            print('take cows back to pasture')
    else:
        print('wait')

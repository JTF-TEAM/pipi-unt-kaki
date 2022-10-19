import genshinstats as gs
gs.set_cookie(ltuid=119480035, ltoken="cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT")

uid = 710785423
data = gs.get_user_stats(uid)
total_characters = len(data['characters'])
print('user "sadru" has a total of', total_characters, 'characters')

stats = gs.get_user_stats(uid)['stats']
for field, value in stats.items():
    print(f"{field}: {value}")

characters = gs.get_characters(uid)
for char in characters:
    print(f"{char['rarity']}* {char['name']:10} | lvl {char['level']:2} C{char['constellation']}")
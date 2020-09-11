import perlin
from graphics import *
import emojis as emj

noise_factory = perlin.PerlinNoiseFactory(2,octaves=3)

noise = [[0 for x in range(100)] for y in range(100)]

map = ''

for i in range(100):
    for j in range(100):
        noise[i][j] = noise_factory(i/10,j/10)

        if noise[i][j] < 0.0:
            map += emj.wave_emoji
        elif noise[i][j] < 0.15:
            map += emj.beach_emoji
        elif noise[i][j] < 0.5:
            map += emj.forest_emoji
        elif noise[i][j] < 1:
            map += emj.mountain_emoji
        else:
            map += '1'
    map += '\n'

print(noise)
print(map)
print('\N{grinning face with smiling eyes}')

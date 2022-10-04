from perlin_noise import PerlinNoise


noise = PerlinNoise(octaves=2, seed=12)
for x in range(10):
    for y in range(10):
        print(noise([x/10, y/10]))
        redness = int(200 * (noise([x/10, y/10])))
        print(redness)

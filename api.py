import os
import sys

import pygame
import requests

# 65.550300 57.143112
ll = "65.550300 57.143112".split(' ')
ll = ','.join(ll)
zoom = 18
map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.remove(map_file)
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                l = ll.replace(',', ' ').split()
                s = float(l[0])
                if zoom < 5:
                    s -= 3
                elif 5 < zoom < 10:
                    s -= 0.1
                else:
                    s -= 0.002
                ll = f'{s},{l[-1]}'
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)

                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_RIGHT:
                l = ll.replace(',', ' ').split()
                s = float(l[0])
                if zoom < 5:
                    s += 3
                elif 5 < zoom < 10:
                    s += 0.1
                else:
                    s += 0.002
                ll = f'{s},{l[-1]}'
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)

                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_UP:
                l = ll.replace(',', ' ').split()
                s = float(l[0])
                if zoom < 5:
                    s -= 3
                elif 5 < zoom < 10:
                    s -= 0.1
                else:
                    s -= 0.002
                ll = f'{l[0]},{s}'
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)

                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_DOWN:
                l = ll.replace(',', ' ').split()
                s = float(l[0])
                if zoom > 5:
                    s -= 3
                elif 5 < zoom < 10:
                    s -= 0.1
                else:
                    s -= 0.002
                ll = f'{l[0]},{s}'
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)

                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_PAGEUP:
                if zoom + 1 != 20:
                    zoom += 1
                else:
                    pass
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()
            if event.key == pygame.K_PAGEDOWN:
                if zoom - 1 != 0:
                    zoom -= 1
                else:
                    pass
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&z={zoom}&l=map"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)

                screen.blit(pygame.image.load(map_file), (0, 0))
                pygame.display.update()

# 57.143112 65.550300
# 65.550300 57.143112

import requests
import json

response = requests.request("GET", "https://codember.dev/colors.txt")

zebra = response.text
zebra = json.loads(zebra)

def solution(zebra):
    first_color = None
    second_color = None

    count = 0
    max_count = 0

    last_color = None
    max_last_color = None

    for i in range(0, len(zebra)):
        print(zebra[i], count, last_color, max_count, max_last_color)
        # First item
        if i == 0:
            first_color = zebra[i]
            count += 1
            last_color = zebra[i]

        if zebra[i-1] == first_color and second_color == None:
            # If same color as first continue
            if first_color == zebra[i]:
                continue
            second_color = zebra[i]
            count += 1
            last_color = zebra[i]
        elif zebra[i-1] == second_color and zebra[i] == first_color:
            count += 1
            last_color = zebra[i]
        elif zebra[i-1] == first_color and zebra[i] == second_color:
            count += 1
            last_color = zebra[i]
        elif zebra[i-1] == second_color and zebra[i] != first_color:
            # Get last count if equals max_count
            if count >= max_count:
                max_count = count
                max_last_color = last_color
            count = 2
            first_color = second_color
            second_color = zebra[i]
            last_color = zebra[i]
        elif zebra[i-1] == first_color and zebra[i] != second_color:
            # Get last count if equals max_count
            if count >= max_count:
                max_count = count
                max_last_color = last_color
            count = 2
            second_color = zebra[i]
            last_color = zebra[i]

    if max_count == 0 or count >= max_count:
        max_count = count
        max_last_color = last_color

    print("Result:", max_count, max_last_color)

    return max_count, max_last_color

solution(zebra)
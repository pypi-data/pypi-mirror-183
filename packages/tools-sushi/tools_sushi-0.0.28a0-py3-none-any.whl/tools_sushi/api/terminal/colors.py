class colors():
    black = (0, 0, 0)
    white = (255, 255, 255)

    red = (229, 57, 53)
    light_red = (239, 83, 80)

    blue = (30, 136, 229)
    light_blue = (100, 181, 246)

    green = (67, 160, 71)
    light_green = (129, 199, 132)

    yellow = (255, 235, 59)
    light_yellow = (255, 241, 118)

    orange = (255, 160, 0)
    light_orange = (255, 167, 38)

    grey = (69, 90, 100)
    light_grey = (144, 164, 174)


def print_colors(content: str, rgb) -> str:
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{content}\033[0m"

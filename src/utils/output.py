import common.config as cf


def print_color(text: str, color: str):
    color_low = color.strip().lower()
    color_print = ""

    for i in range(len(cf.COLORS[0])):
        if color_low == cf.COLORS[0][i]:
            color_print = cf.COLORS[1][i]
            break

    print(color_print + text + cf.COLORS[1][-1])

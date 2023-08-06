from .utils import get_random_color, get_unit, render

ELEMENTS = 3
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash(name)

    return [
        {
            "color": get_random_color(num_from_name + i, colors, len(colors)),
            "translate_x": get_unit(num_from_name * (i + 1), SIZE / 10, 1),
            "translate_y": get_unit(num_from_name * (i + 1), SIZE / 10, 2),
            "scale": 1.2 + get_unit(num_from_name * (i + 1), SIZE / 20) / 10,
            "rotate": get_unit(num_from_name * (i + 1), 360, 1),
        }
        for i in range(ELEMENTS)
    ]


def marble(name, colors):
    properties = generate_colors(name, colors)
    return render("marble.svg", {"properties": properties, "SIZE": SIZE, "size": "80"})

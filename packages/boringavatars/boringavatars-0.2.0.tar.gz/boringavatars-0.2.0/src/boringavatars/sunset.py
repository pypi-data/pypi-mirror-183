import hashlib

from .utils import get_random_color, render

ELEMENTS = 4
SIZE = 80


def generate_colors(name, colors):
    num_from_name = hash(name)
    return [
        get_random_color(num_from_name + i, colors, len(colors))
        for i in range(ELEMENTS)
    ]


def sunset(name, colors, square):
    sunset_colors = generate_colors(name, colors)
    name = hashlib.sha1(name.encode("utf-8")).hexdigest()
    return render(
        "sunset.svg",
        {
            "sunset_colors": sunset_colors,
            "name": name,
            "SIZE": SIZE,
            "size": "80",
            "square": square,
        },
    )

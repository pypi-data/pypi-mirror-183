from .bauhaus import bauhaus
from .beam import beam
from .marble import marble
from .pixel import pixel
from .ring import ring
from .sunset import sunset

__version__ = "0.1.0"

__all__ = ["avatar"]

DEFAULT_COLORS = ["FFAD08", "EDD75A", "73B06F", "0C8F8F", "405059"]

VARIANTS = {
    "beam": beam,
    "marble": marble,
    "pixel": pixel,
    "sunset": sunset,
    "bauhaus": bauhaus,
    "ring": ring,
}


def avatar(name, colors=DEFAULT_COLORS, variant="beam"):
    if variant not in VARIANTS:
        raise ValueError(f"unrecognized variant: {variant}")

    fn = VARIANTS[variant]
    colors = [c.lstrip("#") for c in colors]
    return fn(name, colors)

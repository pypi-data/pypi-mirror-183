import colorsys
from typing import Iterator
import random


class ColorGenerator:
    @staticmethod
    def _rgb_to_hex(rgb: tuple[float, float, float]):
        result = "#"
        for component in rgb:
            result += hex(int(component*255))[2:].rjust(2, "0")
        return result

    @classmethod
    def _h_to_hex(cls, h: float):
        rgb = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        hex = cls._rgb_to_hex(rgb)
        return hex

    @classmethod
    def _color_generator_function(cls) -> Iterator[str]:
        yield cls._h_to_hex(0)
        old_h_list: list[float] = [0, 1]
        while 1:
            colors: list[str] = []
            new_h_list: list[float] = []
            for old_h_number in range(len(old_h_list)-1):
                h = (old_h_list[old_h_number] + old_h_list[old_h_number+1])/2
                new_h_list += [old_h_list[old_h_number], h]
                colors.append(cls._h_to_hex(h))
            random.shuffle(colors)
            yield from colors
            new_h_list.append(1)
            old_h_list = new_h_list

    def __init__(self):
        self._generator = self._color_generator_function()

    def __next__(self):
        return next(self._generator)
    
    def __iter__(self):
        return self

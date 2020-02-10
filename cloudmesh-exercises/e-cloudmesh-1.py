# sp20-516-233 E.Cloudmesh.Common.1

# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE


def marshmallow_verbose(marshmallow_box):
    """Usage: displays the number of MarshmallowPeep objects for each color
        Arguments:
            MARSHMALLOW_BOX   A list of MarshmallowPeep objects
    """
    color_count = {"pink": 0, "yellow": 0}
    for m in marshmallow_box:
        if m.get_color() == "pink":
            color_count["pink"] += 1
        if m.get_color() == "yellow":
            color_count["yellow"] += 1
    VERBOSE(color_count)


class MarshmallowPeep(object):
    def __init__(self, shape, color):
        """Usage: creates a MarshmallowPeep object
            Arguments:
                SHAPE   The shape of the marshmallow peep.
                Color   The color of the marshmallow peep.
        """
        self._shape = shape
        self._color = color

    def get_shape(self):
        return self._shape.lower()

    def get_color(self):
        return self._color.lower()

    def marshmallow_banner(self):
        """Usage: creates a banner for the MarshmallowPeep object
        """
        message = self._color + " " + self._shape + " Banner"
        if self._color.lower() == "pink":
            banner(txt=message, c="=", color="RED")
        elif self._color.lower() == "yellow":
            banner(txt=message, c="=", color="GREEN")
        else:
            banner(txt=message, c="=", color="BLUE")

    def marshmallow_heading(self):
        """Usage: creates a header for the MarshmallowPeep object
        """
        message = self._color + " " + self._shape + " Heading"
        HEADING(txt=message, c="*")


if __name__ == '__main__':
    pinkRabbit = MarshmallowPeep("Rabbit", "Pink")
    yellowChick = MarshmallowPeep("Chick", "Yellow")
    marshmallowBox = [pinkRabbit, yellowChick]

    pinkRabbit.marshmallow_banner()
    pinkRabbit.marshmallow_heading()

    yellowChick.marshmallow_banner()
    yellowChick.marshmallow_heading()

    print("Contents of marshmallow box")
    marshmallow_verbose(marshmallowBox)

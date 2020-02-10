# sp20-516-233 E.Cloudmesh.Common.2

# Develop a program that demonstrates the use of dotdict
from cloudmesh.common.dotdict import dotdict


def need_more_pink(box):
    """Usage: tells whether more pink marshmallows are needed
        Arguments:
            BOX   A dictionary of marshmallows and their counts
    """
    total_pink = box.pink_rabbits + box.pink_chicks
    total_yellow = box.yellow_rabbits + box.yellow_chicks
    if total_pink < total_yellow:
        return True
    else:
        return False


if __name__ == '__main__':
    marshmallow_box = {"pink_rabbits": 7, "yellow_rabbits": 5,
                       "pink_chicks": 3, "yellow_chicks": 8}

    marshmallow_box = dotdict(marshmallow_box)

    if need_more_pink(marshmallow_box):
        print("Need more pink marshmallows!")
        print("Number of pink rabbits: " + str(marshmallow_box.pink_rabbits))
        print("Number of pink chicks: " + str(marshmallow_box.pink_chicks))
    else:
        print("Enough pink marshmallows")

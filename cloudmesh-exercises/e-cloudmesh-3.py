# sp20-516-233 E.Cloudmesh.Common.3

# Develop a program that demonstrates the use of FlatDict
from cloudmesh.common.FlatDict import FlatDict
from pprint import pprint

if __name__ == '__main__':
    print("original dictionary structure:")
    pie = {"type": "Apple",
           "flavor": "Sweet",
           "ingredients": {"crust": ["flour", "butter", "eggs"],
                           "filling": ["apples", "sugar", "cinnamon"]}}
    pprint(pie)
    print()
    print("flat dictionary:")
    flat_pie = FlatDict(pie, sep=".")
    for fp in flat_pie:
        print(fp, flat_pie[fp])

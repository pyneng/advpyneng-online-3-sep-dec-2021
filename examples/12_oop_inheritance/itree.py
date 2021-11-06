import inspect
from scrapli.driver.core import IOSXEDriver
from rich.tree import Tree
from rich import print as rprint


def rtree(cls, tree=None):
    if not inspect.isclass(cls):
        cls = type(cls)
    if tree is None:
        tree = Tree(f"{cls.__name__}")
    else:
        tree = tree.add(f"{cls.__name__}")
    bases = [c for c in cls.__bases__ if c is not object]
    if bases:
        for base in bases:
            rtree(base, tree)
    return tree


if __name__ == "__main__":
    tree = rtree(IOSXEDriver)
    rprint(tree)

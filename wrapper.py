import main
from main import *
import importlib

print("Generating Tree...")
node:Node = Node(arr, 1)
print("Done")
main.node = node
main.ex()

inp = ""
while inp != "quit":
    inp = input("Type anything to reload or 'quit' to quit\n")
    importlib.reload(main)
    main.node = node
    main.ex()
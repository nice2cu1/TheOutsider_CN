import UnityPy
import os

if __name__ == '__main__':
    env = UnityPy.load('darkbundle')

    for obj in env.objects:
        if obj.type.name == "TextAsset":
            data = obj.read()
            with open("./Export/TextAsset/"+data.name+".xml", "wb") as f:
                f.write(bytes(data.script))
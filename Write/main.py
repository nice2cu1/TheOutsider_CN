import UnityPy
import os
import time


if __name__ == '__main__':
    start = time.perf_counter()
    
    env = UnityPy.load('darkbundle')
    for obj in env.objects:
         if obj.type.name == "TextAsset":
            data = obj.read()
            with open("./Export/TextAsset/"+data.name+".xml", "rb") as f:
                data.script = f.read()
            data.save()
    with open(os.path.join("C:\\Users\\Administrator\\AppData\\Roaming\\OuterWildsModManager\\OWML\\Mods\\StreetlightsBehindtheTreesandnice2cu1.TheOutsider\\darkbundle"), "wb") as f:
        f.write(env.file.save(packer='lz4'))
    end = time.perf_counter() 
    print('运行时间为：{}秒'.format(end-start))




import json
from .merge import merge
from os.path import split, exists, join
from copy import deepcopy  # fuck this
db = {
    "rail": {
        "flat": [
            "./assets/minecraft/models/block/rail_flat.json"
        ],
        "raised": [
            "./assets/minecraft/models/block/rail_raised.json"
        ]
    },
    "activator": {
        "flat": [
            "./assets/minecraft/models/block/activator_rail/flat_off.json",
            "./assets/minecraft/models/block/activator_rail/flat_on.json"
        ],
        "raised": [
            "./assets/minecraft/models/block/activator_rail/raised_off.json",
            "./assets/minecraft/models/block/activator_rail/raised_on.json"
        ]
    },
    "detector": {
        "flat": [
            "./assets/minecraft/models/block/detector_rail/flat_off.json",
            "./assets/minecraft/models/block/detector_rail/flat_on.json"
        ],
        "raised": [
            "./assets/minecraft/models/block/detector_rail/raised_off.json",
            "./assets/minecraft/models/block/detector_rail/raised_on.json"
        ]
    },
    "powered": {
        "flat": [
            "./assets/minecraft/models/block/powered_rail/flat_off.json",
            "./assets/minecraft/models/block/powered_rail/flat_on.json"
        ],
        "raised": [
            "./assets/minecraft/models/block/powered_rail/raised_off.json",
            "./assets/minecraft/models/block/powered_rail/raised_on.json"
        ]
    }
}
tdb = deepcopy(db)
for t in tdb:
    for state in tdb[t]:
        for i in range(len(tdb[t][state])):
            _path, _file = split(tdb[t][state][i])
            path = join(_path, "_"+_file)
            tdb[t][state][i] = path


def rail_raised():
    with open("./assets/minecraft/models/block/_rail_raised.json") as file:
        return merge(json.load(file))


def rail_flat():
    with open("./assets/minecraft/models/block/_rail_flat.json") as file:
        return merge(json.load(file))


def activator_rail_flat_on():
    with open("./assets/minecraft/models/block/activator_rail/_flat_on.json") as file:
        _rail_flat = rail_flat()
        jf = merge(json.load(file))
        merge(jf, _rail_flat)
        # VSCODE BUG: you can't find/replace multiline selection, only if you copy-paste it!
        # for texture in _rail_flat["textures"]:
        # 	jf["textures"][texture] = _rail_flat["textures"][texture]
        # for el in _rail_flat["elements"]:
        # 	add(jf["elements"], el)
        return jf


def activator_rail_flat_off():
    _ = activator_rail_flat_on()
    _["textures"]["detail"] = "block/activator_rail"
    return _


def activator_rail_raised():
    with open("./assets/minecraft/models/block/activator_rail/_raised_on.json") as file:
        __rail = rail_raised()
        jf = merge(json.load(file))
        return merge(jf, __rail)


def detector_rail_flat_on():
    __rail = rail_flat()
    with open("./assets/minecraft/models/block/detector_rail/_flat_on.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def detector_rail_flat_off():
    __rail = rail_flat()
    with open("./assets/minecraft/models/block/detector_rail/_flat_off.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def detector_rail_raised_on():
    __rail = rail_raised()
    with open("./assets/minecraft/models/block/detector_rail/_raised_on.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def detector_rail_raised_off():
    __rail = rail_raised()
    with open("./assets/minecraft/models/block/detector_rail/_raised_off.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def powered_rail_flat_on():
    __rail = activator_rail_flat_on()
    with open("./assets/minecraft/models/block/powered_rail/_flat_on.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def powered_rail_flat_off():
    __rail = activator_rail_flat_off()
    with open("./assets/minecraft/models/block/powered_rail/_flat_off.json") as file:
        jf = merge(json.load(file))
        merge(jf, __rail)
        return jf


def powered_rail_raised_on():
    __rail = activator_rail_raised()
    with open("./assets/minecraft/models/block/powered_rail/_raised_on.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def powered_rail_raised_off():
    __rail = activator_rail_raised()
    __rail["textures"]["detail"] = "block/activator_rail"
    with open("./assets/minecraft/models/block/powered_rail/_raised_off.json") as file:
        jf = merge(json.load(file))
        return merge(jf, __rail)


def save(path, dick):
    with open(path, "w") as f:
        f.write(str(dick).replace('\'', "\""))


strdb = {}
for t in tdb:
    for state in tdb[t]:
        for i in range(len(tdb[t][state])):
            path = tdb[t][state][i]
            if exists(path):
                with open(path, "r") as f:
                    if not t in strdb:
                        strdb[t] = {}
                    if not state in strdb[t]:
                        strdb[t][state] = []
                    strdb[t][state].insert(i, json.load(f))

# print(strdb)
# strdb[2]

save("./assets/minecraft/models/block/activator_rail/raised_on.json", activator_rail_raised())
save("./assets/minecraft/models/block/activator_rail/flat_on.json", activator_rail_flat_on())
save("./assets/minecraft/models/block/rail_raised.json", rail_raised())
save("./assets/minecraft/models/block/rail_flat.json", rail_flat())
def rail_curved():
	with open("./assets/minecraft/models/block/_rail_curved.json") as file:
		return json.load(file)
save("./assets/minecraft/models/block/rail_curved.json", rail_curved())
save("./assets/minecraft/models/block/detector_rail/flat_on.json", detector_rail_flat_on())
save("./assets/minecraft/models/block/detector_rail/flat_off.json", detector_rail_flat_off())
save("./assets/minecraft/models/block/detector_rail/raised_on.json", detector_rail_raised_on())
save("./assets/minecraft/models/block/detector_rail/raised_off.json", detector_rail_raised_off())
save("./assets/minecraft/models/block/powered_rail/raised_on.json", powered_rail_raised_on())
save("./assets/minecraft/models/block/powered_rail/raised_off.json", powered_rail_raised_off())
save("./assets/minecraft/models/block/powered_rail/flat_on.json", powered_rail_flat_on())
save("./assets/minecraft/models/block/powered_rail/flat_off.json", powered_rail_flat_off())

def merge(a,b=None):
	_ = o(a)
	if not b:
		return _
	for t in b["textures"]:
		_["textures"][t] = b["textures"][t]
	for e in b["elements"]:
		_["elements"].insert(len(_["elements"]), e)
	return o(_)
def o(jf):
	if "credit" in jf:
		del jf["credit"]
	if "groups" in jf:
		del jf["groups"]
	for i in jf["elements"]:
		if "name" in i:
			del i["name"]
		if "__comment" in i:
			del i["__comment"]
		for _i in i["faces"]:
			if "cullface" in i["faces"][_i]:
				del i["faces"][_i]["cullface"]
	return jf

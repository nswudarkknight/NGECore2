import sys

def setup(core, object):

	object = core.objectService.createObject('object/tangible/wearables/necklace/shared_necklace_rodian_safari_wke_f.iff', object.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setIntAttribute('volume', 1)
	
	return
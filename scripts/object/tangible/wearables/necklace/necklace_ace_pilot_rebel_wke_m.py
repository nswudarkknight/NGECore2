import sys

def setup(core, object):

	object = core.objectService.createObject('object/tangible/wearables/necklace/shared_necklace_ace_pilot_rebel_wke_m.iff', object.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setIntAttribute('volume', 1)
	
	return
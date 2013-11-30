import sys

def setup(core, object):

	object = core.objectService.createObject('object/tangible/wearables/backpack/shared_empireday_sandtrooper_backpack.iff', object.getPlanet())
	object.setStringAttribute('condition', '100/100')
	object.setIntAttribute('volume', 1)
	object.setStringAttribute('cost', '[15] Empire Day Token')
	object.setStringAttribute('faction_restriction', 'Imperial')
	
	return
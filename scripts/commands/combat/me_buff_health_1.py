import sys

def setup(core, actor, target, command):
	if target.getGroupId() != actor.getGroupId():
		core.buffService.addBuffToCreature(actor, 'me_buff_health_0', target)
	else:
		core.buffService.addGroupBuff(actor, 'me_buff_health_0', target)
	return
	
def run(core, actor, target, commandString):
	return
	
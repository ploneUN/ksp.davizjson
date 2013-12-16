from collective.grok import gs
from ksp.davizjson import MessageFactory as _

@gs.importstep(
    name=u'ksp.davizjson', 
    title=_('ksp.davizjson import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('ksp.davizjson.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

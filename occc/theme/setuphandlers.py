from collective.grok import gs
from occc.theme import MessageFactory as _

@gs.importstep(
    name=u'occc.theme', 
    title=_('occc.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('occc.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here

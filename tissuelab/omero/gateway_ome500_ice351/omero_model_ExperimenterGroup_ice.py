# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.1
#
# <auto-generated>
#
# Generated from file `ExperimenterGroup.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'GroupExperimenterMap' not in _M_omero.model.__dict__:
    _M_omero.model._t_GroupExperimenterMap = IcePy.declareClass('::omero::model::GroupExperimenterMap')
    _M_omero.model._t_GroupExperimenterMapPrx = IcePy.declareProxy('::omero::model::GroupExperimenterMap')

if 'Experimenter' not in _M_omero.model.__dict__:
    _M_omero.model._t_Experimenter = IcePy.declareClass('::omero::model::Experimenter')
    _M_omero.model._t_ExperimenterPrx = IcePy.declareProxy('::omero::model::Experimenter')

if 'ExperimenterGroupAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroupAnnotationLink = IcePy.declareClass('::omero::model::ExperimenterGroupAnnotationLink')
    _M_omero.model._t_ExperimenterGroupAnnotationLinkPrx = IcePy.declareProxy('::omero::model::ExperimenterGroupAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if '_t_ExperimenterGroupGroupExperimenterMapSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq = IcePy.defineSequence('::omero::model::ExperimenterGroupGroupExperimenterMapSeq', (), _M_omero.model._t_GroupExperimenterMap)

if '_t_ExperimenterGroupLinkedExperimenterSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroupLinkedExperimenterSeq = IcePy.defineSequence('::omero::model::ExperimenterGroupLinkedExperimenterSeq', (), _M_omero.model._t_Experimenter)

if '_t_ExperimenterGroupAnnotationLinksSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq = IcePy.defineSequence('::omero::model::ExperimenterGroupAnnotationLinksSeq', (), _M_omero.model._t_ExperimenterGroupAnnotationLink)

if '_t_ExperimenterGroupLinkedAnnotationSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroupLinkedAnnotationSeq = IcePy.defineSequence('::omero::model::ExperimenterGroupLinkedAnnotationSeq', (), _M_omero.model._t_Annotation)

if 'ExperimenterGroup' not in _M_omero.model.__dict__:
    _M_omero.model.ExperimenterGroup = Ice.createTempClass()
    class ExperimenterGroup(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _name=None, _groupExperimenterMapSeq=None, _groupExperimenterMapLoaded=False, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _description=None):
            if Ice.getType(self) == _M_omero.model.ExperimenterGroup:
                raise RuntimeError('omero.model.ExperimenterGroup is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._name = _name
            self._groupExperimenterMapSeq = _groupExperimenterMapSeq
            self._groupExperimenterMapLoaded = _groupExperimenterMapLoaded
            self._annotationLinksSeq = _annotationLinksSeq
            self._annotationLinksLoaded = _annotationLinksLoaded
            self._annotationLinksCountPerOwner = _annotationLinksCountPerOwner
            self._description = _description

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::ExperimenterGroup', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::ExperimenterGroup'

        def ice_staticId():
            return '::omero::model::ExperimenterGroup'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getName(self, current=None):
            pass

        def setName(self, theName, current=None):
            pass

        def unloadGroupExperimenterMap(self, current=None):
            pass

        def sizeOfGroupExperimenterMap(self, current=None):
            pass

        def copyGroupExperimenterMap(self, current=None):
            pass

        def addGroupExperimenterMap(self, target, current=None):
            pass

        def addAllGroupExperimenterMapSet(self, targets, current=None):
            pass

        def removeGroupExperimenterMap(self, theTarget, current=None):
            pass

        def removeAllGroupExperimenterMapSet(self, targets, current=None):
            pass

        def clearGroupExperimenterMap(self, current=None):
            pass

        def reloadGroupExperimenterMap(self, toCopy, current=None):
            pass

        def linkExperimenter(self, addition, current=None):
            pass

        def addGroupExperimenterMapToBoth(self, link, bothSides, current=None):
            pass

        def findGroupExperimenterMap(self, removal, current=None):
            pass

        def unlinkExperimenter(self, removal, current=None):
            pass

        def removeGroupExperimenterMapFromBoth(self, link, bothSides, current=None):
            pass

        def linkedExperimenterList(self, current=None):
            pass

        def unloadAnnotationLinks(self, current=None):
            pass

        def sizeOfAnnotationLinks(self, current=None):
            pass

        def copyAnnotationLinks(self, current=None):
            pass

        def addExperimenterGroupAnnotationLink(self, target, current=None):
            pass

        def addAllExperimenterGroupAnnotationLinkSet(self, targets, current=None):
            pass

        def removeExperimenterGroupAnnotationLink(self, theTarget, current=None):
            pass

        def removeAllExperimenterGroupAnnotationLinkSet(self, targets, current=None):
            pass

        def clearAnnotationLinks(self, current=None):
            pass

        def reloadAnnotationLinks(self, toCopy, current=None):
            pass

        def getAnnotationLinksCountPerOwner(self, current=None):
            pass

        def linkAnnotation(self, addition, current=None):
            pass

        def addExperimenterGroupAnnotationLinkToBoth(self, link, bothSides, current=None):
            pass

        def findExperimenterGroupAnnotationLink(self, removal, current=None):
            pass

        def unlinkAnnotation(self, removal, current=None):
            pass

        def removeExperimenterGroupAnnotationLinkFromBoth(self, link, bothSides, current=None):
            pass

        def linkedAnnotationList(self, current=None):
            pass

        def getDescription(self, current=None):
            pass

        def setDescription(self, theDescription, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_ExperimenterGroup)

        __repr__ = __str__

    _M_omero.model.ExperimenterGroupPrx = Ice.createTempClass()
    class ExperimenterGroupPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.ExperimenterGroup._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.ExperimenterGroup._op_setVersion.end(self, _r)

        def getName(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getName.invoke(self, ((), _ctx))

        def begin_getName(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getName.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getName(self, _r):
            return _M_omero.model.ExperimenterGroup._op_getName.end(self, _r)

        def setName(self, theName, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setName.invoke(self, ((theName, ), _ctx))

        def begin_setName(self, theName, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setName.begin(self, ((theName, ), _response, _ex, _sent, _ctx))

        def end_setName(self, _r):
            return _M_omero.model.ExperimenterGroup._op_setName.end(self, _r)

        def unloadGroupExperimenterMap(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unloadGroupExperimenterMap.invoke(self, ((), _ctx))

        def begin_unloadGroupExperimenterMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unloadGroupExperimenterMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_unloadGroupExperimenterMap.end(self, _r)

        def sizeOfGroupExperimenterMap(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_sizeOfGroupExperimenterMap.invoke(self, ((), _ctx))

        def begin_sizeOfGroupExperimenterMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_sizeOfGroupExperimenterMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_sizeOfGroupExperimenterMap.end(self, _r)

        def copyGroupExperimenterMap(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_copyGroupExperimenterMap.invoke(self, ((), _ctx))

        def begin_copyGroupExperimenterMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_copyGroupExperimenterMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_copyGroupExperimenterMap.end(self, _r)

        def addGroupExperimenterMap(self, target, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMap.invoke(self, ((target, ), _ctx))

        def begin_addGroupExperimenterMap(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMap.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMap.end(self, _r)

        def addAllGroupExperimenterMapSet(self, targets, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addAllGroupExperimenterMapSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllGroupExperimenterMapSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addAllGroupExperimenterMapSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllGroupExperimenterMapSet(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addAllGroupExperimenterMapSet.end(self, _r)

        def removeGroupExperimenterMap(self, theTarget, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMap.invoke(self, ((theTarget, ), _ctx))

        def begin_removeGroupExperimenterMap(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMap.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMap.end(self, _r)

        def removeAllGroupExperimenterMapSet(self, targets, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeAllGroupExperimenterMapSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllGroupExperimenterMapSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeAllGroupExperimenterMapSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllGroupExperimenterMapSet(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeAllGroupExperimenterMapSet.end(self, _r)

        def clearGroupExperimenterMap(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_clearGroupExperimenterMap.invoke(self, ((), _ctx))

        def begin_clearGroupExperimenterMap(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_clearGroupExperimenterMap.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_clearGroupExperimenterMap.end(self, _r)

        def reloadGroupExperimenterMap(self, toCopy, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_reloadGroupExperimenterMap.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadGroupExperimenterMap(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_reloadGroupExperimenterMap.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_reloadGroupExperimenterMap.end(self, _r)

        def linkExperimenter(self, addition, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkExperimenter.invoke(self, ((addition, ), _ctx))

        def begin_linkExperimenter(self, addition, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkExperimenter.begin(self, ((addition, ), _response, _ex, _sent, _ctx))

        def end_linkExperimenter(self, _r):
            return _M_omero.model.ExperimenterGroup._op_linkExperimenter.end(self, _r)

        def addGroupExperimenterMapToBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMapToBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_addGroupExperimenterMapToBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMapToBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_addGroupExperimenterMapToBoth(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addGroupExperimenterMapToBoth.end(self, _r)

        def findGroupExperimenterMap(self, removal, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_findGroupExperimenterMap.invoke(self, ((removal, ), _ctx))

        def begin_findGroupExperimenterMap(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_findGroupExperimenterMap.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_findGroupExperimenterMap(self, _r):
            return _M_omero.model.ExperimenterGroup._op_findGroupExperimenterMap.end(self, _r)

        def unlinkExperimenter(self, removal, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unlinkExperimenter.invoke(self, ((removal, ), _ctx))

        def begin_unlinkExperimenter(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unlinkExperimenter.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_unlinkExperimenter(self, _r):
            return _M_omero.model.ExperimenterGroup._op_unlinkExperimenter.end(self, _r)

        def removeGroupExperimenterMapFromBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMapFromBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_removeGroupExperimenterMapFromBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMapFromBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_removeGroupExperimenterMapFromBoth(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeGroupExperimenterMapFromBoth.end(self, _r)

        def linkedExperimenterList(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkedExperimenterList.invoke(self, ((), _ctx))

        def begin_linkedExperimenterList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkedExperimenterList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_linkedExperimenterList(self, _r):
            return _M_omero.model.ExperimenterGroup._op_linkedExperimenterList.end(self, _r)

        def unloadAnnotationLinks(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unloadAnnotationLinks.invoke(self, ((), _ctx))

        def begin_unloadAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unloadAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadAnnotationLinks(self, _r):
            return _M_omero.model.ExperimenterGroup._op_unloadAnnotationLinks.end(self, _r)

        def sizeOfAnnotationLinks(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_sizeOfAnnotationLinks.invoke(self, ((), _ctx))

        def begin_sizeOfAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_sizeOfAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfAnnotationLinks(self, _r):
            return _M_omero.model.ExperimenterGroup._op_sizeOfAnnotationLinks.end(self, _r)

        def copyAnnotationLinks(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_copyAnnotationLinks.invoke(self, ((), _ctx))

        def begin_copyAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_copyAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyAnnotationLinks(self, _r):
            return _M_omero.model.ExperimenterGroup._op_copyAnnotationLinks.end(self, _r)

        def addExperimenterGroupAnnotationLink(self, target, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLink.invoke(self, ((target, ), _ctx))

        def begin_addExperimenterGroupAnnotationLink(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLink.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addExperimenterGroupAnnotationLink(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLink.end(self, _r)

        def addAllExperimenterGroupAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addAllExperimenterGroupAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllExperimenterGroupAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addAllExperimenterGroupAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllExperimenterGroupAnnotationLinkSet(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addAllExperimenterGroupAnnotationLinkSet.end(self, _r)

        def removeExperimenterGroupAnnotationLink(self, theTarget, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLink.invoke(self, ((theTarget, ), _ctx))

        def begin_removeExperimenterGroupAnnotationLink(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLink.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeExperimenterGroupAnnotationLink(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLink.end(self, _r)

        def removeAllExperimenterGroupAnnotationLinkSet(self, targets, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeAllExperimenterGroupAnnotationLinkSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllExperimenterGroupAnnotationLinkSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeAllExperimenterGroupAnnotationLinkSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllExperimenterGroupAnnotationLinkSet(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeAllExperimenterGroupAnnotationLinkSet.end(self, _r)

        def clearAnnotationLinks(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_clearAnnotationLinks.invoke(self, ((), _ctx))

        def begin_clearAnnotationLinks(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_clearAnnotationLinks.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearAnnotationLinks(self, _r):
            return _M_omero.model.ExperimenterGroup._op_clearAnnotationLinks.end(self, _r)

        def reloadAnnotationLinks(self, toCopy, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_reloadAnnotationLinks.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadAnnotationLinks(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_reloadAnnotationLinks.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadAnnotationLinks(self, _r):
            return _M_omero.model.ExperimenterGroup._op_reloadAnnotationLinks.end(self, _r)

        def getAnnotationLinksCountPerOwner(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getAnnotationLinksCountPerOwner.invoke(self, ((), _ctx))

        def begin_getAnnotationLinksCountPerOwner(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getAnnotationLinksCountPerOwner.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAnnotationLinksCountPerOwner(self, _r):
            return _M_omero.model.ExperimenterGroup._op_getAnnotationLinksCountPerOwner.end(self, _r)

        def linkAnnotation(self, addition, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkAnnotation.invoke(self, ((addition, ), _ctx))

        def begin_linkAnnotation(self, addition, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkAnnotation.begin(self, ((addition, ), _response, _ex, _sent, _ctx))

        def end_linkAnnotation(self, _r):
            return _M_omero.model.ExperimenterGroup._op_linkAnnotation.end(self, _r)

        def addExperimenterGroupAnnotationLinkToBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLinkToBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_addExperimenterGroupAnnotationLinkToBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLinkToBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_addExperimenterGroupAnnotationLinkToBoth(self, _r):
            return _M_omero.model.ExperimenterGroup._op_addExperimenterGroupAnnotationLinkToBoth.end(self, _r)

        def findExperimenterGroupAnnotationLink(self, removal, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_findExperimenterGroupAnnotationLink.invoke(self, ((removal, ), _ctx))

        def begin_findExperimenterGroupAnnotationLink(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_findExperimenterGroupAnnotationLink.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_findExperimenterGroupAnnotationLink(self, _r):
            return _M_omero.model.ExperimenterGroup._op_findExperimenterGroupAnnotationLink.end(self, _r)

        def unlinkAnnotation(self, removal, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unlinkAnnotation.invoke(self, ((removal, ), _ctx))

        def begin_unlinkAnnotation(self, removal, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_unlinkAnnotation.begin(self, ((removal, ), _response, _ex, _sent, _ctx))

        def end_unlinkAnnotation(self, _r):
            return _M_omero.model.ExperimenterGroup._op_unlinkAnnotation.end(self, _r)

        def removeExperimenterGroupAnnotationLinkFromBoth(self, link, bothSides, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLinkFromBoth.invoke(self, ((link, bothSides), _ctx))

        def begin_removeExperimenterGroupAnnotationLinkFromBoth(self, link, bothSides, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLinkFromBoth.begin(self, ((link, bothSides), _response, _ex, _sent, _ctx))

        def end_removeExperimenterGroupAnnotationLinkFromBoth(self, _r):
            return _M_omero.model.ExperimenterGroup._op_removeExperimenterGroupAnnotationLinkFromBoth.end(self, _r)

        def linkedAnnotationList(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkedAnnotationList.invoke(self, ((), _ctx))

        def begin_linkedAnnotationList(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_linkedAnnotationList.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_linkedAnnotationList(self, _r):
            return _M_omero.model.ExperimenterGroup._op_linkedAnnotationList.end(self, _r)

        def getDescription(self, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getDescription.invoke(self, ((), _ctx))

        def begin_getDescription(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_getDescription.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getDescription(self, _r):
            return _M_omero.model.ExperimenterGroup._op_getDescription.end(self, _r)

        def setDescription(self, theDescription, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setDescription.invoke(self, ((theDescription, ), _ctx))

        def begin_setDescription(self, theDescription, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ExperimenterGroup._op_setDescription.begin(self, ((theDescription, ), _response, _ex, _sent, _ctx))

        def end_setDescription(self, _r):
            return _M_omero.model.ExperimenterGroup._op_setDescription.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ExperimenterGroupPrx.ice_checkedCast(proxy, '::omero::model::ExperimenterGroup', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ExperimenterGroupPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_ExperimenterGroupPrx = IcePy.defineProxy('::omero::model::ExperimenterGroup', ExperimenterGroupPrx)

    _M_omero.model._t_ExperimenterGroup = IcePy.declareClass('::omero::model::ExperimenterGroup')

    _M_omero.model._t_ExperimenterGroup = IcePy.defineClass('::omero::model::ExperimenterGroup', ExperimenterGroup, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_name', (), _M_omero._t_RString, False, 0),
        ('_groupExperimenterMapSeq', (), _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq, False, 0),
        ('_groupExperimenterMapLoaded', (), IcePy._t_bool, False, 0),
        ('_annotationLinksSeq', (), _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq, False, 0),
        ('_annotationLinksLoaded', (), IcePy._t_bool, False, 0),
        ('_annotationLinksCountPerOwner', (), _M_omero.sys._t_CountMap, False, 0),
        ('_description', (), _M_omero._t_RString, False, 0)
    ))
    ExperimenterGroup._ice_type = _M_omero.model._t_ExperimenterGroup

    ExperimenterGroup._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    ExperimenterGroup._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    ExperimenterGroup._op_getName = IcePy.Operation('getName', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    ExperimenterGroup._op_setName = IcePy.Operation('setName', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    ExperimenterGroup._op_unloadGroupExperimenterMap = IcePy.Operation('unloadGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    ExperimenterGroup._op_sizeOfGroupExperimenterMap = IcePy.Operation('sizeOfGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    ExperimenterGroup._op_copyGroupExperimenterMap = IcePy.Operation('copyGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq, False, 0), ())
    ExperimenterGroup._op_addGroupExperimenterMap = IcePy.Operation('addGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_GroupExperimenterMap, False, 0),), (), None, ())
    ExperimenterGroup._op_addAllGroupExperimenterMapSet = IcePy.Operation('addAllGroupExperimenterMapSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq, False, 0),), (), None, ())
    ExperimenterGroup._op_removeGroupExperimenterMap = IcePy.Operation('removeGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_GroupExperimenterMap, False, 0),), (), None, ())
    ExperimenterGroup._op_removeAllGroupExperimenterMapSet = IcePy.Operation('removeAllGroupExperimenterMapSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq, False, 0),), (), None, ())
    ExperimenterGroup._op_clearGroupExperimenterMap = IcePy.Operation('clearGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    ExperimenterGroup._op_reloadGroupExperimenterMap = IcePy.Operation('reloadGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroup, False, 0),), (), None, ())
    ExperimenterGroup._op_linkExperimenter = IcePy.Operation('linkExperimenter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experimenter, False, 0),), (), ((), _M_omero.model._t_GroupExperimenterMap, False, 0), ())
    ExperimenterGroup._op_addGroupExperimenterMapToBoth = IcePy.Operation('addGroupExperimenterMapToBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_GroupExperimenterMap, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    ExperimenterGroup._op_findGroupExperimenterMap = IcePy.Operation('findGroupExperimenterMap', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experimenter, False, 0),), (), ((), _M_omero.model._t_ExperimenterGroupGroupExperimenterMapSeq, False, 0), ())
    ExperimenterGroup._op_unlinkExperimenter = IcePy.Operation('unlinkExperimenter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experimenter, False, 0),), (), None, ())
    ExperimenterGroup._op_removeGroupExperimenterMapFromBoth = IcePy.Operation('removeGroupExperimenterMapFromBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_GroupExperimenterMap, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    ExperimenterGroup._op_linkedExperimenterList = IcePy.Operation('linkedExperimenterList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimenterGroupLinkedExperimenterSeq, False, 0), ())
    ExperimenterGroup._op_unloadAnnotationLinks = IcePy.Operation('unloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    ExperimenterGroup._op_sizeOfAnnotationLinks = IcePy.Operation('sizeOfAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    ExperimenterGroup._op_copyAnnotationLinks = IcePy.Operation('copyAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq, False, 0), ())
    ExperimenterGroup._op_addExperimenterGroupAnnotationLink = IcePy.Operation('addExperimenterGroupAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLink, False, 0),), (), None, ())
    ExperimenterGroup._op_addAllExperimenterGroupAnnotationLinkSet = IcePy.Operation('addAllExperimenterGroupAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq, False, 0),), (), None, ())
    ExperimenterGroup._op_removeExperimenterGroupAnnotationLink = IcePy.Operation('removeExperimenterGroupAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLink, False, 0),), (), None, ())
    ExperimenterGroup._op_removeAllExperimenterGroupAnnotationLinkSet = IcePy.Operation('removeAllExperimenterGroupAnnotationLinkSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq, False, 0),), (), None, ())
    ExperimenterGroup._op_clearAnnotationLinks = IcePy.Operation('clearAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    ExperimenterGroup._op_reloadAnnotationLinks = IcePy.Operation('reloadAnnotationLinks', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroup, False, 0),), (), None, ())
    ExperimenterGroup._op_getAnnotationLinksCountPerOwner = IcePy.Operation('getAnnotationLinksCountPerOwner', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.sys._t_CountMap, False, 0), ())
    ExperimenterGroup._op_linkAnnotation = IcePy.Operation('linkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), ((), _M_omero.model._t_ExperimenterGroupAnnotationLink, False, 0), ())
    ExperimenterGroup._op_addExperimenterGroupAnnotationLinkToBoth = IcePy.Operation('addExperimenterGroupAnnotationLinkToBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLink, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    ExperimenterGroup._op_findExperimenterGroupAnnotationLink = IcePy.Operation('findExperimenterGroupAnnotationLink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), ((), _M_omero.model._t_ExperimenterGroupAnnotationLinksSeq, False, 0), ())
    ExperimenterGroup._op_unlinkAnnotation = IcePy.Operation('unlinkAnnotation', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Annotation, False, 0),), (), None, ())
    ExperimenterGroup._op_removeExperimenterGroupAnnotationLinkFromBoth = IcePy.Operation('removeExperimenterGroupAnnotationLinkFromBoth', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroupAnnotationLink, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    ExperimenterGroup._op_linkedAnnotationList = IcePy.Operation('linkedAnnotationList', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimenterGroupLinkedAnnotationSeq, False, 0), ())
    ExperimenterGroup._op_getDescription = IcePy.Operation('getDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    ExperimenterGroup._op_setDescription = IcePy.Operation('setDescription', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.ExperimenterGroup = ExperimenterGroup
    del ExperimenterGroup

    _M_omero.model.ExperimenterGroupPrx = ExperimenterGroupPrx
    del ExperimenterGroupPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero

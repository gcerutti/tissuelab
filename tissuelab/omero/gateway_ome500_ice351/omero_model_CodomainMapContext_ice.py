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
# Generated from file `CodomainMapContext.ice'
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

if 'RenderingDef' not in _M_omero.model.__dict__:
    _M_omero.model._t_RenderingDef = IcePy.declareClass('::omero::model::RenderingDef')
    _M_omero.model._t_RenderingDefPrx = IcePy.declareProxy('::omero::model::RenderingDef')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'CodomainMapContext' not in _M_omero.model.__dict__:
    _M_omero.model.CodomainMapContext = Ice.createTempClass()
    class CodomainMapContext(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _renderingDef=None):
            if Ice.getType(self) == _M_omero.model.CodomainMapContext:
                raise RuntimeError('omero.model.CodomainMapContext is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._version = _version
            self._renderingDef = _renderingDef

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::CodomainMapContext', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::CodomainMapContext'

        def ice_staticId():
            return '::omero::model::CodomainMapContext'
        ice_staticId = staticmethod(ice_staticId)

        def getVersion(self, current=None):
            pass

        def setVersion(self, theVersion, current=None):
            pass

        def getRenderingDef(self, current=None):
            pass

        def setRenderingDef(self, theRenderingDef, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_CodomainMapContext)

        __repr__ = __str__

    _M_omero.model.CodomainMapContextPrx = Ice.createTempClass()
    class CodomainMapContextPrx(_M_omero.model.IObjectPrx):

        def getVersion(self, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_getVersion.invoke(self, ((), _ctx))

        def begin_getVersion(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_getVersion.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getVersion(self, _r):
            return _M_omero.model.CodomainMapContext._op_getVersion.end(self, _r)

        def setVersion(self, theVersion, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_setVersion.invoke(self, ((theVersion, ), _ctx))

        def begin_setVersion(self, theVersion, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_setVersion.begin(self, ((theVersion, ), _response, _ex, _sent, _ctx))

        def end_setVersion(self, _r):
            return _M_omero.model.CodomainMapContext._op_setVersion.end(self, _r)

        def getRenderingDef(self, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_getRenderingDef.invoke(self, ((), _ctx))

        def begin_getRenderingDef(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_getRenderingDef.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getRenderingDef(self, _r):
            return _M_omero.model.CodomainMapContext._op_getRenderingDef.end(self, _r)

        def setRenderingDef(self, theRenderingDef, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_setRenderingDef.invoke(self, ((theRenderingDef, ), _ctx))

        def begin_setRenderingDef(self, theRenderingDef, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.CodomainMapContext._op_setRenderingDef.begin(self, ((theRenderingDef, ), _response, _ex, _sent, _ctx))

        def end_setRenderingDef(self, _r):
            return _M_omero.model.CodomainMapContext._op_setRenderingDef.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.CodomainMapContextPrx.ice_checkedCast(proxy, '::omero::model::CodomainMapContext', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.CodomainMapContextPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.model._t_CodomainMapContextPrx = IcePy.defineProxy('::omero::model::CodomainMapContext', CodomainMapContextPrx)

    _M_omero.model._t_CodomainMapContext = IcePy.declareClass('::omero::model::CodomainMapContext')

    _M_omero.model._t_CodomainMapContext = IcePy.defineClass('::omero::model::CodomainMapContext', CodomainMapContext, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_version', (), _M_omero._t_RInt, False, 0),
        ('_renderingDef', (), _M_omero.model._t_RenderingDef, False, 0)
    ))
    CodomainMapContext._ice_type = _M_omero.model._t_CodomainMapContext

    CodomainMapContext._op_getVersion = IcePy.Operation('getVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RInt, False, 0), ())
    CodomainMapContext._op_setVersion = IcePy.Operation('setVersion', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RInt, False, 0),), (), None, ())
    CodomainMapContext._op_getRenderingDef = IcePy.Operation('getRenderingDef', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_RenderingDef, False, 0), ())
    CodomainMapContext._op_setRenderingDef = IcePy.Operation('setRenderingDef', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_RenderingDef, False, 0),), (), None, ())

    _M_omero.model.CodomainMapContext = CodomainMapContext
    del CodomainMapContext

    _M_omero.model.CodomainMapContextPrx = CodomainMapContextPrx
    del CodomainMapContextPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero

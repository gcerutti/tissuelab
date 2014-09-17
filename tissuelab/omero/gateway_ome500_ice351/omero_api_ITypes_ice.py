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
# Generated from file `ITypes.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import omero_ModelF_ice
import omero_ServicesF_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Start of module omero
__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if 'ITypes' not in _M_omero.api.__dict__:
    _M_omero.api.ITypes = Ice.createTempClass()
    class ITypes(_M_omero.api.ServiceInterface):
        '''See ITypes.html'''
        def __init__(self):
            if Ice.getType(self) == _M_omero.api.ITypes:
                raise RuntimeError('omero.api.ITypes is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::ITypes', '::omero::api::ServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::ITypes'

        def ice_staticId():
            return '::omero::api::ITypes'
        ice_staticId = staticmethod(ice_staticId)

        def createEnumeration_async(self, _cb, newEnum, current=None):
            pass

        def getEnumeration_async(self, _cb, type, value, current=None):
            pass

        def allEnumerations_async(self, _cb, type, current=None):
            pass

        def updateEnumeration_async(self, _cb, oldEnum, current=None):
            pass

        def updateEnumerations_async(self, _cb, oldEnums, current=None):
            pass

        def deleteEnumeration_async(self, _cb, oldEnum, current=None):
            pass

        def getEnumerationTypes_async(self, _cb, current=None):
            pass

        def getAnnotationTypes_async(self, _cb, current=None):
            pass

        def getEnumerationsWithEntries_async(self, _cb, current=None):
            pass

        def getOriginalEnumerations_async(self, _cb, current=None):
            pass

        def resetEnumerations_async(self, _cb, enumClass, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_ITypes)

        __repr__ = __str__

    _M_omero.api.ITypesPrx = Ice.createTempClass()
    class ITypesPrx(_M_omero.api.ServiceInterfacePrx):

        def createEnumeration(self, newEnum, _ctx=None):
            return _M_omero.api.ITypes._op_createEnumeration.invoke(self, ((newEnum, ), _ctx))

        def begin_createEnumeration(self, newEnum, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_createEnumeration.begin(self, ((newEnum, ), _response, _ex, _sent, _ctx))

        def end_createEnumeration(self, _r):
            return _M_omero.api.ITypes._op_createEnumeration.end(self, _r)

        def createEnumeration_async(self, _cb, newEnum, _ctx=None):
            return _M_omero.api.ITypes._op_createEnumeration.invokeAsync(self, (_cb, (newEnum, ), _ctx))

        def getEnumeration(self, type, value, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumeration.invoke(self, ((type, value), _ctx))

        def begin_getEnumeration(self, type, value, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumeration.begin(self, ((type, value), _response, _ex, _sent, _ctx))

        def end_getEnumeration(self, _r):
            return _M_omero.api.ITypes._op_getEnumeration.end(self, _r)

        def getEnumeration_async(self, _cb, type, value, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumeration.invokeAsync(self, (_cb, (type, value), _ctx))

        def allEnumerations(self, type, _ctx=None):
            return _M_omero.api.ITypes._op_allEnumerations.invoke(self, ((type, ), _ctx))

        def begin_allEnumerations(self, type, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_allEnumerations.begin(self, ((type, ), _response, _ex, _sent, _ctx))

        def end_allEnumerations(self, _r):
            return _M_omero.api.ITypes._op_allEnumerations.end(self, _r)

        def allEnumerations_async(self, _cb, type, _ctx=None):
            return _M_omero.api.ITypes._op_allEnumerations.invokeAsync(self, (_cb, (type, ), _ctx))

        def updateEnumeration(self, oldEnum, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumeration.invoke(self, ((oldEnum, ), _ctx))

        def begin_updateEnumeration(self, oldEnum, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumeration.begin(self, ((oldEnum, ), _response, _ex, _sent, _ctx))

        def end_updateEnumeration(self, _r):
            return _M_omero.api.ITypes._op_updateEnumeration.end(self, _r)

        def updateEnumeration_async(self, _cb, oldEnum, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumeration.invokeAsync(self, (_cb, (oldEnum, ), _ctx))

        def updateEnumerations(self, oldEnums, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumerations.invoke(self, ((oldEnums, ), _ctx))

        def begin_updateEnumerations(self, oldEnums, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumerations.begin(self, ((oldEnums, ), _response, _ex, _sent, _ctx))

        def end_updateEnumerations(self, _r):
            return _M_omero.api.ITypes._op_updateEnumerations.end(self, _r)

        def updateEnumerations_async(self, _cb, oldEnums, _ctx=None):
            return _M_omero.api.ITypes._op_updateEnumerations.invokeAsync(self, (_cb, (oldEnums, ), _ctx))

        def deleteEnumeration(self, oldEnum, _ctx=None):
            return _M_omero.api.ITypes._op_deleteEnumeration.invoke(self, ((oldEnum, ), _ctx))

        def begin_deleteEnumeration(self, oldEnum, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_deleteEnumeration.begin(self, ((oldEnum, ), _response, _ex, _sent, _ctx))

        def end_deleteEnumeration(self, _r):
            return _M_omero.api.ITypes._op_deleteEnumeration.end(self, _r)

        def deleteEnumeration_async(self, _cb, oldEnum, _ctx=None):
            return _M_omero.api.ITypes._op_deleteEnumeration.invokeAsync(self, (_cb, (oldEnum, ), _ctx))

        def getEnumerationTypes(self, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationTypes.invoke(self, ((), _ctx))

        def begin_getEnumerationTypes(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationTypes.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEnumerationTypes(self, _r):
            return _M_omero.api.ITypes._op_getEnumerationTypes.end(self, _r)

        def getEnumerationTypes_async(self, _cb, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationTypes.invokeAsync(self, (_cb, (), _ctx))

        def getAnnotationTypes(self, _ctx=None):
            return _M_omero.api.ITypes._op_getAnnotationTypes.invoke(self, ((), _ctx))

        def begin_getAnnotationTypes(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_getAnnotationTypes.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getAnnotationTypes(self, _r):
            return _M_omero.api.ITypes._op_getAnnotationTypes.end(self, _r)

        def getAnnotationTypes_async(self, _cb, _ctx=None):
            return _M_omero.api.ITypes._op_getAnnotationTypes.invokeAsync(self, (_cb, (), _ctx))

        def getEnumerationsWithEntries(self, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationsWithEntries.invoke(self, ((), _ctx))

        def begin_getEnumerationsWithEntries(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationsWithEntries.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getEnumerationsWithEntries(self, _r):
            return _M_omero.api.ITypes._op_getEnumerationsWithEntries.end(self, _r)

        def getEnumerationsWithEntries_async(self, _cb, _ctx=None):
            return _M_omero.api.ITypes._op_getEnumerationsWithEntries.invokeAsync(self, (_cb, (), _ctx))

        def getOriginalEnumerations(self, _ctx=None):
            return _M_omero.api.ITypes._op_getOriginalEnumerations.invoke(self, ((), _ctx))

        def begin_getOriginalEnumerations(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_getOriginalEnumerations.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getOriginalEnumerations(self, _r):
            return _M_omero.api.ITypes._op_getOriginalEnumerations.end(self, _r)

        def getOriginalEnumerations_async(self, _cb, _ctx=None):
            return _M_omero.api.ITypes._op_getOriginalEnumerations.invokeAsync(self, (_cb, (), _ctx))

        def resetEnumerations(self, enumClass, _ctx=None):
            return _M_omero.api.ITypes._op_resetEnumerations.invoke(self, ((enumClass, ), _ctx))

        def begin_resetEnumerations(self, enumClass, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.ITypes._op_resetEnumerations.begin(self, ((enumClass, ), _response, _ex, _sent, _ctx))

        def end_resetEnumerations(self, _r):
            return _M_omero.api.ITypes._op_resetEnumerations.end(self, _r)

        def resetEnumerations_async(self, _cb, enumClass, _ctx=None):
            return _M_omero.api.ITypes._op_resetEnumerations.invokeAsync(self, (_cb, (enumClass, ), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.ITypesPrx.ice_checkedCast(proxy, '::omero::api::ITypes', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.ITypesPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_omero.api._t_ITypesPrx = IcePy.defineProxy('::omero::api::ITypes', ITypesPrx)

    _M_omero.api._t_ITypes = IcePy.defineClass('::omero::api::ITypes', ITypes, -1, (), True, False, None, (_M_omero.api._t_ServiceInterface,), ())
    ITypes._ice_type = _M_omero.api._t_ITypes

    ITypes._op_createEnumeration = IcePy.Operation('createEnumeration', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_IObject, False, 0),), (), ((), _M_omero.model._t_IObject, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_getEnumeration = IcePy.Operation('getEnumeration', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_omero.model._t_IObject, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_allEnumerations = IcePy.Operation('allEnumerations', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_omero.api._t_IObjectList, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_updateEnumeration = IcePy.Operation('updateEnumeration', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_IObject, False, 0),), (), ((), _M_omero.model._t_IObject, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_updateEnumerations = IcePy.Operation('updateEnumerations', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.api._t_IObjectList, False, 0),), (), None, (_M_omero._t_ServerError,))
    ITypes._op_deleteEnumeration = IcePy.Operation('deleteEnumeration', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_IObject, False, 0),), (), None, (_M_omero._t_ServerError,))
    ITypes._op_getEnumerationTypes = IcePy.Operation('getEnumerationTypes', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (), (), ((), _M_omero.api._t_StringSet, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_getAnnotationTypes = IcePy.Operation('getAnnotationTypes', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (), (), ((), _M_omero.api._t_StringSet, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_getEnumerationsWithEntries = IcePy.Operation('getEnumerationsWithEntries', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (), (), ((), _M_omero.api._t_IObjectListMap, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_getOriginalEnumerations = IcePy.Operation('getOriginalEnumerations', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (), (), ((), _M_omero.api._t_IObjectList, False, 0), (_M_omero._t_ServerError,))
    ITypes._op_resetEnumerations = IcePy.Operation('resetEnumerations', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), IcePy._t_string, False, 0),), (), None, (_M_omero._t_ServerError,))

    _M_omero.api.ITypes = ITypes
    del ITypes

    _M_omero.api.ITypesPrx = ITypesPrx
    del ITypesPrx

# End of module omero.api

__name__ = 'omero'

# End of module omero

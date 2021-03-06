"""
   /*
   **   Generated by blitz/templates/resouces/combined.vm
   **
   **   Copyright 2007, 2008 Glencoe Software, Inc. All rights reserved.
   **   Use is subject to license terms supplied in LICENSE.txt
   **
   */
"""
import Ice
import IceImport
import omero
IceImport.load("omero_model_DetailsI")
IceImport.load("omero_model_ObjectiveSettings_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class ObjectiveSettingsI(_omero_model.ObjectiveSettings):

      CORRECTIONCOLLAR =  "ome.model.acquisition.ObjectiveSettings_correctionCollar"
      MEDIUM =  "ome.model.acquisition.ObjectiveSettings_medium"
      REFRACTIVEINDEX =  "ome.model.acquisition.ObjectiveSettings_refractiveIndex"
      OBJECTIVE =  "ome.model.acquisition.ObjectiveSettings_objective"
      DETAILS =  "ome.model.acquisition.ObjectiveSettings_details"
      def errorIfUnloaded(self):
          if not self._loaded:
              raise _omero.UnloadedEntityException("Object unloaded:"+str(self))

      def throwNullCollectionException(self,propertyName):
          raise _omero.UnloadedEntityException(""+
          "Error updating collection:" + propertyName +"\n"+
          "Collection is currently null. This can be seen\n" +
          "by testing \""+ propertyName +"Loaded\". This implies\n"+
          "that this collection was unloaded. Please refresh this object\n"+
          "in order to update this collection.\n")

      def _toggleCollectionsLoaded(self,load):
          pass

      def __init__(self, id = None, loaded = True):
          super(ObjectiveSettingsI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadCorrectionCollar( )
          self.unloadMedium( )
          self.unloadRefractiveIndex( )
          self.unloadObjective( )
          self.unloadDetails( )

      def isLoaded(self, current = None):
          return self._loaded
      def unloadCollections(self, current = None):
          self._toggleCollectionsLoaded( False )
      def isGlobal(self, current = None):
          return  False ;
      def isMutable(self, current = None):
          return  True ;
      def isAnnotated(self, current = None):
          return  False ;
      def isLink(self, current = None):
          return  False ;
      def shallowCopy(self, current = None):
            if not self._loaded: return self.proxy()
            copy = ObjectiveSettingsI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return ObjectiveSettingsI( self._id.getValue(), False )

      def getDetails(self, current = None):
          self.errorIfUnloaded()
          return self._details

      def unloadDetails(self, current = None):
          self._details = None

      def getId(self, current = None):
          return self._id

      def setId(self, _id, current = None):
          self._id = _id

      def checkUnloadedProperty(self, value, loadedField):
          if value == None:
              self.__dict__[loadedField] = False
          else:
              self.__dict__[loadedField] = True

      def getVersion(self, current = None):
          self.errorIfUnloaded()
          return self._version

      def setVersion(self, version, current = None):
          self.errorIfUnloaded()
          self._version = version

      def unloadCorrectionCollar(self, ):
          self._correctionCollarLoaded = False
          self._correctionCollar = None;

      def getCorrectionCollar(self, current = None):
          self.errorIfUnloaded()
          return self._correctionCollar

      def setCorrectionCollar(self, _correctionCollar, current = None):
          self.errorIfUnloaded()
          self._correctionCollar = _correctionCollar
          pass

      def unloadMedium(self, ):
          self._mediumLoaded = False
          self._medium = None;

      def getMedium(self, current = None):
          self.errorIfUnloaded()
          return self._medium

      def setMedium(self, _medium, current = None):
          self.errorIfUnloaded()
          self._medium = _medium
          pass

      def unloadRefractiveIndex(self, ):
          self._refractiveIndexLoaded = False
          self._refractiveIndex = None;

      def getRefractiveIndex(self, current = None):
          self.errorIfUnloaded()
          return self._refractiveIndex

      def setRefractiveIndex(self, _refractiveIndex, current = None):
          self.errorIfUnloaded()
          self._refractiveIndex = _refractiveIndex
          pass

      def unloadObjective(self, ):
          self._objectiveLoaded = False
          self._objective = None;

      def getObjective(self, current = None):
          self.errorIfUnloaded()
          return self._objective

      def setObjective(self, _objective, current = None):
          self.errorIfUnloaded()
          self._objective = _objective
          pass


      def ice_postUnmarshal(self):
          """
          Provides additional initialization once all data loaded
          """
          pass # Currently unused


      def ice_preMarshal(self):
          """
          Provides additional validation before data is sent
          """
          pass # Currently unused

      def __getattr__(self, name):
          import __builtin__
          """
          Reroutes all access to object.field through object.getField() or object.isField()
          """
          field  = "_" + name
          capitalized = name[0].capitalize() + name[1:]
          getter = "get" + capitalized
          questn = "is" + capitalized
          try:
              self.__dict__[field]
              if hasattr(self, getter):
                  method = getattr(self, getter)
                  return method()
              elif hasattr(self, questn):
                  method = getattr(self, questn)
                  return method()
          except:
              pass
          raise AttributeError("'%s' object has no attribute '%s' or '%s'" % (self.__class__.__name__, getter, questn))

      def __setattr__(self, name, value):
          """
          Reroutes all access to object.field through object.getField(), with the caveat
          that all sets on variables starting with "_" are permitted directly.
          """
          if name.startswith("_"):
              self.__dict__[name] = value
              return
          else:
              field  = "_" + name
              setter = "set" + name[0].capitalize() + name[1:]
              if hasattr(self, field) and hasattr(self, setter):
                  method = getattr(self, setter)
                  return method(value)
          raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, setter))

_omero_model.ObjectiveSettingsI = ObjectiveSettingsI

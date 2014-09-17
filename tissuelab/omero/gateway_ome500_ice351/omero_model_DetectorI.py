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
IceImport.load("omero_model_Detector_ice")
from omero.rtypes import rlong
_omero = Ice.openModule("omero")
_omero_model = Ice.openModule("omero.model")
__name__ = "omero.model"
class DetectorI(_omero_model.Detector):

      MANUFACTURER =  "ome.model.acquisition.Detector_manufacturer"
      MODEL =  "ome.model.acquisition.Detector_model"
      LOTNUMBER =  "ome.model.acquisition.Detector_lotNumber"
      SERIALNUMBER =  "ome.model.acquisition.Detector_serialNumber"
      VOLTAGE =  "ome.model.acquisition.Detector_voltage"
      GAIN =  "ome.model.acquisition.Detector_gain"
      OFFSETVALUE =  "ome.model.acquisition.Detector_offsetValue"
      ZOOM =  "ome.model.acquisition.Detector_zoom"
      AMPLIFICATIONGAIN =  "ome.model.acquisition.Detector_amplificationGain"
      TYPE =  "ome.model.acquisition.Detector_type"
      INSTRUMENT =  "ome.model.acquisition.Detector_instrument"
      DETAILS =  "ome.model.acquisition.Detector_details"
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
          super(DetectorI, self).__init__()
          # Relying on omero.rtypes.rlong's error-handling
          self._id = rlong(id)
          self._loaded = loaded
          if self._loaded:
             self._details = _omero_model.DetailsI()
             self._toggleCollectionsLoaded(True)

      def unload(self, current = None):
          self._loaded = False
          self.unloadManufacturer( )
          self.unloadModel( )
          self.unloadLotNumber( )
          self.unloadSerialNumber( )
          self.unloadVoltage( )
          self.unloadGain( )
          self.unloadOffsetValue( )
          self.unloadZoom( )
          self.unloadAmplificationGain( )
          self.unloadType( )
          self.unloadInstrument( )
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
            copy = DetectorI()
            copy._id = self._id;
            copy._version = self._version;
            copy._details = None  # Unloading for the moment.
            raise omero.ClientError("NYI")
      def proxy(self, current = None):
          if self._id is None: raise omero.ClientError("Proxies require an id")
          return DetectorI( self._id.getValue(), False )

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

      def unloadManufacturer(self, ):
          self._manufacturerLoaded = False
          self._manufacturer = None;

      def getManufacturer(self, current = None):
          self.errorIfUnloaded()
          return self._manufacturer

      def setManufacturer(self, _manufacturer, current = None):
          self.errorIfUnloaded()
          self._manufacturer = _manufacturer
          pass

      def unloadModel(self, ):
          self._modelLoaded = False
          self._model = None;

      def getModel(self, current = None):
          self.errorIfUnloaded()
          return self._model

      def setModel(self, _model, current = None):
          self.errorIfUnloaded()
          self._model = _model
          pass

      def unloadLotNumber(self, ):
          self._lotNumberLoaded = False
          self._lotNumber = None;

      def getLotNumber(self, current = None):
          self.errorIfUnloaded()
          return self._lotNumber

      def setLotNumber(self, _lotNumber, current = None):
          self.errorIfUnloaded()
          self._lotNumber = _lotNumber
          pass

      def unloadSerialNumber(self, ):
          self._serialNumberLoaded = False
          self._serialNumber = None;

      def getSerialNumber(self, current = None):
          self.errorIfUnloaded()
          return self._serialNumber

      def setSerialNumber(self, _serialNumber, current = None):
          self.errorIfUnloaded()
          self._serialNumber = _serialNumber
          pass

      def unloadVoltage(self, ):
          self._voltageLoaded = False
          self._voltage = None;

      def getVoltage(self, current = None):
          self.errorIfUnloaded()
          return self._voltage

      def setVoltage(self, _voltage, current = None):
          self.errorIfUnloaded()
          self._voltage = _voltage
          pass

      def unloadGain(self, ):
          self._gainLoaded = False
          self._gain = None;

      def getGain(self, current = None):
          self.errorIfUnloaded()
          return self._gain

      def setGain(self, _gain, current = None):
          self.errorIfUnloaded()
          self._gain = _gain
          pass

      def unloadOffsetValue(self, ):
          self._offsetValueLoaded = False
          self._offsetValue = None;

      def getOffsetValue(self, current = None):
          self.errorIfUnloaded()
          return self._offsetValue

      def setOffsetValue(self, _offsetValue, current = None):
          self.errorIfUnloaded()
          self._offsetValue = _offsetValue
          pass

      def unloadZoom(self, ):
          self._zoomLoaded = False
          self._zoom = None;

      def getZoom(self, current = None):
          self.errorIfUnloaded()
          return self._zoom

      def setZoom(self, _zoom, current = None):
          self.errorIfUnloaded()
          self._zoom = _zoom
          pass

      def unloadAmplificationGain(self, ):
          self._amplificationGainLoaded = False
          self._amplificationGain = None;

      def getAmplificationGain(self, current = None):
          self.errorIfUnloaded()
          return self._amplificationGain

      def setAmplificationGain(self, _amplificationGain, current = None):
          self.errorIfUnloaded()
          self._amplificationGain = _amplificationGain
          pass

      def unloadType(self, ):
          self._typeLoaded = False
          self._type = None;

      def getType(self, current = None):
          self.errorIfUnloaded()
          return self._type

      def setType(self, _type, current = None):
          self.errorIfUnloaded()
          self._type = _type
          pass

      def unloadInstrument(self, ):
          self._instrumentLoaded = False
          self._instrument = None;

      def getInstrument(self, current = None):
          self.errorIfUnloaded()
          return self._instrument

      def setInstrument(self, _instrument, current = None):
          self.errorIfUnloaded()
          self._instrument = _instrument
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

_omero_model.DetectorI = DetectorI

#! python3
from dataclasses import dataclass
from typing import List

import _contamxpy

_lib = _contamxpy.lib
_ffi = _contamxpy.ffi

MAX_LEN_VER_STR = 64
NAMELEN = 16          # contaminants, elements, schedules, levels, controls
NMLN2 = 32            # zones

#=========================================================== class Zone  =====#
class Zone:
    """Zone class used in list of zones. """

    def __init__(self, zoneNr, zoneName, flags, volume, levNr, levName) -> None:

        #: Zone number typically assigned by *ContamW*.
        self.zoneNr: int = zoneNr

        self.zoneName = zoneName
        self.flags = flags
        self.volume = volume
        self.levNr = levNr
        self.levName = levName
    
    def __repr__(self):
        return("{}({!r},{!r},{!r},{!r},{!r},{!r})".format( \
            self.__class__.__name__, self.zoneNr, self.zoneName, self.flags, \
            self.volume, self.levNr, self.levName) \
              )

#=========================================================== class Path  =====#
class Path:
    """Instances of Path are created via the :py:func:`contamxpy.prjDataReadyFcnP` callback function.  
    If the callback function is called as indicated via the :py:class:`contamxpy.cxLib` constructor, 
    then Paths will will be accessible in the :py:attr:`contamxpy.cxLib.paths` list.

    Attributes
    ----------
    pathNr
        Path number, typically assigned by *ContamW*.
    flags
        Flags used to indicate airflow path properties. Not all of these flags are relevant to co-simulation, e.g., the WPC-related flags can be ignored.
        
        Airflow path flag values:
        
        + 0x0001 possible wind pressure
        + 0x0002 path uses WPC file pressure
        + 0x0004 path uses WPC file contaminants
        + 0x0008 Simple air-handling system (SAHS) supply or return path
        + 0x0010 SAHS recirculation flow path
        + 0x0020 SAHS outside air flow path
        + 0x0040 SAHS exhaust flow path
        + 0x0080 path has associate pressure limits
        + 0x0100 path has associate flow limits
        + 0x0200 path has associated constant airflow element
        + 0x0400 junction leak path

    from_zone
        Number of *From* zone used to indicate positive flow direction: *from_zone* -> to_zone.
    to_zone
        Number of *To* zone used to indicate positive flow direction: from_zone -> *to_zone*.
    ahs_nr
        Number of the Simple AHS associated with this Path if represents either a ventilation system *supply* or *return*.
    X
        X-coordinate
    Y
        Y-coordinate
    Z
        Z-coordinate
    envIndex
        Envelope index
    """

    def __init__(self, pathNr, flags, from_zone, to_zone, ahs_nr, X, Y, Z, envIndex) -> None:
        self.pathNr = pathNr
        self.flags = flags
        self.from_zone = from_zone
        self.to_zone = to_zone
        self.ahs_nr = ahs_nr
        self.X = X
        self.Y = Y
        self.Z = Z
        self.envIndex = envIndex
    
    def __repr__(self):
        return("{}({!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r},{!r})".format( \
            self.__class__.__name__, self.pathNr, self.flags, \
            self.from_zone, self.to_zone, self.ahs_nr, self.X, self.Y, self.Z, self.envIndex) \
              )

#=========================================================== class cxLib =====#
class cxLib:
    """cxLib class provides a wrapper around ``contamx-lib``.
       The cxLib constructor. 

        wp : `int` {0, 1}, optional
            Set wind pressure calculation method :py:attr:`contamxpy.cxLib.wpMode`:
            
            + 0 = CONTAM computes wind pressures using WTH-like messages and ambient Mass Fractions using CTM-like messages, i.e., cxiSetAmbtXXX messages.
            + 1 = Use envelope-related functions of the contam-x-cosim API to set wind pressure of individual envelope flow paths (default), i.e., cxiSetEnvelopeXXX.

        cb : `bool`, optional
            Set callback option :py:attr:`contamxpy.cxLib.cbOption` for :py:func:`contamxpy.prjDataReadyFcnP`:
            
            + `False` = ``contamx-lib`` will not execute callback function.
            + `True`  = ``contamx-lib`` will execute callback function.
    """

    def __init__( self, wp: int = 0, cb: bool = False):
        
        #----- Instance Attributes -----#

        self._self_handle = _ffi.new_handle(self)
        """FFI-generated handle (`void *`)."""
        
        self._state = _lib.cxiGetContamState()
        """ContamXState obtained from ``contamx-lib`` via instantiation of :py:class:`contamxpy.cxLib` (`void *`)."""
        
        self.wpMode: int = wp
        """Wind pressure calculation mode."""

        if wp < 0 or wp > 1:
            wp = 0
        _lib.cxiSetWindPressureMode(self._state, wp)

        self.cbOption: bool = cb
        """Callback function option."""

        ### DEBUG
        ###print(f"cxLib __init__() =>\n\t_state=[{self._state}]\n\tself_handle=[{self._self_handle}]\n\tself=[{self}]\n")
        ###print(f"\tnContaminants={self.nContaminants}\n\tnZones={self.nZones}\n\tnPaths={self.nPaths}\n")

        if(cb==True):
            # {self._self_handle} is passed through to provide the callback with access 
            #   to the instance of the {cxLib} object.
            _lib.cxiRegisterCallback_PrjDataReady(self._state, self._self_handle, _lib.prjDataReadyFcnP)

        self.verbose : int = 0
        """(Read-only) Logging level {0 = none (default), 1 = medium, 2 = high}."""

        #----- PRJ-related Instance Attributes -----#

        self.nContaminants : int = -1
        """(Read-only) Number of `Contaminants` in the PRJ. Defaults to `-1`. See :py:attr:`contamxpy.cxLib.contaminants`."""

        self.contaminants = []
        """(Read-only) List of contaminant names (`list` of `str`) populated via the :py:func:`contamxpy.prjDataReadyFcnP` callback function if :py:attr:`contamxpy.cxLib.cbOption` = `True`.
        """

        self.nZones = -1
        """(Read-only) Number of `Zones` in the PRJ. Defaults to `-1`. See :py:attr:`contamxpy.cxLib.zones`."""

        self.zones = []
        """(Read-only) List of :py:class:`contamxpy.Zone` objects populated via the :py:func:`contamxpy.prjDataReadyFcnP` callback function if :py:attr:`contamxpy.cxLib.cbOption` = `True`.
        """

        self.nPaths = -1
        """(Read-only) Number of `Paths` in PRJ. Defaults to `-1`. See :py:attr:`contamxpy.cxLib.paths`."""

        self.paths = []
        """(Read-only) List of :py:class:`contamxpy.Path` objects populated via the :py:func:`contamxpy.prjDataReadyFcnP` callback function if :py:attr:`contamxpy.cxLib.cbOption` = `True`.
        """

    @staticmethod 
    def __convertString(cdataStr):
        """Private helper function used to decode C-strings to Python strings."""
        return _ffi.string(cdataStr).decode('utf-8')
    
    def setVerbosity(self, level = 0):
        """Set logging level for instance of :py:class:`contamxpy.cxLib`. See :py:attr:`contamxpy.cxLib.verbose`.
        
        Args:
            level : `int`
                Logging level:

                + 0 No logging
                + 1 Minimal logging
                + 2 Maximum logging
        """
        self.verbose = max(level,0)

    #---------- contamx-lib: simulation initialization
    ### Not needed - The _state is an attribute of cxLib obtain upon instantiation.
    ### def getState(self):
    ###     return _lib.cxiGetContamState()

    ### This function is not needed as wpMode is set via the cxLib constructor.
    ### def setWindPressureMode(state, mode):
    ###     _lib.cxiSetWindPressureMode(state, mode)

    def getVersion(self):
        """
        :returns: The version of ``contamx-lib``, i.e., the *ContamX* version, e.g., `3.4.1.4-64bit`.
        :rtype: str
        """
        bufStr = _ffi.new("char[]", MAX_LEN_VER_STR)
        _lib.cxiGetVersion(self._state, bufStr)
        return cxLib.__convertString(bufStr)

    def setupSimulation(self, prjPath, useCosim = 1):
        """Setup the simulation including the option to run ContamX in the co-simulation mode.
            Calling cxiSetupSimulation() with \p useCosim set to \e 1 will initiate the simulation 
            by reading the PRJ file, allocating simulation data, calling of the user-defined 
            callback function if set to do so via cxiRegisterCallback_PrjDataReady(), and
            running the steady state initialization. 

            Args:
                prjPath : `str`
                    The file system path to the CONTAM PRJ file on which to run the simulation
                
                useCosim: `int`
                    Select ContamX run mode: 

                    * 0 = run a CONTAM-only simulation, 
                    * 1 = run ContamX in co-simulation mode.
        """
        _lib.cxiSetupSimulation(self._state, prjPath.encode('ascii'), useCosim)

    #---------- contamx-lib: Simulation properties ----------
    def getSimTimeStep(self):
        """
        :returns: Calculation time step in seconds (1 - 60)
        :rtype: int
        """
        timeStep = _lib.cxiGetSimulationTimeStep(self._state)
        return timeStep

    def getSimStartDate(self):
        """
        :returns: Start day of year of the simulation [1 - 365]
        :rtype: int
        """
        dayOfYear = _lib.cxiGetSimulationStartDate(self._state)
        return dayOfYear

    def getSimEndDate(self):
        """
        :returns: End day of year of the simulation [1 - 365]
        :rtype: int
        """
        dayOfYear = _lib.cxiGetSimulationEndDate(self._state)
        return dayOfYear

    def getSimStartTime(self):
        """
        :returns: Start time of day the simulation in seconds [0 - 86400)
        :rtype: int
        """
        timeOfDaySeconds = _lib.cxiGetSimulationStartTime(self._state)
        return timeOfDaySeconds

    def getSimEndTime(self):
        """
        :returns: End time of day of the simulation in seconds [0 - 86400)
        :rtype: int
        """
        timeOfDaySeconds = _lib.cxiGetSimulationEndTime(self._state)
        return timeOfDaySeconds

    #---------- contamx-lib: Simulation time ----------
    def getCurrentDayOfYear(self):
        """
        :returns: Current day of year of the simulation [1 - 365]
        :rtype: int
        """
        return _lib.cxiGetCurrentDate(self._state)

    def getCurrentTimeInSec(self):
        """
        :returns: Current time of day of the simulation in seconds [0 - 86400)
        :rtype: int
        """
        return _lib.cxiGetCurrentTime(self._state)

    #----------- contamx-lib: Simulation control ----------
    def doSimStep(self, stepForward = 1):
        """Run next simulation time step.

        Args:
            stepForward : `int`
                Currently only a value of  `1` is allowed to run the next time step.
        """
        stepForward = 1
        _lib.cxiDoCoSimStep(self._state, stepForward)

    def endSimulation(self):
        """This function must be called at the end of a co-simulation. 
        This should only be called after all time steps of the co-simulation have been completed, 
        i.e., after :py:func:`contamxpy.cxLib.doSimStep` has been called for the values obtained 
        for the ending date and time of the simulation."""
        _lib.cxiEndSimulation(self._state)

    #----------- Called by prjDataReadyFcnP() ----------
    # These functions are used to populate the list of
    #   items which are members of cxLib instances.
    #
    def _getCtmName(self, i):
        """
        Args:
            i : `int`
                Contaminant number, e.g., assigned by ContamW

        :returns: Contaminant name.
        :rtype: str
        """
        nameStr = _ffi.new("char[]", NAMELEN)
        if( i >= 0 and i < self.nContaminants ):
            _lib.cxiGetCtmName(self._state, i, nameStr)
        return cxLib.__convertString(nameStr)

    def _getZoneInfo(self, i):
        """
        Args:
            i : `int`
                Zone number, e.g., assigned by ContamW

        :returns: :py:class:`contamxpy.Zone` instance for requested Zone number
        :rtype: :py:class:`contamxpy.Zone`
        """
        pz = _ffi.new("ZONE_COSIM_DSC *")
        zoneNameStr = _ffi.new("char[]", NAMELEN)
        levNameStr = _ffi.new("char[]", NAMELEN)

        if( i > 0 and i <= self.nZones ):
            _lib.cxiGetZoneInfo(self._state, i, pz)
            zoneNameStr = cxLib.__convertString(pz.name)
            levNameStr = cxLib.__convertString(pz.level_name)
            zone = Zone(pz.nr, zoneNameStr, pz.flags, pz.Vol, pz.level_nr, levNameStr)
        return zone

    def _getPathInfo(self, i):
        """
        Args:
            i : `int`
                Path number, e.g., assigned by ContamW

        :returns: :py:class:`contamxpy.Path` instance for requested Path number
        :rtype: :py:class:`contamxpy.Path`
        """
        pp = _ffi.new("PATH_COSIM_DSC *")

        if( i > 0 and i <= self.nPaths ):
            _lib.cxiGetPathInfo(self._state, i, pp)
            path = Path(pp.nr, pp.flags, pp.from_zone, pp.to_zone, pp.ahs_nr, pp.X, pp.Y, pp.Z, pp.envIndex)
        return path

#===================================================== Callback function =====#
#
@_ffi.def_extern()
def prjDataReadyFcnP(state, handle):
    """
    This function populates the list Attributes of :py:class:`cxLib` contaminants[], zones[], and paths[].

    Parameters
    ----------
    state
        The *ContamXState* obtained from ``contamx-lib`` upon instantiation of an :py:class:`contamxpy.cxLib` object.
    handle
        The CFFI handle to the current :py:class:`contamxpy.cxLib` instance.

    """

    #----- Get instance of cxLib class from pass-through data handle
    #      created in cxLib.__init__() via new_handle() FFI function.
    cxlib = _ffi.from_handle(handle)
    if cxlib.verbose > 0:
        print(f"prjDataReadFcnP(\n\tstate=[{state}]\n\tpData=[{handle}]\n\tuser_data=[{cxlib}]\n)\n")

    #----- Get data from the state
    #
    cxlib.nContaminants = _lib.cxiGetNumCtms(state)
    cxlib.nZones = _lib.cxiGetNumZones(state)
    cxlib.nPaths = _lib.cxiGetNumPaths(state)
    ### DEBUG ###
    if cxlib.verbose > 0:
        print(f"\tnContaminants={cxlib.nContaminants}\n\tnZones={cxlib.nZones}\n\tnPaths={cxlib.nPaths}\n")

    #----- Get list of Contaminants from contamx-lib
    #
    for i in range(cxlib.nContaminants):
        name = cxlib._getCtmName(i)
        if( len(name) <= 0 ):
            print(f"ERROR: cxiGetCtmName({i})\n")
        else:
            cxlib.contaminants.append(name)
    if(cxlib.verbose > 0):
        print(f"Contaminants = {cxlib.contaminants}\n")

    #----- Get list of Zones from contamx-lib
    #  and populate cxlib zones list with Zone objects.
    #  NOTE: zones indexed from 1->nZones.
    #
    for i in range(cxlib.nZones):
        z = cxlib._getZoneInfo(i+1)
        cxlib.zones.append(z)

    if(cxlib.verbose > 0):
        print(f"Zones = {cxlib.zones}\n")

    #----- Get list of Paths from contamx-lib
    #  and populate cxlib path list with Path objects.
    #  NOTE: paths indexed from 1->nPaths.
    #
    for i in range(cxlib.nPaths):
        p = cxlib._getPathInfo(i+1)
        cxlib.paths.append(p)

    if(cxlib.verbose > 0):
        print(f"Paths = {cxlib.paths}\n")

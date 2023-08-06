#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2022 by Frank Brehm, Berlin
@summary: The module for special error classes on VSphere API operations.
"""
from __future__ import absolute_import

# Standard modules

# Third party modules

from fb_tools.errors import FbHandlerError

# Own modules
from .xlate import XLATOR

__version__ = '0.3.3'

_ = XLATOR.gettext


# =============================================================================
class FbVMWareError(FbHandlerError):
    """Base class for all exception belonging to VSphere/VMWare."""
    pass


# =============================================================================
class BaseVSphereHandlerError(FbVMWareError):
    """Base class for all exception belonging to VSphere."""
    pass


# =============================================================================
class VSphereHandlerError(BaseVSphereHandlerError):
    """Base class for all exception belonging to VSphere."""
    pass


# =============================================================================
class VSphereNoDatastoresFoundError(FbHandlerError):

    # -------------------------------------------------------------------------
    def __init__(self, msg=None):

        if not msg:
            msg = _("No VSphere datastores found.")
        self.msg = msg

    # -------------------------------------------------------------------------
    def __str__(self):

        return self.msg


# =============================================================================
class VSphereExpectedError(VSphereHandlerError):
    """Base class for all errors, which could be expected in application object
        and displayed without stack trace."""
    pass


# =============================================================================
class VSphereNameError(VSphereExpectedError):
    """Special error class for invalid Vsphere object names."""

    # -------------------------------------------------------------------------
    def __init__(self, name, obj_type=None):

        self.name = name
        self.obj_type = obj_type

    # -------------------------------------------------------------------------
    def __str__(self):

        if self.obj_type:
            msg = _("Invalid name {n!r} for a {o} VSphere object.").format(
                n=self.name, o=self.obj_type)
        else:
            msg = _("Invalid name {!r} for a VSphere object.").format(self.name)

        return msg


# =============================================================================
class VSphereDatacenterNotFoundError(VSphereExpectedError):
    """Special error class for the case, that the given datacenter
         was not found in VSphere."""

    # -------------------------------------------------------------------------
    def __init__(self, dc):

        self.dc = dc

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("The VSphere datacenter {!r} is not existing.").format(self.dc)
        return msg


# =============================================================================
class VSphereVmNotFoundError(VSphereExpectedError):
    """Special error class for the case, that the given VM was not found in VSphere."""

    # -------------------------------------------------------------------------
    def __init__(self, vm):

        self.vm = vm

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("The VSphere Virtual machine {!r} was not found.").format(self.vm)
        return msg


# =============================================================================
class VSphereNoDatastoreFoundError(VSphereExpectedError):
    """Special error class for the case, that no SAN based data store was with
        enogh free space was found."""

    # -------------------------------------------------------------------------
    def __init__(self, needed_bytes):

        self.needed_bytes = int(needed_bytes)

    # -------------------------------------------------------------------------
    def __str__(self):

        mb = float(self.needed_bytes) / 1024.0 / 1024.0
        gb = mb / 1024.0

        msg = _(
            "No SAN based datastore found with at least {m:0.0f} MiB == {g:0.1f} GiB "
            "available space found.").format(m=mb, g=gb)
        return msg


# =============================================================================
class VSphereNetworkNotExistingError(VSphereExpectedError):
    """Special error class for the case, if the expected network is not existing."""

    # -------------------------------------------------------------------------
    def __init__(self, net_name):

        self.net_name = net_name

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("The network {!r} is not existing.").format(self.net_name)
        return msg


# =============================================================================
class VSphereCannotConnectError(VSphereExpectedError):
    """Special error class for the case, it cannot connect
        to the given vSphere server."""

    # -------------------------------------------------------------------------
    def __init__(self, url):

        self.url = url

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("Could not connect to the vSphere {!r}.").format(self.url)
        return msg

# =============================================================================
class VSphereVimFault(VSphereExpectedError):
    """Special error class for the case, it cannot connect
        to the given vSphere server and gets a vim.fault.VimFault."""

    # -------------------------------------------------------------------------
    def __init__(self, fault, url):

        self.fault = fault
        self.url = url

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("Got a {c} on connecting to vSphere {url!r}:").format(
            c=self.fault.__class__.__name__, url=self.url)
        msg += ' ' + self.fault.msg
        return msg


# =============================================================================
class TimeoutCreateVmError(VSphereExpectedError):

    # -------------------------------------------------------------------------
    def __init__(self, vm, timeout=None):

        t_o = None
        if timeout is not None:
            t_o = float(timeout)
        self.timeout = t_o

        self.vm = vm

    # -------------------------------------------------------------------------
    def __str__(self):

        if self.timeout is not None:
            msg = _("Timeout on creating VM {vm!r} after {to:0.1f} seconds.").format(
                vm=self.vm, to=self.timeout)
        else:
            msg = _("Timeout on creating VM {!r}.").format(self.vm)
        return msg


# =============================================================================
class WrongPortTypeError(FbVMWareError, TypeError):

    # -------------------------------------------------------------------------
    def __init__(self, port, emesg=None):

        self.port = port
        self.emesg = emesg

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _("Invalid type of {!r} for a port of a VSPhere server").format(self.port)
        if self.emesg:
            msg += ': ' + self.emesg
        else:
            msg += '.'

        return msg

# =============================================================================
class WrongPortValueError(FbVMWareError, ValueError):

    default_max_port = (2 ** 16) - 1

    # -------------------------------------------------------------------------
    def __init__(self, port, max_port=None):

        self.port = port
        self.max_port = max_port
        if self.max_port is None:
            self.max_port = self.default_max_port

    # -------------------------------------------------------------------------
    def __str__(self):

        msg = _(
            "Invalid port number {port!r} for the VSphere server, "
            "PORT must be greater than zero and less or equal to {max}.").format(
            port=self.port, max=self.max_port)

        return msg


# =============================================================================
if __name__ == "__main__":

    pass

# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 list

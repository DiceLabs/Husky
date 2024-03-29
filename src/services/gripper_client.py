#!/usr/bin/env python3

from client import call_service
from services import ServiceNames, ServicePorts
from req_resp import GenericRequest

call_service(port=ServicePorts[ServiceNames.RIGHT_GRIPPER], request=GenericRequest(function="close", args={}))
call_service(port=ServicePorts[ServiceNames.RIGHT_GRIPPER], request=GenericRequest(function="open", args={}))
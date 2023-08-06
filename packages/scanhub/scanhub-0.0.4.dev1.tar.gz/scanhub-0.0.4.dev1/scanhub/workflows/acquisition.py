# Authors: Christoph Dinh <christoph.dinh@brain-link.de>
#          Johannes Behrens <johannes.behrens@brain-link.de>
#          David Schote <david.schote@brain-link.de>
#
# License: BSD-3-Clause


from enum import IntEnum
from uuid import UUID

from pydantic import BaseModel, StrictStr

class AcquisitionCommand(IntEnum):
    start = 1001
    stop = 1002
    pause = 1003

class AcquisitionEvent(BaseModel):
    """RecoJob is a pydantic model for a reco job.""" # noqa: E501
    device_id: int | str | UUID
    record_id: int | str | UUID
    command_id: AcquisitionCommand
    input_sequence: StrictStr
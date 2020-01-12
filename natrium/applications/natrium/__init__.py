from fastapi import APIRouter
from starlette.responses import FileResponse
from pathlib import Path
from .depends import JSONForm
from natrium import app
from i18n import t as Ts_

router = APIRouter()

@router.get("/static/picture/resource/{resource}", tags=["Utils"],
    summary=Ts_("apidoc.utils.static_resource.summary"),
    description=Ts_("apidoc.utils.static_resource.description"),
)
async def static_resource(resource: str):
    return FileResponse(str(Path(f"./assets/resources/{resource}.png").absolute()))

import natrium.applications.natrium.buckets
import natrium.applications.natrium.exceptions

# sub.
import natrium.applications.natrium.paths.authserver
import natrium.applications.natrium.paths.resourceserver
import natrium.applications.natrium.paths.optionserver
import natrium.applications.natrium.paths.amadeus
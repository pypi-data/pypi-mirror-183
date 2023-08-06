from __future__ import annotations

import urllib
from typing import Optional, Union

from vectice.api.http_error_handlers import InvalidReferenceError, MissingReferenceError
from vectice.api.json.model import ModelOutput
from vectice.api.project import ProjectApi
from vectice.api.rest_api import HttpError, RestApi


class ModelApi(RestApi):
    def get_model(
        self,
        model: Union[str, int],
        project: Optional[Union[str, int]] = None,
        workspace: Optional[Union[str, int]] = None,
    ):
        if not isinstance(model, int) and not isinstance(model, str):
            raise InvalidReferenceError("model", model)
        if isinstance(model, int):
            parent_project = None
            url = f"/metadata/model/{model}"
        else:
            if project is None:
                raise MissingReferenceError("project")
            parent_project = ProjectApi(self.auth).get_project(project, workspace)
            url = f"/metadata/project/{parent_project.id}/model/name/{urllib.parse.quote(model)}"
        try:
            response = self.get(url)
            result = ModelOutput(response)
            if parent_project is not None:
                result.project = parent_project
            return result
        except HttpError as e:
            raise self._httpErrorHandler.handle_get_http_error(e, "model", model)

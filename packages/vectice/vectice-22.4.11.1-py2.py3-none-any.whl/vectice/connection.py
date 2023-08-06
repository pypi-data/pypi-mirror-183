from __future__ import annotations

import logging
from typing import TYPE_CHECKING, List, Optional, Union

from vectice.api import Client
from vectice.models.workspace import Workspace
from vectice.utils.configuration import Configuration
from vectice.utils.last_assets import _get_last_used_assets_and_logging

if TYPE_CHECKING:
    from vectice.models.project import Project


_logger = logging.getLogger(__name__)
CAN_NOT_BE_EMPTY_ERROR_MESSAGE = "%s can not be empty."


class Connection:
    """Connect to the Vectice backend (application).

    Authentication credentials are retrieved, in order, from keyword
    arguments else from environment variables.

    """

    def __init__(
        self,
        api_token: Optional[str] = None,
        host: Optional[str] = None,
        workspace: Optional[Union[str, int]] = None,
    ):
        """
        :param api_token: Your private api token.
        :param host: The address of the Vectice application.
        :param workspace: The workspace you want to work in.
        """
        logging.getLogger("Client").propagate = True
        self._client = Client(
            workspace=workspace,
            token=api_token,
            api_endpoint=host,
            auto_connect=True,
            allow_self_certificate=True,
        )
        _logger.info("Vectice successfully connected.")
        compatibility = self._client.check_compatibility()
        if compatibility.status != "OK":
            if compatibility.status == "Error":
                _logger.error(f"compatibility error: {compatibility.message}")
                raise RuntimeError(f"compatibility error: {compatibility.message}")
            else:
                _logger.warning(f"compatibility warning: {compatibility.message}")

    def __repr__(self) -> str:
        return (
            "Connection("
            + f"workspace={self._client.workspace.name if self._client.workspace else 'None'}, "
            + f"host={self._client.auth.api_base_url}, "
        )

    def workspace(self, workspace: Union[str, int]) -> Workspace:
        """Return a workspace.

        :param workspace: The id or the name of the desired workspace.
        :return: Workspace
        """
        output = self._client.get_workspace(workspace)
        result = Workspace(output.id, output.name, output.description)
        result.__post_init__(self._client, self)
        return result

    @property
    def workspaces(self) -> Optional[List[Workspace]]:
        """
        List workspaces.

        List the workspaces to which this connection has access.

        :return: List of Workspaces
        """
        outputs = self._client.list_workspaces()
        results = [Workspace(id=output.id, name=output.name, description=output.description) for output in outputs.list]
        for workspace in results:
            workspace.__post_init__(self._client, self)
        return results

    @staticmethod
    def connect(
        api_token: Optional[str] = None,
        host: Optional[str] = None,
        config: Optional[str] = None,
        workspace: Optional[Union[str, int]] = None,
        project: Optional[str] = None,
    ) -> Optional[Union[Connection, Workspace, Project]]:
        """Factory method to connect to the Vectice backend (application).

        Authentication credentials are retrieved, in order, from
        keyword arguments else from environment variables.

        Uses the api_token, host, workspace, project or json config
        provided.  The json config file is available from the Vectice
        webapp when creating an API token.

        :param api_token:  The api token provided by the Vectice webapp
        :param host:  The backend host to which the client will connect
        :param config:  A JSON config file containing keys VECTICE_API_TOKEN and VECTICE_API_ENDPOINT as well as optionally WORKSPACE and PROJECT
        :param workspace:  The name of an optional workspace to return.
        :param project:  The name of an optional project to return.
        :return:  A Connection, Workspace, or Project.

        """
        if config:
            configuration = Configuration(config)
            workspace = configuration.workspace
            project = configuration.project
            api_token = configuration.api_token
            host = configuration.host
        if host == "":
            raise ValueError(CAN_NOT_BE_EMPTY_ERROR_MESSAGE % "The host")
        if api_token == "":  # nosec B105
            raise ValueError(CAN_NOT_BE_EMPTY_ERROR_MESSAGE % "The API token")  # nosec B105
        connection = Connection(api_token=api_token, host=host)
        if workspace == "":
            raise ValueError(CAN_NOT_BE_EMPTY_ERROR_MESSAGE % "The workspace name")
        if project == "":
            raise ValueError(CAN_NOT_BE_EMPTY_ERROR_MESSAGE % "The project name")
        if workspace and not project:
            workspace_output: Workspace = connection.workspace(workspace)
            _logger.info(f"Your current workspace: {workspace_output.name}")
            _get_last_used_assets_and_logging(connection._client, _logger, workspace_output.name)
            return workspace_output
        elif workspace and project:
            logging.getLogger("vectice.models.workspace").propagate = False
            workspace_output = connection.workspace(workspace)
            project_output: Project = workspace_output.project(project)
            _logger.info(f"Your current workspace: {workspace_output.name} and project: {project_output.name}")
            _get_last_used_assets_and_logging(connection._client, _logger, workspace_output.name)
            return project_output
        elif project and not workspace:
            raise ValueError("A workspace reference is needed to retrieve a project.")
        return connection

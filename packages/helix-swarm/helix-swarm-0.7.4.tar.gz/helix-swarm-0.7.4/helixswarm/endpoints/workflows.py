from typing import Dict, List, Optional, Union

from helixswarm.helpers import minimal_version


class Workflows:

    def __init__(self, swarm) -> None:
        self.swarm = swarm

    @minimal_version(9)
    def get(self,
            *,
            fields: Optional[List[str]] = None,
            no_cache: Optional[bool] = None
            ) -> dict:
        """
        Gets workflows.

        Args:
            fields (Optional[List[str]]):
                An optional list of fields to show for each workflow. Omitting
                this parameter or passing an empty value shows all fields.

            noCache (Optional[bool]):
                If provided and has a value of 'true' a query will always be
                performed and the cache of workflows is ignored. Otherwise the
                cache will be used if it exists.

        Returns:
            dict: json response.
        """
        params = dict()  # type: Dict[str, Union[str, bool]]

        if fields:
            params['fields'] = ','.join(fields)

        if no_cache:
            params['noCache'] = no_cache

        return self.swarm._request('GET', 'workflows', params=params)

    @minimal_version(9)
    def get_info(self,
                 identifier: int,
                 *,
                 fields: Optional[List[str]] = None
                 ) -> dict:
        """
        Gets a workflow by identifier.

        Args:
            identifier (int):
                Workflow id.

            fields (Optional[List[str]):
                An optional list of fields to show for each workflow. Omitting
                this parameter or passing an empty value shows all fields.

        Returns:
            dict: json response.
        """
        params = dict()  # type: Dict[str, str]

        if fields:
            params['fields'] = ','.join(fields)

        response = self.swarm._request(
            'GET',
            'workflows/{}'.format(identifier),
            params=params
        )

        return response

    @minimal_version(9)
    def create(self,
               name: str,
               *,
               description: Optional[str] = None,
               shared: Optional[bool] = None,
               owners: Optional[List[str]] = None,
               on_submit: Optional[List[str]] = None,
               end_rules: Optional[List[str]] = None,
               auto_approve: Optional[List[str]] = None,
               counted_votes: Optional[str] = None
               ) -> dict:
        """
        Create a new workflow.

        Args:
            name (str):
                The workflow name. Will be compared against other workflows and
                rejected if not unique.

            description (Optional[str]):
                Description for the new workflow.

            shared (Optional[bool]):
                Whether this workflow is shared for other users that do not own
                it. Defaults to not shared.

            owners (Optional[List[str]):
                A list owners for the workflow. Can be users or group names,
                prefixed with `swarm-group-`. Users and group names must exist
                or the workflow will be rejected.

            on_submit (Optional[List[str]]):
                Data for rules when changes are submitted. Valid values for
                with_review are no_checking, approved, strict. Valid values for
                without review are: `no_checking`, `auto_create`, `reject`.

            end_rules (Optional[List[str]):
                Data for rules when changes are submitted. Valid values are:
                `no_checking`, `no_revision`.

            auto_approve (Optional[List[str]):
                Data for rules when changes are submitted. Valid values are:
                `votes`, ``never``.

            counted_votes (Optional[str]):
                Data for rules when counting votes up. Valid values are: `anyone`,
                `members`.

        Returns:
            dict: json response.
        """
        data = dict(
            name=name,
        )  # type: Dict[str, Union[str, bool, List[str]]]

        if description:
            data['description'] = description

        if shared:
            data['shared'] = shared

        if owners:
            data['owners'] = owners

        if on_submit:
            data['on_submit'] = on_submit

        if end_rules:
            data['end_rules'] = end_rules

        if auto_approve:
            data['auto_approve'] = auto_approve

        if counted_votes:
            data['counted_votes'] = counted_votes

        return self.swarm._request('POST', 'workflows', data=data)

    @minimal_version(9)
    def edit(self,
             identifier: str,
             *,
             name: Optional[str] = None,
             description: Optional[str] = None,
             shared: Optional[bool] = None,
             owners: Optional[List[str]] = None,
             on_submit: Optional[dict] = None,
             end_rules: Optional[List[str]] = None,
             auto_approve: Optional[List[str]] = None,
             counted_votes: Optional[str] = None
             ) -> dict:
        """
        Edit a workflow.

        Args:
            identifier (str):
                The id of the workflow being edited.

            name (Optional[str]):
                The workflow name. Will be compared against other workflows and
                rejected if not unique.

            description (Optional[str]):
                Description for the new workflow.

            shared (Optional[bool]):
                Whether this workflow is shared for other users that do not own
                it. Defaults to not shared.

            owners (Optional[List[str]):
                A list owners for the workflow. Can be users or group names,
                prefixed with `swarm-group-`. Users and group names must exist
                or the workflow will be rejected.

            on_submit (Optional[dict]):
                Data for rules when changes are submitted. Valid values for
                with_review are no_checking, approved, strict. Valid values for
                without review are: `no_checking`, `auto_create`, `reject`.

            end_rules (Optional[List[str]]):
                Data for rules when changes are submitted. Valid values are:
                `no_checking`, `no_revision`.

            auto_approve (Optional[List[str]`` (optional)
                Data for rules when changes are submitted. Valid values are:
                `votes`, `never`.

            counted_votes (Optional[str]):
                Data for rules when counting votes up. Valid values are:
                `anyone`, `members`.

        Returns:
            dict: json response.
        """
        data = dict(
            id=identifier,
        )  # type: Dict[str, Union[str, bool, dict, List[str]]]

        if name:
            data['name'] = name

        if description:
            data['description'] = description

        if shared:
            data['shared'] = shared

        if owners:
            data['owners'] = owners

        if on_submit:
            data['on_submit'] = on_submit

        if end_rules:
            data['end_rules'] = end_rules

        if auto_approve:
            data['auto_approve'] = auto_approve

        if counted_votes:
            data['counted_votes'] = counted_votes

        response = self.swarm._request(
            'PATCH',
            'workflows/{}'.format(identifier),
            data=data
        )

        return response

    @minimal_version(9)
    def delete(self, identifier: str) -> dict:
        """
        Delete a workflow. This call must be authenticated and the user must
        have permission to edit the workflow. If the workflow is in use it
        cannot be deleted and an error message will be returned

        Args:
            identifier (str):
                The id of the workflow being deleted.

        Returns:
            dict: json response.
        """
        return self.swarm._request('DELETE', 'workflows/{}'.format(identifier))

    @minimal_version(9)
    def update(self,
               identifier: str,
               name: str,
               *,
               description: Optional[str] = None,
               shared: Optional[bool] = None,
               owners: Optional[List[str]] = None,
               on_submit: Optional[dict] = None,
               end_rules: Optional[List[str]] = None,
               auto_approve: Optional[List[str]] = None,
               counted_votes: Optional[str] = None
               ) -> dict:
        """
        Update a workflow. All values should be provided in the request.
        If not provided any missing values are reverted to default.

        Args:
            identifier (str):
                The id of the workflow being edited.

            name (Optional[str]):
                The workflow name. Will be compared against other workflows and
                rejected if not unique.

            description (Optional[str]):
                Description for the new workflow.

            shared (Optional[bool]):
                Whether this workflow is shared for other users that do not own
                it. Defaults to not shared.

            owners (Optional[List[str]):
                A list owners for the workflow. Can be users or group names,
                prefixed with `swarm-group-`. Users and group names must exist
                or the workflow will be rejected.

            on_submit (Optional[dict]):
                Data for rules when changes are submitted. Valid values for
                with_review are no_checking, approved, strict. Valid values for
                without review are: `no_checking`, `auto_create`, `reject`.

            end_rules (Optional[List[str]]):
                Data for rules when changes are submitted. Valid values are:
                `no_checking`, `no_revision`.

            auto_approve (Optional[List[str]]):
                Data for rules when changes are submitted. Valid values are:
                `votes`, `never`.

            counted_votes (Optional[str]):
                Data for rules when counting votes up. Valid values are:
                `anyone`, `members`.

        Returns:
            dict: json response.
        """
        data = dict(
            id=identifier,
            name=name,
        )  # type: Dict[str, Union[str, bool, dict, List[str]]]

        if description:
            data['description'] = description

        if shared:
            data['shared'] = shared

        if owners:
            data['owners'] = owners

        if on_submit:
            data['on_submit'] = on_submit

        if end_rules:
            data['end_rules'] = end_rules

        if auto_approve:
            data['auto_approve'] = auto_approve

        if counted_votes:
            data['counted_votes'] = counted_votes

        response = self.swarm._request(
            'PUT',
            'workflows/{}'.format(identifier),
            data=data
        )

        return response

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.authorization_update import AuthorizationUpdate
from ...models.patc_hauthorizationsauthorization_id_response_200 import PATCHauthorizationsauthorizationIdResponse200
from ...types import Response


def _get_kwargs(
    authorization_id: str,
    *,
    client: Client,
    json_body: AuthorizationUpdate,
) -> Dict[str, Any]:
    url = "{}/authorizations/{authorizationId}".format(client.base_url, authorizationId=authorization_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[PATCHauthorizationsauthorizationIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHauthorizationsauthorizationIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHauthorizationsauthorizationIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    authorization_id: str,
    *,
    client: Client,
    json_body: AuthorizationUpdate,
) -> Response[PATCHauthorizationsauthorizationIdResponse200]:
    """Update an authorization

     Update an authorization

    Args:
        authorization_id (str):
        json_body (AuthorizationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHauthorizationsauthorizationIdResponse200]
    """

    kwargs = _get_kwargs(
        authorization_id=authorization_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    authorization_id: str,
    *,
    client: Client,
    json_body: AuthorizationUpdate,
) -> Optional[PATCHauthorizationsauthorizationIdResponse200]:
    """Update an authorization

     Update an authorization

    Args:
        authorization_id (str):
        json_body (AuthorizationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHauthorizationsauthorizationIdResponse200]
    """

    return sync_detailed(
        authorization_id=authorization_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    authorization_id: str,
    *,
    client: Client,
    json_body: AuthorizationUpdate,
) -> Response[PATCHauthorizationsauthorizationIdResponse200]:
    """Update an authorization

     Update an authorization

    Args:
        authorization_id (str):
        json_body (AuthorizationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHauthorizationsauthorizationIdResponse200]
    """

    kwargs = _get_kwargs(
        authorization_id=authorization_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    authorization_id: str,
    *,
    client: Client,
    json_body: AuthorizationUpdate,
) -> Optional[PATCHauthorizationsauthorizationIdResponse200]:
    """Update an authorization

     Update an authorization

    Args:
        authorization_id (str):
        json_body (AuthorizationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHauthorizationsauthorizationIdResponse200]
    """

    return (
        await asyncio_detailed(
            authorization_id=authorization_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

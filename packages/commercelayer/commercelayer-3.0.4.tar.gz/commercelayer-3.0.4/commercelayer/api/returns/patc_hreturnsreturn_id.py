from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hreturnsreturn_id_response_200 import PATCHreturnsreturnIdResponse200
from ...models.return_update import ReturnUpdate
from ...types import Response


def _get_kwargs(
    return_id: str,
    *,
    client: Client,
    json_body: ReturnUpdate,
) -> Dict[str, Any]:
    url = "{}/returns/{returnId}".format(client.base_url, returnId=return_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHreturnsreturnIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHreturnsreturnIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHreturnsreturnIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    return_id: str,
    *,
    client: Client,
    json_body: ReturnUpdate,
) -> Response[PATCHreturnsreturnIdResponse200]:
    """Update a return

     Update a return

    Args:
        return_id (str):
        json_body (ReturnUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHreturnsreturnIdResponse200]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    return_id: str,
    *,
    client: Client,
    json_body: ReturnUpdate,
) -> Optional[PATCHreturnsreturnIdResponse200]:
    """Update a return

     Update a return

    Args:
        return_id (str):
        json_body (ReturnUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHreturnsreturnIdResponse200]
    """

    return sync_detailed(
        return_id=return_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    return_id: str,
    *,
    client: Client,
    json_body: ReturnUpdate,
) -> Response[PATCHreturnsreturnIdResponse200]:
    """Update a return

     Update a return

    Args:
        return_id (str):
        json_body (ReturnUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHreturnsreturnIdResponse200]
    """

    kwargs = _get_kwargs(
        return_id=return_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    return_id: str,
    *,
    client: Client,
    json_body: ReturnUpdate,
) -> Optional[PATCHreturnsreturnIdResponse200]:
    """Update a return

     Update a return

    Args:
        return_id (str):
        json_body (ReturnUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHreturnsreturnIdResponse200]
    """

    return (
        await asyncio_detailed(
            return_id=return_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

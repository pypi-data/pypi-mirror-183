from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hwire_transferswire_transfer_id_response_200 import PATCHwireTransferswireTransferIdResponse200
from ...models.wire_transfer_update import WireTransferUpdate
from ...types import Response


def _get_kwargs(
    wire_transfer_id: str,
    *,
    client: Client,
    json_body: WireTransferUpdate,
) -> Dict[str, Any]:
    url = "{}/wire_transfers/{wireTransferId}".format(client.base_url, wireTransferId=wire_transfer_id)

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
) -> Optional[PATCHwireTransferswireTransferIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHwireTransferswireTransferIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHwireTransferswireTransferIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wire_transfer_id: str,
    *,
    client: Client,
    json_body: WireTransferUpdate,
) -> Response[PATCHwireTransferswireTransferIdResponse200]:
    """Update a wire transfer

     Update a wire transfer

    Args:
        wire_transfer_id (str):
        json_body (WireTransferUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwireTransferswireTransferIdResponse200]
    """

    kwargs = _get_kwargs(
        wire_transfer_id=wire_transfer_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wire_transfer_id: str,
    *,
    client: Client,
    json_body: WireTransferUpdate,
) -> Optional[PATCHwireTransferswireTransferIdResponse200]:
    """Update a wire transfer

     Update a wire transfer

    Args:
        wire_transfer_id (str):
        json_body (WireTransferUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwireTransferswireTransferIdResponse200]
    """

    return sync_detailed(
        wire_transfer_id=wire_transfer_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    wire_transfer_id: str,
    *,
    client: Client,
    json_body: WireTransferUpdate,
) -> Response[PATCHwireTransferswireTransferIdResponse200]:
    """Update a wire transfer

     Update a wire transfer

    Args:
        wire_transfer_id (str):
        json_body (WireTransferUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwireTransferswireTransferIdResponse200]
    """

    kwargs = _get_kwargs(
        wire_transfer_id=wire_transfer_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wire_transfer_id: str,
    *,
    client: Client,
    json_body: WireTransferUpdate,
) -> Optional[PATCHwireTransferswireTransferIdResponse200]:
    """Update a wire transfer

     Update a wire transfer

    Args:
        wire_transfer_id (str):
        json_body (WireTransferUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwireTransferswireTransferIdResponse200]
    """

    return (
        await asyncio_detailed(
            wire_transfer_id=wire_transfer_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

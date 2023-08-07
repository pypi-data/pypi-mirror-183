from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.inventory_return_location_update import InventoryReturnLocationUpdate
from ...models.patc_hinventory_return_locationsinventory_return_location_id_response_200 import (
    PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200,
)
from ...types import Response


def _get_kwargs(
    inventory_return_location_id: str,
    *,
    client: Client,
    json_body: InventoryReturnLocationUpdate,
) -> Dict[str, Any]:
    url = "{}/inventory_return_locations/{inventoryReturnLocationId}".format(
        client.base_url, inventoryReturnLocationId=inventory_return_location_id
    )

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
) -> Optional[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    inventory_return_location_id: str,
    *,
    client: Client,
    json_body: InventoryReturnLocationUpdate,
) -> Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    """Update an inventory return location

     Update an inventory return location

    Args:
        inventory_return_location_id (str):
        json_body (InventoryReturnLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]
    """

    kwargs = _get_kwargs(
        inventory_return_location_id=inventory_return_location_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    inventory_return_location_id: str,
    *,
    client: Client,
    json_body: InventoryReturnLocationUpdate,
) -> Optional[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    """Update an inventory return location

     Update an inventory return location

    Args:
        inventory_return_location_id (str):
        json_body (InventoryReturnLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]
    """

    return sync_detailed(
        inventory_return_location_id=inventory_return_location_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    inventory_return_location_id: str,
    *,
    client: Client,
    json_body: InventoryReturnLocationUpdate,
) -> Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    """Update an inventory return location

     Update an inventory return location

    Args:
        inventory_return_location_id (str):
        json_body (InventoryReturnLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]
    """

    kwargs = _get_kwargs(
        inventory_return_location_id=inventory_return_location_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    inventory_return_location_id: str,
    *,
    client: Client,
    json_body: InventoryReturnLocationUpdate,
) -> Optional[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]:
    """Update an inventory return location

     Update an inventory return location

    Args:
        inventory_return_location_id (str):
        json_body (InventoryReturnLocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHinventoryReturnLocationsinventoryReturnLocationIdResponse200]
    """

    return (
        await asyncio_detailed(
            inventory_return_location_id=inventory_return_location_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

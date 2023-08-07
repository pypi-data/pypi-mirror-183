from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hprice_volume_tiersprice_volume_tier_id_response_200 import (
    PATCHpriceVolumeTierspriceVolumeTierIdResponse200,
)
from ...models.price_volume_tier_update import PriceVolumeTierUpdate
from ...types import Response


def _get_kwargs(
    price_volume_tier_id: str,
    *,
    client: Client,
    json_body: PriceVolumeTierUpdate,
) -> Dict[str, Any]:
    url = "{}/price_volume_tiers/{priceVolumeTierId}".format(client.base_url, priceVolumeTierId=price_volume_tier_id)

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
) -> Optional[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHpriceVolumeTierspriceVolumeTierIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    price_volume_tier_id: str,
    *,
    client: Client,
    json_body: PriceVolumeTierUpdate,
) -> Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    """Update a price volume tier

     Update a price volume tier

    Args:
        price_volume_tier_id (str):
        json_body (PriceVolumeTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]
    """

    kwargs = _get_kwargs(
        price_volume_tier_id=price_volume_tier_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    price_volume_tier_id: str,
    *,
    client: Client,
    json_body: PriceVolumeTierUpdate,
) -> Optional[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    """Update a price volume tier

     Update a price volume tier

    Args:
        price_volume_tier_id (str):
        json_body (PriceVolumeTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]
    """

    return sync_detailed(
        price_volume_tier_id=price_volume_tier_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    price_volume_tier_id: str,
    *,
    client: Client,
    json_body: PriceVolumeTierUpdate,
) -> Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    """Update a price volume tier

     Update a price volume tier

    Args:
        price_volume_tier_id (str):
        json_body (PriceVolumeTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]
    """

    kwargs = _get_kwargs(
        price_volume_tier_id=price_volume_tier_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    price_volume_tier_id: str,
    *,
    client: Client,
    json_body: PriceVolumeTierUpdate,
) -> Optional[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]:
    """Update a price volume tier

     Update a price volume tier

    Args:
        price_volume_tier_id (str):
        json_body (PriceVolumeTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpriceVolumeTierspriceVolumeTierIdResponse200]
    """

    return (
        await asyncio_detailed(
            price_volume_tier_id=price_volume_tier_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hshipping_weight_tiersshipping_weight_tier_id_response_200 import (
    PATCHshippingWeightTiersshippingWeightTierIdResponse200,
)
from ...models.shipping_weight_tier_update import ShippingWeightTierUpdate
from ...types import Response


def _get_kwargs(
    shipping_weight_tier_id: str,
    *,
    client: Client,
    json_body: ShippingWeightTierUpdate,
) -> Dict[str, Any]:
    url = "{}/shipping_weight_tiers/{shippingWeightTierId}".format(
        client.base_url, shippingWeightTierId=shipping_weight_tier_id
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
) -> Optional[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHshippingWeightTiersshippingWeightTierIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shipping_weight_tier_id: str,
    *,
    client: Client,
    json_body: ShippingWeightTierUpdate,
) -> Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    """Update a shipping weight tier

     Update a shipping weight tier

    Args:
        shipping_weight_tier_id (str):
        json_body (ShippingWeightTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]
    """

    kwargs = _get_kwargs(
        shipping_weight_tier_id=shipping_weight_tier_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    shipping_weight_tier_id: str,
    *,
    client: Client,
    json_body: ShippingWeightTierUpdate,
) -> Optional[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    """Update a shipping weight tier

     Update a shipping weight tier

    Args:
        shipping_weight_tier_id (str):
        json_body (ShippingWeightTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]
    """

    return sync_detailed(
        shipping_weight_tier_id=shipping_weight_tier_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    shipping_weight_tier_id: str,
    *,
    client: Client,
    json_body: ShippingWeightTierUpdate,
) -> Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    """Update a shipping weight tier

     Update a shipping weight tier

    Args:
        shipping_weight_tier_id (str):
        json_body (ShippingWeightTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]
    """

    kwargs = _get_kwargs(
        shipping_weight_tier_id=shipping_weight_tier_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shipping_weight_tier_id: str,
    *,
    client: Client,
    json_body: ShippingWeightTierUpdate,
) -> Optional[PATCHshippingWeightTiersshippingWeightTierIdResponse200]:
    """Update a shipping weight tier

     Update a shipping weight tier

    Args:
        shipping_weight_tier_id (str):
        json_body (ShippingWeightTierUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHshippingWeightTiersshippingWeightTierIdResponse200]
    """

    return (
        await asyncio_detailed(
            shipping_weight_tier_id=shipping_weight_tier_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

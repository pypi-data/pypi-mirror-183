from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.percentage_discount_promotion_create import PercentageDiscountPromotionCreate
from ...models.pos_tpercentage_discount_promotions_response_201 import POSTpercentageDiscountPromotionsResponse201
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: PercentageDiscountPromotionCreate,
) -> Dict[str, Any]:
    url = "{}/percentage_discount_promotions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[POSTpercentageDiscountPromotionsResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = POSTpercentageDiscountPromotionsResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[POSTpercentageDiscountPromotionsResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PercentageDiscountPromotionCreate,
) -> Response[POSTpercentageDiscountPromotionsResponse201]:
    """Create a percentage discount promotion

     Create a percentage discount promotion

    Args:
        json_body (PercentageDiscountPromotionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTpercentageDiscountPromotionsResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: PercentageDiscountPromotionCreate,
) -> Optional[POSTpercentageDiscountPromotionsResponse201]:
    """Create a percentage discount promotion

     Create a percentage discount promotion

    Args:
        json_body (PercentageDiscountPromotionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTpercentageDiscountPromotionsResponse201]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PercentageDiscountPromotionCreate,
) -> Response[POSTpercentageDiscountPromotionsResponse201]:
    """Create a percentage discount promotion

     Create a percentage discount promotion

    Args:
        json_body (PercentageDiscountPromotionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTpercentageDiscountPromotionsResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: PercentageDiscountPromotionCreate,
) -> Optional[POSTpercentageDiscountPromotionsResponse201]:
    """Create a percentage discount promotion

     Create a percentage discount promotion

    Args:
        json_body (PercentageDiscountPromotionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTpercentageDiscountPromotionsResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

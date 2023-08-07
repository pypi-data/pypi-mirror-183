from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hpercentage_discount_promotionspercentage_discount_promotion_id_response_200 import (
    PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200,
)
from ...models.percentage_discount_promotion_update import PercentageDiscountPromotionUpdate
from ...types import Response


def _get_kwargs(
    percentage_discount_promotion_id: str,
    *,
    client: Client,
    json_body: PercentageDiscountPromotionUpdate,
) -> Dict[str, Any]:
    url = "{}/percentage_discount_promotions/{percentageDiscountPromotionId}".format(
        client.base_url, percentageDiscountPromotionId=percentage_discount_promotion_id
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
) -> Optional[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200.from_dict(
            response.json()
        )

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    percentage_discount_promotion_id: str,
    *,
    client: Client,
    json_body: PercentageDiscountPromotionUpdate,
) -> Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    """Update a percentage discount promotion

     Update a percentage discount promotion

    Args:
        percentage_discount_promotion_id (str):
        json_body (PercentageDiscountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        percentage_discount_promotion_id=percentage_discount_promotion_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    percentage_discount_promotion_id: str,
    *,
    client: Client,
    json_body: PercentageDiscountPromotionUpdate,
) -> Optional[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    """Update a percentage discount promotion

     Update a percentage discount promotion

    Args:
        percentage_discount_promotion_id (str):
        json_body (PercentageDiscountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]
    """

    return sync_detailed(
        percentage_discount_promotion_id=percentage_discount_promotion_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    percentage_discount_promotion_id: str,
    *,
    client: Client,
    json_body: PercentageDiscountPromotionUpdate,
) -> Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    """Update a percentage discount promotion

     Update a percentage discount promotion

    Args:
        percentage_discount_promotion_id (str):
        json_body (PercentageDiscountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        percentage_discount_promotion_id=percentage_discount_promotion_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    percentage_discount_promotion_id: str,
    *,
    client: Client,
    json_body: PercentageDiscountPromotionUpdate,
) -> Optional[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]:
    """Update a percentage discount promotion

     Update a percentage discount promotion

    Args:
        percentage_discount_promotion_id (str):
        json_body (PercentageDiscountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200]
    """

    return (
        await asyncio_detailed(
            percentage_discount_promotion_id=percentage_discount_promotion_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

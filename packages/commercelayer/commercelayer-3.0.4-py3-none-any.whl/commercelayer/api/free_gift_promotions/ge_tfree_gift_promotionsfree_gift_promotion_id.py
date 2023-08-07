from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.ge_tfree_gift_promotionsfree_gift_promotion_id_response_200 import (
    GETfreeGiftPromotionsfreeGiftPromotionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    free_gift_promotion_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/free_gift_promotions/{freeGiftPromotionId}".format(
        client.base_url, freeGiftPromotionId=free_gift_promotion_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GETfreeGiftPromotionsfreeGiftPromotionIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    free_gift_promotion_id: str,
    *,
    client: Client,
) -> Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    """Retrieve a free gift promotion

     Retrieve a free gift promotion

    Args:
        free_gift_promotion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        free_gift_promotion_id=free_gift_promotion_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    free_gift_promotion_id: str,
    *,
    client: Client,
) -> Optional[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    """Retrieve a free gift promotion

     Retrieve a free gift promotion

    Args:
        free_gift_promotion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]
    """

    return sync_detailed(
        free_gift_promotion_id=free_gift_promotion_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    free_gift_promotion_id: str,
    *,
    client: Client,
) -> Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    """Retrieve a free gift promotion

     Retrieve a free gift promotion

    Args:
        free_gift_promotion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        free_gift_promotion_id=free_gift_promotion_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    free_gift_promotion_id: str,
    *,
    client: Client,
) -> Optional[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]:
    """Retrieve a free gift promotion

     Retrieve a free gift promotion

    Args:
        free_gift_promotion_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETfreeGiftPromotionsfreeGiftPromotionIdResponse200]
    """

    return (
        await asyncio_detailed(
            free_gift_promotion_id=free_gift_promotion_id,
            client=client,
        )
    ).parsed

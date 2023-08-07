from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.fixed_amount_promotion_update import FixedAmountPromotionUpdate
from ...models.patc_hfixed_amount_promotionsfixed_amount_promotion_id_response_200 import (
    PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    fixed_amount_promotion_id: str,
    *,
    client: Client,
    json_body: FixedAmountPromotionUpdate,
) -> Dict[str, Any]:
    url = "{}/fixed_amount_promotions/{fixedAmountPromotionId}".format(
        client.base_url, fixedAmountPromotionId=fixed_amount_promotion_id
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
) -> Optional[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fixed_amount_promotion_id: str,
    *,
    client: Client,
    json_body: FixedAmountPromotionUpdate,
) -> Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    """Update a fixed amount promotion

     Update a fixed amount promotion

    Args:
        fixed_amount_promotion_id (str):
        json_body (FixedAmountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        fixed_amount_promotion_id=fixed_amount_promotion_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fixed_amount_promotion_id: str,
    *,
    client: Client,
    json_body: FixedAmountPromotionUpdate,
) -> Optional[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    """Update a fixed amount promotion

     Update a fixed amount promotion

    Args:
        fixed_amount_promotion_id (str):
        json_body (FixedAmountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]
    """

    return sync_detailed(
        fixed_amount_promotion_id=fixed_amount_promotion_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    fixed_amount_promotion_id: str,
    *,
    client: Client,
    json_body: FixedAmountPromotionUpdate,
) -> Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    """Update a fixed amount promotion

     Update a fixed amount promotion

    Args:
        fixed_amount_promotion_id (str):
        json_body (FixedAmountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        fixed_amount_promotion_id=fixed_amount_promotion_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fixed_amount_promotion_id: str,
    *,
    client: Client,
    json_body: FixedAmountPromotionUpdate,
) -> Optional[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]:
    """Update a fixed amount promotion

     Update a fixed amount promotion

    Args:
        fixed_amount_promotion_id (str):
        json_body (FixedAmountPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHfixedAmountPromotionsfixedAmountPromotionIdResponse200]
    """

    return (
        await asyncio_detailed(
            fixed_amount_promotion_id=fixed_amount_promotion_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

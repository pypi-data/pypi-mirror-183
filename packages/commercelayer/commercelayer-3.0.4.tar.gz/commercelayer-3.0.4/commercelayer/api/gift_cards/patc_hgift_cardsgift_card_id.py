from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.gift_card_update import GiftCardUpdate
from ...models.patc_hgift_cardsgift_card_id_response_200 import PATCHgiftCardsgiftCardIdResponse200
from ...types import Response


def _get_kwargs(
    gift_card_id: str,
    *,
    client: Client,
    json_body: GiftCardUpdate,
) -> Dict[str, Any]:
    url = "{}/gift_cards/{giftCardId}".format(client.base_url, giftCardId=gift_card_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHgiftCardsgiftCardIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHgiftCardsgiftCardIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHgiftCardsgiftCardIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_card_id: str,
    *,
    client: Client,
    json_body: GiftCardUpdate,
) -> Response[PATCHgiftCardsgiftCardIdResponse200]:
    """Update a gift card

     Update a gift card

    Args:
        gift_card_id (str):
        json_body (GiftCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgiftCardsgiftCardIdResponse200]
    """

    kwargs = _get_kwargs(
        gift_card_id=gift_card_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_card_id: str,
    *,
    client: Client,
    json_body: GiftCardUpdate,
) -> Optional[PATCHgiftCardsgiftCardIdResponse200]:
    """Update a gift card

     Update a gift card

    Args:
        gift_card_id (str):
        json_body (GiftCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgiftCardsgiftCardIdResponse200]
    """

    return sync_detailed(
        gift_card_id=gift_card_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    gift_card_id: str,
    *,
    client: Client,
    json_body: GiftCardUpdate,
) -> Response[PATCHgiftCardsgiftCardIdResponse200]:
    """Update a gift card

     Update a gift card

    Args:
        gift_card_id (str):
        json_body (GiftCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgiftCardsgiftCardIdResponse200]
    """

    kwargs = _get_kwargs(
        gift_card_id=gift_card_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_card_id: str,
    *,
    client: Client,
    json_body: GiftCardUpdate,
) -> Optional[PATCHgiftCardsgiftCardIdResponse200]:
    """Update a gift card

     Update a gift card

    Args:
        gift_card_id (str):
        json_body (GiftCardUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgiftCardsgiftCardIdResponse200]
    """

    return (
        await asyncio_detailed(
            gift_card_id=gift_card_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

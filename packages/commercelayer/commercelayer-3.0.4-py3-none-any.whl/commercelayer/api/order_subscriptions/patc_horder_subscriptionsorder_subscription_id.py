from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.order_subscription_update import OrderSubscriptionUpdate
from ...models.patc_horder_subscriptionsorder_subscription_id_response_200 import (
    PATCHorderSubscriptionsorderSubscriptionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    order_subscription_id: str,
    *,
    client: Client,
    json_body: OrderSubscriptionUpdate,
) -> Dict[str, Any]:
    url = "{}/order_subscriptions/{orderSubscriptionId}".format(
        client.base_url, orderSubscriptionId=order_subscription_id
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
) -> Optional[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHorderSubscriptionsorderSubscriptionIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_subscription_id: str,
    *,
    client: Client,
    json_body: OrderSubscriptionUpdate,
) -> Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    """Update an order subscription

     Update an order subscription

    Args:
        order_subscription_id (str):
        json_body (OrderSubscriptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]
    """

    kwargs = _get_kwargs(
        order_subscription_id=order_subscription_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_subscription_id: str,
    *,
    client: Client,
    json_body: OrderSubscriptionUpdate,
) -> Optional[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    """Update an order subscription

     Update an order subscription

    Args:
        order_subscription_id (str):
        json_body (OrderSubscriptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]
    """

    return sync_detailed(
        order_subscription_id=order_subscription_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    order_subscription_id: str,
    *,
    client: Client,
    json_body: OrderSubscriptionUpdate,
) -> Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    """Update an order subscription

     Update an order subscription

    Args:
        order_subscription_id (str):
        json_body (OrderSubscriptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]
    """

    kwargs = _get_kwargs(
        order_subscription_id=order_subscription_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_subscription_id: str,
    *,
    client: Client,
    json_body: OrderSubscriptionUpdate,
) -> Optional[PATCHorderSubscriptionsorderSubscriptionIdResponse200]:
    """Update an order subscription

     Update an order subscription

    Args:
        order_subscription_id (str):
        json_body (OrderSubscriptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHorderSubscriptionsorderSubscriptionIdResponse200]
    """

    return (
        await asyncio_detailed(
            order_subscription_id=order_subscription_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

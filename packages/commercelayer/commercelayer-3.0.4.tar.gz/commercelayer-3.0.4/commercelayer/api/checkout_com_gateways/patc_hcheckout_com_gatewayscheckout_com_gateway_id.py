from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.checkout_com_gateway_update import CheckoutComGatewayUpdate
from ...models.patc_hcheckout_com_gatewayscheckout_com_gateway_id_response_200 import (
    PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200,
)
from ...types import Response


def _get_kwargs(
    checkout_com_gateway_id: str,
    *,
    client: Client,
    json_body: CheckoutComGatewayUpdate,
) -> Dict[str, Any]:
    url = "{}/checkout_com_gateways/{checkoutComGatewayId}".format(
        client.base_url, checkoutComGatewayId=checkout_com_gateway_id
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
) -> Optional[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    checkout_com_gateway_id: str,
    *,
    client: Client,
    json_body: CheckoutComGatewayUpdate,
) -> Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    """Update a checkout.com gateway

     Update a checkout.com gateway

    Args:
        checkout_com_gateway_id (str):
        json_body (CheckoutComGatewayUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]
    """

    kwargs = _get_kwargs(
        checkout_com_gateway_id=checkout_com_gateway_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    checkout_com_gateway_id: str,
    *,
    client: Client,
    json_body: CheckoutComGatewayUpdate,
) -> Optional[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    """Update a checkout.com gateway

     Update a checkout.com gateway

    Args:
        checkout_com_gateway_id (str):
        json_body (CheckoutComGatewayUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]
    """

    return sync_detailed(
        checkout_com_gateway_id=checkout_com_gateway_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    checkout_com_gateway_id: str,
    *,
    client: Client,
    json_body: CheckoutComGatewayUpdate,
) -> Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    """Update a checkout.com gateway

     Update a checkout.com gateway

    Args:
        checkout_com_gateway_id (str):
        json_body (CheckoutComGatewayUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]
    """

    kwargs = _get_kwargs(
        checkout_com_gateway_id=checkout_com_gateway_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    checkout_com_gateway_id: str,
    *,
    client: Client,
    json_body: CheckoutComGatewayUpdate,
) -> Optional[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]:
    """Update a checkout.com gateway

     Update a checkout.com gateway

    Args:
        checkout_com_gateway_id (str):
        json_body (CheckoutComGatewayUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComGatewayscheckoutComGatewayIdResponse200]
    """

    return (
        await asyncio_detailed(
            checkout_com_gateway_id=checkout_com_gateway_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

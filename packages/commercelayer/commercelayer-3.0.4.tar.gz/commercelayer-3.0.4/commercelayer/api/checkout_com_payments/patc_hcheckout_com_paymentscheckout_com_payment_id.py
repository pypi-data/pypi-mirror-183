from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.checkout_com_payment_update import CheckoutComPaymentUpdate
from ...models.patc_hcheckout_com_paymentscheckout_com_payment_id_response_200 import (
    PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200,
)
from ...types import Response


def _get_kwargs(
    checkout_com_payment_id: str,
    *,
    client: Client,
    json_body: CheckoutComPaymentUpdate,
) -> Dict[str, Any]:
    url = "{}/checkout_com_payments/{checkoutComPaymentId}".format(
        client.base_url, checkoutComPaymentId=checkout_com_payment_id
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
) -> Optional[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    checkout_com_payment_id: str,
    *,
    client: Client,
    json_body: CheckoutComPaymentUpdate,
) -> Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    """Update a checkout.com payment

     Update a checkout.com payment

    Args:
        checkout_com_payment_id (str):
        json_body (CheckoutComPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]
    """

    kwargs = _get_kwargs(
        checkout_com_payment_id=checkout_com_payment_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    checkout_com_payment_id: str,
    *,
    client: Client,
    json_body: CheckoutComPaymentUpdate,
) -> Optional[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    """Update a checkout.com payment

     Update a checkout.com payment

    Args:
        checkout_com_payment_id (str):
        json_body (CheckoutComPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]
    """

    return sync_detailed(
        checkout_com_payment_id=checkout_com_payment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    checkout_com_payment_id: str,
    *,
    client: Client,
    json_body: CheckoutComPaymentUpdate,
) -> Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    """Update a checkout.com payment

     Update a checkout.com payment

    Args:
        checkout_com_payment_id (str):
        json_body (CheckoutComPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]
    """

    kwargs = _get_kwargs(
        checkout_com_payment_id=checkout_com_payment_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    checkout_com_payment_id: str,
    *,
    client: Client,
    json_body: CheckoutComPaymentUpdate,
) -> Optional[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]:
    """Update a checkout.com payment

     Update a checkout.com payment

    Args:
        checkout_com_payment_id (str):
        json_body (CheckoutComPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcheckoutComPaymentscheckoutComPaymentIdResponse200]
    """

    return (
        await asyncio_detailed(
            checkout_com_payment_id=checkout_com_payment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

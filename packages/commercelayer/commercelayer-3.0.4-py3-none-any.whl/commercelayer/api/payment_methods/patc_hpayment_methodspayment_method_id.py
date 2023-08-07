from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hpayment_methodspayment_method_id_response_200 import PATCHpaymentMethodspaymentMethodIdResponse200
from ...models.payment_method_update import PaymentMethodUpdate
from ...types import Response


def _get_kwargs(
    payment_method_id: str,
    *,
    client: Client,
    json_body: PaymentMethodUpdate,
) -> Dict[str, Any]:
    url = "{}/payment_methods/{paymentMethodId}".format(client.base_url, paymentMethodId=payment_method_id)

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
) -> Optional[PATCHpaymentMethodspaymentMethodIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHpaymentMethodspaymentMethodIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHpaymentMethodspaymentMethodIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    payment_method_id: str,
    *,
    client: Client,
    json_body: PaymentMethodUpdate,
) -> Response[PATCHpaymentMethodspaymentMethodIdResponse200]:
    """Update a payment method

     Update a payment method

    Args:
        payment_method_id (str):
        json_body (PaymentMethodUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpaymentMethodspaymentMethodIdResponse200]
    """

    kwargs = _get_kwargs(
        payment_method_id=payment_method_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    payment_method_id: str,
    *,
    client: Client,
    json_body: PaymentMethodUpdate,
) -> Optional[PATCHpaymentMethodspaymentMethodIdResponse200]:
    """Update a payment method

     Update a payment method

    Args:
        payment_method_id (str):
        json_body (PaymentMethodUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpaymentMethodspaymentMethodIdResponse200]
    """

    return sync_detailed(
        payment_method_id=payment_method_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    payment_method_id: str,
    *,
    client: Client,
    json_body: PaymentMethodUpdate,
) -> Response[PATCHpaymentMethodspaymentMethodIdResponse200]:
    """Update a payment method

     Update a payment method

    Args:
        payment_method_id (str):
        json_body (PaymentMethodUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpaymentMethodspaymentMethodIdResponse200]
    """

    kwargs = _get_kwargs(
        payment_method_id=payment_method_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    payment_method_id: str,
    *,
    client: Client,
    json_body: PaymentMethodUpdate,
) -> Optional[PATCHpaymentMethodspaymentMethodIdResponse200]:
    """Update a payment method

     Update a payment method

    Args:
        payment_method_id (str):
        json_body (PaymentMethodUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpaymentMethodspaymentMethodIdResponse200]
    """

    return (
        await asyncio_detailed(
            payment_method_id=payment_method_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

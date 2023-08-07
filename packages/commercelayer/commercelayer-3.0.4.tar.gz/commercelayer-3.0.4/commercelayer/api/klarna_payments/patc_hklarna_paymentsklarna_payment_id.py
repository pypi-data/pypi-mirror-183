from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.klarna_payment_update import KlarnaPaymentUpdate
from ...models.patc_hklarna_paymentsklarna_payment_id_response_200 import PATCHklarnaPaymentsklarnaPaymentIdResponse200
from ...types import Response


def _get_kwargs(
    klarna_payment_id: str,
    *,
    client: Client,
    json_body: KlarnaPaymentUpdate,
) -> Dict[str, Any]:
    url = "{}/klarna_payments/{klarnaPaymentId}".format(client.base_url, klarnaPaymentId=klarna_payment_id)

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
) -> Optional[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHklarnaPaymentsklarnaPaymentIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    klarna_payment_id: str,
    *,
    client: Client,
    json_body: KlarnaPaymentUpdate,
) -> Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    """Update a klarna payment

     Update a klarna payment

    Args:
        klarna_payment_id (str):
        json_body (KlarnaPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]
    """

    kwargs = _get_kwargs(
        klarna_payment_id=klarna_payment_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    klarna_payment_id: str,
    *,
    client: Client,
    json_body: KlarnaPaymentUpdate,
) -> Optional[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    """Update a klarna payment

     Update a klarna payment

    Args:
        klarna_payment_id (str):
        json_body (KlarnaPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]
    """

    return sync_detailed(
        klarna_payment_id=klarna_payment_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    klarna_payment_id: str,
    *,
    client: Client,
    json_body: KlarnaPaymentUpdate,
) -> Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    """Update a klarna payment

     Update a klarna payment

    Args:
        klarna_payment_id (str):
        json_body (KlarnaPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]
    """

    kwargs = _get_kwargs(
        klarna_payment_id=klarna_payment_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    klarna_payment_id: str,
    *,
    client: Client,
    json_body: KlarnaPaymentUpdate,
) -> Optional[PATCHklarnaPaymentsklarnaPaymentIdResponse200]:
    """Update a klarna payment

     Update a klarna payment

    Args:
        klarna_payment_id (str):
        json_body (KlarnaPaymentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHklarnaPaymentsklarnaPaymentIdResponse200]
    """

    return (
        await asyncio_detailed(
            klarna_payment_id=klarna_payment_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

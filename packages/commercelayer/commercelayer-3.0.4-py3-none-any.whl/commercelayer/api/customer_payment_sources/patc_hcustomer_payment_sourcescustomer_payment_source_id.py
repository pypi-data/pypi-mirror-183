from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.customer_payment_source_update import CustomerPaymentSourceUpdate
from ...models.patc_hcustomer_payment_sourcescustomer_payment_source_id_response_200 import (
    PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200,
)
from ...types import Response


def _get_kwargs(
    customer_payment_source_id: str,
    *,
    client: Client,
    json_body: CustomerPaymentSourceUpdate,
) -> Dict[str, Any]:
    url = "{}/customer_payment_sources/{customerPaymentSourceId}".format(
        client.base_url, customerPaymentSourceId=customer_payment_source_id
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
) -> Optional[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_payment_source_id: str,
    *,
    client: Client,
    json_body: CustomerPaymentSourceUpdate,
) -> Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    """Update a customer payment source

     Update a customer payment source

    Args:
        customer_payment_source_id (str):
        json_body (CustomerPaymentSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_payment_source_id=customer_payment_source_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_payment_source_id: str,
    *,
    client: Client,
    json_body: CustomerPaymentSourceUpdate,
) -> Optional[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    """Update a customer payment source

     Update a customer payment source

    Args:
        customer_payment_source_id (str):
        json_body (CustomerPaymentSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]
    """

    return sync_detailed(
        customer_payment_source_id=customer_payment_source_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_payment_source_id: str,
    *,
    client: Client,
    json_body: CustomerPaymentSourceUpdate,
) -> Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    """Update a customer payment source

     Update a customer payment source

    Args:
        customer_payment_source_id (str):
        json_body (CustomerPaymentSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_payment_source_id=customer_payment_source_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_payment_source_id: str,
    *,
    client: Client,
    json_body: CustomerPaymentSourceUpdate,
) -> Optional[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]:
    """Update a customer payment source

     Update a customer payment source

    Args:
        customer_payment_source_id (str):
        json_body (CustomerPaymentSourceUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPaymentSourcescustomerPaymentSourceIdResponse200]
    """

    return (
        await asyncio_detailed(
            customer_payment_source_id=customer_payment_source_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.ge_tcustomer_addressescustomer_address_id_response_200 import (
    GETcustomerAddressescustomerAddressIdResponse200,
)
from ...types import Response


def _get_kwargs(
    customer_address_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/customer_addresses/{customerAddressId}".format(client.base_url, customerAddressId=customer_address_id)

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
) -> Optional[GETcustomerAddressescustomerAddressIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GETcustomerAddressescustomerAddressIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GETcustomerAddressescustomerAddressIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_address_id: str,
    *,
    client: Client,
) -> Response[GETcustomerAddressescustomerAddressIdResponse200]:
    """Retrieve a customer address

     Retrieve a customer address

    Args:
        customer_address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETcustomerAddressescustomerAddressIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_address_id=customer_address_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_address_id: str,
    *,
    client: Client,
) -> Optional[GETcustomerAddressescustomerAddressIdResponse200]:
    """Retrieve a customer address

     Retrieve a customer address

    Args:
        customer_address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETcustomerAddressescustomerAddressIdResponse200]
    """

    return sync_detailed(
        customer_address_id=customer_address_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_address_id: str,
    *,
    client: Client,
) -> Response[GETcustomerAddressescustomerAddressIdResponse200]:
    """Retrieve a customer address

     Retrieve a customer address

    Args:
        customer_address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETcustomerAddressescustomerAddressIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_address_id=customer_address_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_address_id: str,
    *,
    client: Client,
) -> Optional[GETcustomerAddressescustomerAddressIdResponse200]:
    """Retrieve a customer address

     Retrieve a customer address

    Args:
        customer_address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETcustomerAddressescustomerAddressIdResponse200]
    """

    return (
        await asyncio_detailed(
            customer_address_id=customer_address_id,
            client=client,
        )
    ).parsed

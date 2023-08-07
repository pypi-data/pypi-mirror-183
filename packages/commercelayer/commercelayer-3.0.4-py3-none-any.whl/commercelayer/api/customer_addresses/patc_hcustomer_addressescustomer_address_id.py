from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.customer_address_update import CustomerAddressUpdate
from ...models.patc_hcustomer_addressescustomer_address_id_response_200 import (
    PATCHcustomerAddressescustomerAddressIdResponse200,
)
from ...types import Response


def _get_kwargs(
    customer_address_id: str,
    *,
    client: Client,
    json_body: CustomerAddressUpdate,
) -> Dict[str, Any]:
    url = "{}/customer_addresses/{customerAddressId}".format(client.base_url, customerAddressId=customer_address_id)

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
) -> Optional[PATCHcustomerAddressescustomerAddressIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcustomerAddressescustomerAddressIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHcustomerAddressescustomerAddressIdResponse200]:
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
    json_body: CustomerAddressUpdate,
) -> Response[PATCHcustomerAddressescustomerAddressIdResponse200]:
    """Update a customer address

     Update a customer address

    Args:
        customer_address_id (str):
        json_body (CustomerAddressUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerAddressescustomerAddressIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_address_id=customer_address_id,
        client=client,
        json_body=json_body,
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
    json_body: CustomerAddressUpdate,
) -> Optional[PATCHcustomerAddressescustomerAddressIdResponse200]:
    """Update a customer address

     Update a customer address

    Args:
        customer_address_id (str):
        json_body (CustomerAddressUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerAddressescustomerAddressIdResponse200]
    """

    return sync_detailed(
        customer_address_id=customer_address_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_address_id: str,
    *,
    client: Client,
    json_body: CustomerAddressUpdate,
) -> Response[PATCHcustomerAddressescustomerAddressIdResponse200]:
    """Update a customer address

     Update a customer address

    Args:
        customer_address_id (str):
        json_body (CustomerAddressUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerAddressescustomerAddressIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_address_id=customer_address_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_address_id: str,
    *,
    client: Client,
    json_body: CustomerAddressUpdate,
) -> Optional[PATCHcustomerAddressescustomerAddressIdResponse200]:
    """Update a customer address

     Update a customer address

    Args:
        customer_address_id (str):
        json_body (CustomerAddressUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerAddressescustomerAddressIdResponse200]
    """

    return (
        await asyncio_detailed(
            customer_address_id=customer_address_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

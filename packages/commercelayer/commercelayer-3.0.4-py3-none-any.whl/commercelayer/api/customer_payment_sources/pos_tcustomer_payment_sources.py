from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.customer_payment_source_create import CustomerPaymentSourceCreate
from ...models.pos_tcustomer_payment_sources_response_201 import POSTcustomerPaymentSourcesResponse201
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CustomerPaymentSourceCreate,
) -> Dict[str, Any]:
    url = "{}/customer_payment_sources".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[POSTcustomerPaymentSourcesResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = POSTcustomerPaymentSourcesResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[POSTcustomerPaymentSourcesResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CustomerPaymentSourceCreate,
) -> Response[POSTcustomerPaymentSourcesResponse201]:
    """Create a customer payment source

     Create a customer payment source

    Args:
        json_body (CustomerPaymentSourceCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTcustomerPaymentSourcesResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CustomerPaymentSourceCreate,
) -> Optional[POSTcustomerPaymentSourcesResponse201]:
    """Create a customer payment source

     Create a customer payment source

    Args:
        json_body (CustomerPaymentSourceCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTcustomerPaymentSourcesResponse201]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CustomerPaymentSourceCreate,
) -> Response[POSTcustomerPaymentSourcesResponse201]:
    """Create a customer payment source

     Create a customer payment source

    Args:
        json_body (CustomerPaymentSourceCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTcustomerPaymentSourcesResponse201]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CustomerPaymentSourceCreate,
) -> Optional[POSTcustomerPaymentSourcesResponse201]:
    """Create a customer payment source

     Create a customer payment source

    Args:
        json_body (CustomerPaymentSourceCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTcustomerPaymentSourcesResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

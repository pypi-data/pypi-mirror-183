from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.pos_tstripe_gateways_response_201 import POSTstripeGatewaysResponse201
from ...models.stripe_gateway_create import StripeGatewayCreate
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: StripeGatewayCreate,
) -> Dict[str, Any]:
    url = "{}/stripe_gateways".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[POSTstripeGatewaysResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = POSTstripeGatewaysResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[POSTstripeGatewaysResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: StripeGatewayCreate,
) -> Response[POSTstripeGatewaysResponse201]:
    """Create a stripe gateway

     Create a stripe gateway

    Args:
        json_body (StripeGatewayCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTstripeGatewaysResponse201]
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
    json_body: StripeGatewayCreate,
) -> Optional[POSTstripeGatewaysResponse201]:
    """Create a stripe gateway

     Create a stripe gateway

    Args:
        json_body (StripeGatewayCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTstripeGatewaysResponse201]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: StripeGatewayCreate,
) -> Response[POSTstripeGatewaysResponse201]:
    """Create a stripe gateway

     Create a stripe gateway

    Args:
        json_body (StripeGatewayCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTstripeGatewaysResponse201]
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
    json_body: StripeGatewayCreate,
) -> Optional[POSTstripeGatewaysResponse201]:
    """Create a stripe gateway

     Create a stripe gateway

    Args:
        json_body (StripeGatewayCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[POSTstripeGatewaysResponse201]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed

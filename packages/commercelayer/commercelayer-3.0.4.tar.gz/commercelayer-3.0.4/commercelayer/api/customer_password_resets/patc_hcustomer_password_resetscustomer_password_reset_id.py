from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.customer_password_reset_update import CustomerPasswordResetUpdate
from ...models.patc_hcustomer_password_resetscustomer_password_reset_id_response_200 import (
    PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200,
)
from ...types import Response


def _get_kwargs(
    customer_password_reset_id: str,
    *,
    client: Client,
    json_body: CustomerPasswordResetUpdate,
) -> Dict[str, Any]:
    url = "{}/customer_password_resets/{customerPasswordResetId}".format(
        client.base_url, customerPasswordResetId=customer_password_reset_id
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
) -> Optional[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_password_reset_id: str,
    *,
    client: Client,
    json_body: CustomerPasswordResetUpdate,
) -> Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    """Update a customer password reset

     Update a customer password reset

    Args:
        customer_password_reset_id (str):
        json_body (CustomerPasswordResetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_password_reset_id=customer_password_reset_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_password_reset_id: str,
    *,
    client: Client,
    json_body: CustomerPasswordResetUpdate,
) -> Optional[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    """Update a customer password reset

     Update a customer password reset

    Args:
        customer_password_reset_id (str):
        json_body (CustomerPasswordResetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]
    """

    return sync_detailed(
        customer_password_reset_id=customer_password_reset_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    customer_password_reset_id: str,
    *,
    client: Client,
    json_body: CustomerPasswordResetUpdate,
) -> Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    """Update a customer password reset

     Update a customer password reset

    Args:
        customer_password_reset_id (str):
        json_body (CustomerPasswordResetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]
    """

    kwargs = _get_kwargs(
        customer_password_reset_id=customer_password_reset_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_password_reset_id: str,
    *,
    client: Client,
    json_body: CustomerPasswordResetUpdate,
) -> Optional[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]:
    """Update a customer password reset

     Update a customer password reset

    Args:
        customer_password_reset_id (str):
        json_body (CustomerPasswordResetUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcustomerPasswordResetscustomerPasswordResetIdResponse200]
    """

    return (
        await asyncio_detailed(
            customer_password_reset_id=customer_password_reset_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

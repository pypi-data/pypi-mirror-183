from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.ge_tmerchantsmerchant_id_response_200 import GETmerchantsmerchantIdResponse200
from ...types import Response


def _get_kwargs(
    merchant_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/merchants/{merchantId}".format(client.base_url, merchantId=merchant_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GETmerchantsmerchantIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GETmerchantsmerchantIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GETmerchantsmerchantIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    merchant_id: str,
    *,
    client: Client,
) -> Response[GETmerchantsmerchantIdResponse200]:
    """Retrieve a merchant

     Retrieve a merchant

    Args:
        merchant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmerchantsmerchantIdResponse200]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    merchant_id: str,
    *,
    client: Client,
) -> Optional[GETmerchantsmerchantIdResponse200]:
    """Retrieve a merchant

     Retrieve a merchant

    Args:
        merchant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmerchantsmerchantIdResponse200]
    """

    return sync_detailed(
        merchant_id=merchant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    merchant_id: str,
    *,
    client: Client,
) -> Response[GETmerchantsmerchantIdResponse200]:
    """Retrieve a merchant

     Retrieve a merchant

    Args:
        merchant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmerchantsmerchantIdResponse200]
    """

    kwargs = _get_kwargs(
        merchant_id=merchant_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    merchant_id: str,
    *,
    client: Client,
) -> Optional[GETmerchantsmerchantIdResponse200]:
    """Retrieve a merchant

     Retrieve a merchant

    Args:
        merchant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmerchantsmerchantIdResponse200]
    """

    return (
        await asyncio_detailed(
            merchant_id=merchant_id,
            client=client,
        )
    ).parsed

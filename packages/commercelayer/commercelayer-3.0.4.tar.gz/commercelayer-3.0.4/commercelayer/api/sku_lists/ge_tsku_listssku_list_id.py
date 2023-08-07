from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.ge_tsku_listssku_list_id_response_200 import GETskuListsskuListIdResponse200
from ...types import Response


def _get_kwargs(
    sku_list_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sku_lists/{skuListId}".format(client.base_url, skuListId=sku_list_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[GETskuListsskuListIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GETskuListsskuListIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[GETskuListsskuListIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sku_list_id: str,
    *,
    client: Client,
) -> Response[GETskuListsskuListIdResponse200]:
    """Retrieve a SKU list

     Retrieve a SKU list

    Args:
        sku_list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETskuListsskuListIdResponse200]
    """

    kwargs = _get_kwargs(
        sku_list_id=sku_list_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sku_list_id: str,
    *,
    client: Client,
) -> Optional[GETskuListsskuListIdResponse200]:
    """Retrieve a SKU list

     Retrieve a SKU list

    Args:
        sku_list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETskuListsskuListIdResponse200]
    """

    return sync_detailed(
        sku_list_id=sku_list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sku_list_id: str,
    *,
    client: Client,
) -> Response[GETskuListsskuListIdResponse200]:
    """Retrieve a SKU list

     Retrieve a SKU list

    Args:
        sku_list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETskuListsskuListIdResponse200]
    """

    kwargs = _get_kwargs(
        sku_list_id=sku_list_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sku_list_id: str,
    *,
    client: Client,
) -> Optional[GETskuListsskuListIdResponse200]:
    """Retrieve a SKU list

     Retrieve a SKU list

    Args:
        sku_list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETskuListsskuListIdResponse200]
    """

    return (
        await asyncio_detailed(
            sku_list_id=sku_list_id,
            client=client,
        )
    ).parsed

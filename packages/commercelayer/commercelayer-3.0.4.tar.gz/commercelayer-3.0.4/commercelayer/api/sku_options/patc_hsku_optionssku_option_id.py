from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hsku_optionssku_option_id_response_200 import PATCHskuOptionsskuOptionIdResponse200
from ...models.sku_option_update import SkuOptionUpdate
from ...types import Response


def _get_kwargs(
    sku_option_id: str,
    *,
    client: Client,
    json_body: SkuOptionUpdate,
) -> Dict[str, Any]:
    url = "{}/sku_options/{skuOptionId}".format(client.base_url, skuOptionId=sku_option_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHskuOptionsskuOptionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHskuOptionsskuOptionIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHskuOptionsskuOptionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sku_option_id: str,
    *,
    client: Client,
    json_body: SkuOptionUpdate,
) -> Response[PATCHskuOptionsskuOptionIdResponse200]:
    """Update a SKU option

     Update a SKU option

    Args:
        sku_option_id (str):
        json_body (SkuOptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHskuOptionsskuOptionIdResponse200]
    """

    kwargs = _get_kwargs(
        sku_option_id=sku_option_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sku_option_id: str,
    *,
    client: Client,
    json_body: SkuOptionUpdate,
) -> Optional[PATCHskuOptionsskuOptionIdResponse200]:
    """Update a SKU option

     Update a SKU option

    Args:
        sku_option_id (str):
        json_body (SkuOptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHskuOptionsskuOptionIdResponse200]
    """

    return sync_detailed(
        sku_option_id=sku_option_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    sku_option_id: str,
    *,
    client: Client,
    json_body: SkuOptionUpdate,
) -> Response[PATCHskuOptionsskuOptionIdResponse200]:
    """Update a SKU option

     Update a SKU option

    Args:
        sku_option_id (str):
        json_body (SkuOptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHskuOptionsskuOptionIdResponse200]
    """

    kwargs = _get_kwargs(
        sku_option_id=sku_option_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sku_option_id: str,
    *,
    client: Client,
    json_body: SkuOptionUpdate,
) -> Optional[PATCHskuOptionsskuOptionIdResponse200]:
    """Update a SKU option

     Update a SKU option

    Args:
        sku_option_id (str):
        json_body (SkuOptionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHskuOptionsskuOptionIdResponse200]
    """

    return (
        await asyncio_detailed(
            sku_option_id=sku_option_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

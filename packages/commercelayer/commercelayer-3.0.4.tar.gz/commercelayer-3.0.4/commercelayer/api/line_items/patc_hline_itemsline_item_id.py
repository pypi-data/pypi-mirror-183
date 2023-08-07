from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.line_item_update import LineItemUpdate
from ...models.patc_hline_itemsline_item_id_response_200 import PATCHlineItemslineItemIdResponse200
from ...types import Response


def _get_kwargs(
    line_item_id: str,
    *,
    client: Client,
    json_body: LineItemUpdate,
) -> Dict[str, Any]:
    url = "{}/line_items/{lineItemId}".format(client.base_url, lineItemId=line_item_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHlineItemslineItemIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHlineItemslineItemIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHlineItemslineItemIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    line_item_id: str,
    *,
    client: Client,
    json_body: LineItemUpdate,
) -> Response[PATCHlineItemslineItemIdResponse200]:
    """Update a line item

     Update a line item

    Args:
        line_item_id (str):
        json_body (LineItemUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHlineItemslineItemIdResponse200]
    """

    kwargs = _get_kwargs(
        line_item_id=line_item_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    line_item_id: str,
    *,
    client: Client,
    json_body: LineItemUpdate,
) -> Optional[PATCHlineItemslineItemIdResponse200]:
    """Update a line item

     Update a line item

    Args:
        line_item_id (str):
        json_body (LineItemUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHlineItemslineItemIdResponse200]
    """

    return sync_detailed(
        line_item_id=line_item_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    line_item_id: str,
    *,
    client: Client,
    json_body: LineItemUpdate,
) -> Response[PATCHlineItemslineItemIdResponse200]:
    """Update a line item

     Update a line item

    Args:
        line_item_id (str):
        json_body (LineItemUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHlineItemslineItemIdResponse200]
    """

    kwargs = _get_kwargs(
        line_item_id=line_item_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    line_item_id: str,
    *,
    client: Client,
    json_body: LineItemUpdate,
) -> Optional[PATCHlineItemslineItemIdResponse200]:
    """Update a line item

     Update a line item

    Args:
        line_item_id (str):
        json_body (LineItemUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHlineItemslineItemIdResponse200]
    """

    return (
        await asyncio_detailed(
            line_item_id=line_item_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

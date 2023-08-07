from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_htax_categoriestax_category_id_response_200 import PATCHtaxCategoriestaxCategoryIdResponse200
from ...models.tax_category_update import TaxCategoryUpdate
from ...types import Response


def _get_kwargs(
    tax_category_id: str,
    *,
    client: Client,
    json_body: TaxCategoryUpdate,
) -> Dict[str, Any]:
    url = "{}/tax_categories/{taxCategoryId}".format(client.base_url, taxCategoryId=tax_category_id)

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
) -> Optional[PATCHtaxCategoriestaxCategoryIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHtaxCategoriestaxCategoryIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHtaxCategoriestaxCategoryIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tax_category_id: str,
    *,
    client: Client,
    json_body: TaxCategoryUpdate,
) -> Response[PATCHtaxCategoriestaxCategoryIdResponse200]:
    """Update a tax category

     Update a tax category

    Args:
        tax_category_id (str):
        json_body (TaxCategoryUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHtaxCategoriestaxCategoryIdResponse200]
    """

    kwargs = _get_kwargs(
        tax_category_id=tax_category_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tax_category_id: str,
    *,
    client: Client,
    json_body: TaxCategoryUpdate,
) -> Optional[PATCHtaxCategoriestaxCategoryIdResponse200]:
    """Update a tax category

     Update a tax category

    Args:
        tax_category_id (str):
        json_body (TaxCategoryUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHtaxCategoriestaxCategoryIdResponse200]
    """

    return sync_detailed(
        tax_category_id=tax_category_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    tax_category_id: str,
    *,
    client: Client,
    json_body: TaxCategoryUpdate,
) -> Response[PATCHtaxCategoriestaxCategoryIdResponse200]:
    """Update a tax category

     Update a tax category

    Args:
        tax_category_id (str):
        json_body (TaxCategoryUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHtaxCategoriestaxCategoryIdResponse200]
    """

    kwargs = _get_kwargs(
        tax_category_id=tax_category_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tax_category_id: str,
    *,
    client: Client,
    json_body: TaxCategoryUpdate,
) -> Optional[PATCHtaxCategoriestaxCategoryIdResponse200]:
    """Update a tax category

     Update a tax category

    Args:
        tax_category_id (str):
        json_body (TaxCategoryUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHtaxCategoriestaxCategoryIdResponse200]
    """

    return (
        await asyncio_detailed(
            tax_category_id=tax_category_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

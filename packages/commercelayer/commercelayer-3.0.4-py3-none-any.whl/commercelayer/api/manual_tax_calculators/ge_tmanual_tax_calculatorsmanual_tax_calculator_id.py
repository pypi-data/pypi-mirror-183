from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.ge_tmanual_tax_calculatorsmanual_tax_calculator_id_response_200 import (
    GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200,
)
from ...types import Response


def _get_kwargs(
    manual_tax_calculator_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/manual_tax_calculators/{manualTaxCalculatorId}".format(
        client.base_url, manualTaxCalculatorId=manual_tax_calculator_id
    )

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
) -> Optional[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    manual_tax_calculator_id: str,
    *,
    client: Client,
) -> Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Retrieve a manual tax calculator

     Retrieve a manual tax calculator

    Args:
        manual_tax_calculator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    kwargs = _get_kwargs(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    manual_tax_calculator_id: str,
    *,
    client: Client,
) -> Optional[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Retrieve a manual tax calculator

     Retrieve a manual tax calculator

    Args:
        manual_tax_calculator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    return sync_detailed(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    manual_tax_calculator_id: str,
    *,
    client: Client,
) -> Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Retrieve a manual tax calculator

     Retrieve a manual tax calculator

    Args:
        manual_tax_calculator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    kwargs = _get_kwargs(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    manual_tax_calculator_id: str,
    *,
    client: Client,
) -> Optional[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Retrieve a manual tax calculator

     Retrieve a manual tax calculator

    Args:
        manual_tax_calculator_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GETmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    return (
        await asyncio_detailed(
            manual_tax_calculator_id=manual_tax_calculator_id,
            client=client,
        )
    ).parsed

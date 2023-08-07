from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.manual_tax_calculator_update import ManualTaxCalculatorUpdate
from ...models.patc_hmanual_tax_calculatorsmanual_tax_calculator_id_response_200 import (
    PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200,
)
from ...types import Response


def _get_kwargs(
    manual_tax_calculator_id: str,
    *,
    client: Client,
    json_body: ManualTaxCalculatorUpdate,
) -> Dict[str, Any]:
    url = "{}/manual_tax_calculators/{manualTaxCalculatorId}".format(
        client.base_url, manualTaxCalculatorId=manual_tax_calculator_id
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
) -> Optional[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
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
    json_body: ManualTaxCalculatorUpdate,
) -> Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Update a manual tax calculator

     Update a manual tax calculator

    Args:
        manual_tax_calculator_id (str):
        json_body (ManualTaxCalculatorUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    kwargs = _get_kwargs(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
        json_body=json_body,
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
    json_body: ManualTaxCalculatorUpdate,
) -> Optional[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Update a manual tax calculator

     Update a manual tax calculator

    Args:
        manual_tax_calculator_id (str):
        json_body (ManualTaxCalculatorUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    return sync_detailed(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    manual_tax_calculator_id: str,
    *,
    client: Client,
    json_body: ManualTaxCalculatorUpdate,
) -> Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Update a manual tax calculator

     Update a manual tax calculator

    Args:
        manual_tax_calculator_id (str):
        json_body (ManualTaxCalculatorUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    kwargs = _get_kwargs(
        manual_tax_calculator_id=manual_tax_calculator_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    manual_tax_calculator_id: str,
    *,
    client: Client,
    json_body: ManualTaxCalculatorUpdate,
) -> Optional[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]:
    """Update a manual tax calculator

     Update a manual tax calculator

    Args:
        manual_tax_calculator_id (str):
        json_body (ManualTaxCalculatorUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHmanualTaxCalculatorsmanualTaxCalculatorIdResponse200]
    """

    return (
        await asyncio_detailed(
            manual_tax_calculator_id=manual_tax_calculator_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.bing_geocoder_update import BingGeocoderUpdate
from ...models.patc_hbing_geocodersbing_geocoder_id_response_200 import PATCHbingGeocodersbingGeocoderIdResponse200
from ...types import Response


def _get_kwargs(
    bing_geocoder_id: str,
    *,
    client: Client,
    json_body: BingGeocoderUpdate,
) -> Dict[str, Any]:
    url = "{}/bing_geocoders/{bingGeocoderId}".format(client.base_url, bingGeocoderId=bing_geocoder_id)

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
) -> Optional[PATCHbingGeocodersbingGeocoderIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHbingGeocodersbingGeocoderIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHbingGeocodersbingGeocoderIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bing_geocoder_id: str,
    *,
    client: Client,
    json_body: BingGeocoderUpdate,
) -> Response[PATCHbingGeocodersbingGeocoderIdResponse200]:
    """Update a bing geocoder

     Update a bing geocoder

    Args:
        bing_geocoder_id (str):
        json_body (BingGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbingGeocodersbingGeocoderIdResponse200]
    """

    kwargs = _get_kwargs(
        bing_geocoder_id=bing_geocoder_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bing_geocoder_id: str,
    *,
    client: Client,
    json_body: BingGeocoderUpdate,
) -> Optional[PATCHbingGeocodersbingGeocoderIdResponse200]:
    """Update a bing geocoder

     Update a bing geocoder

    Args:
        bing_geocoder_id (str):
        json_body (BingGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbingGeocodersbingGeocoderIdResponse200]
    """

    return sync_detailed(
        bing_geocoder_id=bing_geocoder_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    bing_geocoder_id: str,
    *,
    client: Client,
    json_body: BingGeocoderUpdate,
) -> Response[PATCHbingGeocodersbingGeocoderIdResponse200]:
    """Update a bing geocoder

     Update a bing geocoder

    Args:
        bing_geocoder_id (str):
        json_body (BingGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbingGeocodersbingGeocoderIdResponse200]
    """

    kwargs = _get_kwargs(
        bing_geocoder_id=bing_geocoder_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bing_geocoder_id: str,
    *,
    client: Client,
    json_body: BingGeocoderUpdate,
) -> Optional[PATCHbingGeocodersbingGeocoderIdResponse200]:
    """Update a bing geocoder

     Update a bing geocoder

    Args:
        bing_geocoder_id (str):
        json_body (BingGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbingGeocodersbingGeocoderIdResponse200]
    """

    return (
        await asyncio_detailed(
            bing_geocoder_id=bing_geocoder_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

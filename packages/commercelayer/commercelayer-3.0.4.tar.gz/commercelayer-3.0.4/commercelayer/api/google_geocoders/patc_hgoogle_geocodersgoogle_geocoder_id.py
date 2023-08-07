from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.google_geocoder_update import GoogleGeocoderUpdate
from ...models.patc_hgoogle_geocodersgoogle_geocoder_id_response_200 import (
    PATCHgoogleGeocodersgoogleGeocoderIdResponse200,
)
from ...types import Response


def _get_kwargs(
    google_geocoder_id: str,
    *,
    client: Client,
    json_body: GoogleGeocoderUpdate,
) -> Dict[str, Any]:
    url = "{}/google_geocoders/{googleGeocoderId}".format(client.base_url, googleGeocoderId=google_geocoder_id)

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
) -> Optional[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHgoogleGeocodersgoogleGeocoderIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    google_geocoder_id: str,
    *,
    client: Client,
    json_body: GoogleGeocoderUpdate,
) -> Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    """Update a google geocoder

     Update a google geocoder

    Args:
        google_geocoder_id (str):
        json_body (GoogleGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]
    """

    kwargs = _get_kwargs(
        google_geocoder_id=google_geocoder_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    google_geocoder_id: str,
    *,
    client: Client,
    json_body: GoogleGeocoderUpdate,
) -> Optional[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    """Update a google geocoder

     Update a google geocoder

    Args:
        google_geocoder_id (str):
        json_body (GoogleGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]
    """

    return sync_detailed(
        google_geocoder_id=google_geocoder_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    google_geocoder_id: str,
    *,
    client: Client,
    json_body: GoogleGeocoderUpdate,
) -> Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    """Update a google geocoder

     Update a google geocoder

    Args:
        google_geocoder_id (str):
        json_body (GoogleGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]
    """

    kwargs = _get_kwargs(
        google_geocoder_id=google_geocoder_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    google_geocoder_id: str,
    *,
    client: Client,
    json_body: GoogleGeocoderUpdate,
) -> Optional[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]:
    """Update a google geocoder

     Update a google geocoder

    Args:
        google_geocoder_id (str):
        json_body (GoogleGeocoderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHgoogleGeocodersgoogleGeocoderIdResponse200]
    """

    return (
        await asyncio_detailed(
            google_geocoder_id=google_geocoder_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

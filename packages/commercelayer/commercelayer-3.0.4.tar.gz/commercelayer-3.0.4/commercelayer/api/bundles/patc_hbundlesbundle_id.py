from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.bundle_update import BundleUpdate
from ...models.patc_hbundlesbundle_id_response_200 import PATCHbundlesbundleIdResponse200
from ...types import Response


def _get_kwargs(
    bundle_id: str,
    *,
    client: Client,
    json_body: BundleUpdate,
) -> Dict[str, Any]:
    url = "{}/bundles/{bundleId}".format(client.base_url, bundleId=bundle_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHbundlesbundleIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHbundlesbundleIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHbundlesbundleIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bundle_id: str,
    *,
    client: Client,
    json_body: BundleUpdate,
) -> Response[PATCHbundlesbundleIdResponse200]:
    """Update a bundle

     Update a bundle

    Args:
        bundle_id (str):
        json_body (BundleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbundlesbundleIdResponse200]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bundle_id: str,
    *,
    client: Client,
    json_body: BundleUpdate,
) -> Optional[PATCHbundlesbundleIdResponse200]:
    """Update a bundle

     Update a bundle

    Args:
        bundle_id (str):
        json_body (BundleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbundlesbundleIdResponse200]
    """

    return sync_detailed(
        bundle_id=bundle_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    bundle_id: str,
    *,
    client: Client,
    json_body: BundleUpdate,
) -> Response[PATCHbundlesbundleIdResponse200]:
    """Update a bundle

     Update a bundle

    Args:
        bundle_id (str):
        json_body (BundleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbundlesbundleIdResponse200]
    """

    kwargs = _get_kwargs(
        bundle_id=bundle_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bundle_id: str,
    *,
    client: Client,
    json_body: BundleUpdate,
) -> Optional[PATCHbundlesbundleIdResponse200]:
    """Update a bundle

     Update a bundle

    Args:
        bundle_id (str):
        json_body (BundleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHbundlesbundleIdResponse200]
    """

    return (
        await asyncio_detailed(
            bundle_id=bundle_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

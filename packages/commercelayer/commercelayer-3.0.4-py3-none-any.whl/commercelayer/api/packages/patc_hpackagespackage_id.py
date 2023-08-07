from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.package_update import PackageUpdate
from ...models.patc_hpackagespackage_id_response_200 import PATCHpackagespackageIdResponse200
from ...types import Response


def _get_kwargs(
    package_id: str,
    *,
    client: Client,
    json_body: PackageUpdate,
) -> Dict[str, Any]:
    url = "{}/packages/{packageId}".format(client.base_url, packageId=package_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHpackagespackageIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHpackagespackageIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHpackagespackageIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    package_id: str,
    *,
    client: Client,
    json_body: PackageUpdate,
) -> Response[PATCHpackagespackageIdResponse200]:
    """Update a package

     Update a package

    Args:
        package_id (str):
        json_body (PackageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpackagespackageIdResponse200]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    package_id: str,
    *,
    client: Client,
    json_body: PackageUpdate,
) -> Optional[PATCHpackagespackageIdResponse200]:
    """Update a package

     Update a package

    Args:
        package_id (str):
        json_body (PackageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpackagespackageIdResponse200]
    """

    return sync_detailed(
        package_id=package_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    package_id: str,
    *,
    client: Client,
    json_body: PackageUpdate,
) -> Response[PATCHpackagespackageIdResponse200]:
    """Update a package

     Update a package

    Args:
        package_id (str):
        json_body (PackageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpackagespackageIdResponse200]
    """

    kwargs = _get_kwargs(
        package_id=package_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    package_id: str,
    *,
    client: Client,
    json_body: PackageUpdate,
) -> Optional[PATCHpackagespackageIdResponse200]:
    """Update a package

     Update a package

    Args:
        package_id (str):
        json_body (PackageUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHpackagespackageIdResponse200]
    """

    return (
        await asyncio_detailed(
            package_id=package_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

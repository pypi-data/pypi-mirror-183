from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.capture_update import CaptureUpdate
from ...models.patc_hcapturescapture_id_response_200 import PATCHcapturescaptureIdResponse200
from ...types import Response


def _get_kwargs(
    capture_id: str,
    *,
    client: Client,
    json_body: CaptureUpdate,
) -> Dict[str, Any]:
    url = "{}/captures/{captureId}".format(client.base_url, captureId=capture_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHcapturescaptureIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHcapturescaptureIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHcapturescaptureIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    capture_id: str,
    *,
    client: Client,
    json_body: CaptureUpdate,
) -> Response[PATCHcapturescaptureIdResponse200]:
    """Update a capture

     Update a capture

    Args:
        capture_id (str):
        json_body (CaptureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcapturescaptureIdResponse200]
    """

    kwargs = _get_kwargs(
        capture_id=capture_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    capture_id: str,
    *,
    client: Client,
    json_body: CaptureUpdate,
) -> Optional[PATCHcapturescaptureIdResponse200]:
    """Update a capture

     Update a capture

    Args:
        capture_id (str):
        json_body (CaptureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcapturescaptureIdResponse200]
    """

    return sync_detailed(
        capture_id=capture_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    capture_id: str,
    *,
    client: Client,
    json_body: CaptureUpdate,
) -> Response[PATCHcapturescaptureIdResponse200]:
    """Update a capture

     Update a capture

    Args:
        capture_id (str):
        json_body (CaptureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcapturescaptureIdResponse200]
    """

    kwargs = _get_kwargs(
        capture_id=capture_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    capture_id: str,
    *,
    client: Client,
    json_body: CaptureUpdate,
) -> Optional[PATCHcapturescaptureIdResponse200]:
    """Update a capture

     Update a capture

    Args:
        capture_id (str):
        json_body (CaptureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHcapturescaptureIdResponse200]
    """

    return (
        await asyncio_detailed(
            capture_id=capture_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

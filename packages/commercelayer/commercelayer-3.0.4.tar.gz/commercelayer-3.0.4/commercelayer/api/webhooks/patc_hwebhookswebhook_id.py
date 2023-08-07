from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.patc_hwebhookswebhook_id_response_200 import PATCHwebhookswebhookIdResponse200
from ...models.webhook_update import WebhookUpdate
from ...types import Response


def _get_kwargs(
    webhook_id: str,
    *,
    client: Client,
    json_body: WebhookUpdate,
) -> Dict[str, Any]:
    url = "{}/webhooks/{webhookId}".format(client.base_url, webhookId=webhook_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PATCHwebhookswebhookIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHwebhookswebhookIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PATCHwebhookswebhookIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: str,
    *,
    client: Client,
    json_body: WebhookUpdate,
) -> Response[PATCHwebhookswebhookIdResponse200]:
    """Update a webhook

     Update a webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwebhookswebhookIdResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: str,
    *,
    client: Client,
    json_body: WebhookUpdate,
) -> Optional[PATCHwebhookswebhookIdResponse200]:
    """Update a webhook

     Update a webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwebhookswebhookIdResponse200]
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    webhook_id: str,
    *,
    client: Client,
    json_body: WebhookUpdate,
) -> Response[PATCHwebhookswebhookIdResponse200]:
    """Update a webhook

     Update a webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwebhookswebhookIdResponse200]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: str,
    *,
    client: Client,
    json_body: WebhookUpdate,
) -> Optional[PATCHwebhookswebhookIdResponse200]:
    """Update a webhook

     Update a webhook

    Args:
        webhook_id (str):
        json_body (WebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHwebhookswebhookIdResponse200]
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.external_promotion_update import ExternalPromotionUpdate
from ...models.patc_hexternal_promotionsexternal_promotion_id_response_200 import (
    PATCHexternalPromotionsexternalPromotionIdResponse200,
)
from ...types import Response


def _get_kwargs(
    external_promotion_id: str,
    *,
    client: Client,
    json_body: ExternalPromotionUpdate,
) -> Dict[str, Any]:
    url = "{}/external_promotions/{externalPromotionId}".format(
        client.base_url, externalPromotionId=external_promotion_id
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
) -> Optional[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PATCHexternalPromotionsexternalPromotionIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_promotion_id: str,
    *,
    client: Client,
    json_body: ExternalPromotionUpdate,
) -> Response[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    """Update an external promotion

     Update an external promotion

    Args:
        external_promotion_id (str):
        json_body (ExternalPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHexternalPromotionsexternalPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        external_promotion_id=external_promotion_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_promotion_id: str,
    *,
    client: Client,
    json_body: ExternalPromotionUpdate,
) -> Optional[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    """Update an external promotion

     Update an external promotion

    Args:
        external_promotion_id (str):
        json_body (ExternalPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHexternalPromotionsexternalPromotionIdResponse200]
    """

    return sync_detailed(
        external_promotion_id=external_promotion_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    external_promotion_id: str,
    *,
    client: Client,
    json_body: ExternalPromotionUpdate,
) -> Response[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    """Update an external promotion

     Update an external promotion

    Args:
        external_promotion_id (str):
        json_body (ExternalPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHexternalPromotionsexternalPromotionIdResponse200]
    """

    kwargs = _get_kwargs(
        external_promotion_id=external_promotion_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_promotion_id: str,
    *,
    client: Client,
    json_body: ExternalPromotionUpdate,
) -> Optional[PATCHexternalPromotionsexternalPromotionIdResponse200]:
    """Update an external promotion

     Update an external promotion

    Args:
        external_promotion_id (str):
        json_body (ExternalPromotionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PATCHexternalPromotionsexternalPromotionIdResponse200]
    """

    return (
        await asyncio_detailed(
            external_promotion_id=external_promotion_id,
            client=client,
            json_body=json_body,
        )
    ).parsed

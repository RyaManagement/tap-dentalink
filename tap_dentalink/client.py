"""REST client handling, including DentalinkStream base class."""

from __future__ import annotations

import decimal
import typing as t
from importlib import resources
from urllib.parse import parse_qsl

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.pagination import BaseAPIPaginator  # noqa: TC002
from singer_sdk.streams import RESTStream

import re

if t.TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = resources.files(__package__) / "schemas"

class DentalinkStream(RESTStream):
    """Dentalink stream class."""

    # Update this value if necessary or override `parse_response`.
    records_jsonpath = "$.data[*]"

    # Update this value if necessary or override `get_new_paginator`.
    next_page_token_jsonpath = "$.links.next"  # noqa: S105

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        # TODO: hardcode a value here, or retrieve it from self.config
        return self.config.get("api_url")

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")  # noqa: ERA001
        headers = {
            "Authorization": f'Token {self.config.get("auth_token")}',
            "Content-Type": "application/json"
        }
        return headers


    def get_url_params(
        self,
        context: Context | None,  # noqa: ARG002
        next_page_token: t.Any | None,  # noqa: ANN401
    ) -> dict[str, t.Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        pattern = re.compile("cursor=(.*)$")
        if next_page_token:
            cursor = pattern.search(next_page_token).groups()[0]
            params["cursor"] = cursor
        else:
            params.update(self.get_query_params(context))
        return params

    def get_query_params(self, context):
        return {}

    def parse_response(self, response: requests.Response) -> t.Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(
            self.records_jsonpath,
            input=response.json(parse_float=decimal.Decimal),
        )

    def backoff_max_tries(self) -> int:  # noqa: PLR6301
        """The number of attempts before giving up when retrying requests.

        Returns:
            Number of max retries.
        """
        return self.config.get("backoff_retries")

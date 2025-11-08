"""Dentalink tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_dentalink import streams

from datetime import date


class TapDentalink(Tap):
    """Dentalink tap class."""

    name = "tap-dentalink"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType(nullable=False),
            required=True,
            secret=True,  # Flag config as protected.
            title="Auth Token",
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_url",
            th.StringType(nullable=False),
            title="API URL",
            default="https://api.dentalink.healthatom.com/api",
            description="The url for the API service",
        ),
        th.Property(
            "backoff_retries",
            th.IntegerType(),
            title="Backoff retries",
            default=10,
            description="The number of backoff retries",
        ),
        th.Property(
            "start_date",
            th.DateType(),
            required=True,
            title="Start Date",
            description="Initial date to start extracting data from",
        ),
        th.Property(
            "end_date",
            th.DateType(),
            title="End Date",
            default=None,
            description="End date for records to extract",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.DentalinkStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.CitasStream(self),
            streams.EstadoCitasStream(self),
            streams.MediosDePagoStream(self),
            streams.MotivoAtencionStream(self),
            streams.PacientesStream(self),
            streams.PagosStream(self),
            streams.PrestacionesStream(self),
            streams.SillonesStream(self),
            streams.TratamientosStream(self),
            streams.TratamientosDetallesStream(self),
            streams.ProduccionStream(self),
            streams.PagosEliminadosStream(self),
            streams.ArancelesStream(self),
            streams.BancosStream(self),
            streams.CajasStream(self),
            streams.CategoriasStream(self),
            streams.ConveniosStream(self),
            streams.EspecialidadesStream(self),
            streams.LiquidacionesStream(self),
            streams.LiquidacionesDetallesStream(self),
            streams.TareasStream(self),
            ##streams.AgendasStream(self),
            ##streams.EncuestasStream(self),
        ]


if __name__ == "__main__":
    TapDentalink.cli()

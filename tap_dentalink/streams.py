"""Stream type classes for tap-dentalink."""

from __future__ import annotations

import typing as t
from importlib import resources

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_dentalink.client import DentalinkStream
import json
from datetime import date, timedelta

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.



def create_stream_class(name: str, path: str,
):
    class Stream(DentalinkStream):
        """Define custom stream."""
        primary_keys: t.ClassVar[list[str]] = ["id"]
        replication_key = "id"
        # Optionally, you may also use `schema_filepath` in place of `schema`:
        schema_filepath = SCHEMAS_DIR / f"{name}.json"  # noqa: ERA001

    Stream.name = name
    Stream.path = path

    return Stream

#AgendasStream = create_stream_class("agendas", "/agendas", primary_keys=None, replication_key=None)
CitasStream = create_stream_class("citas", "/v1/citas")
EstadoCitasStream = create_stream_class("estado_citas", "/v1/citas/estados")
MediosDePagoStream = create_stream_class("medios_de_pago", "/v1/medios")
MotivoAtencionStream = create_stream_class("motivos_atencion", "/v1/motivosAtencionEspecialidad")
PacientesStream = create_stream_class("pacientes", "/v1/pacientes")
PagosStream = create_stream_class("pagos", "/v1/pagos")
PrestacionesStream = create_stream_class("prestaciones", "/v1/prestaciones")
SillonesStream = create_stream_class("sillones", "/v1/sillones")
TratamientosStream = create_stream_class("tratamientos", "/v1/tratamientos")
PagosEliminadosStream = create_stream_class("pagoseliminados", "/v1/pagosEliminados")
ArancelesStream = create_stream_class("aranceles", "/v1/aranceles")
BancosStream = create_stream_class("bancos", "/v1/bancos")
CajasStream = create_stream_class("cajas", "/v1/cajas")
CategoriasStream = create_stream_class("categorias", "/v1/categorias")
ConveniosStream = create_stream_class("convenios", "/v1/convenios")
EspecialidadesStream = create_stream_class("especialidades", "/v1/especialidades")
LiquidacionesStream = create_stream_class("liquidaciones", "/v1/liquidaciones")
LiquidacionesDetallesStream = create_stream_class("liquidacionesdetalles", "/v1/liquidacionesDetalles")
TareasStream = create_stream_class("tareas", "/v1/tareas")

class TratamientosDetallesStream(DentalinkStream):
    """Define custom stream."""

    name = "tratamientosdetalles"
    path = "/v1/tratamientosdetalles"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "tratamientosdetalles.json"  # noqa: ERA001


    @property
    def partitions(self) -> list[dict]:
        start_date = date(2014, 7, 10)
        end_date = date.today()
        date_list = [
            (start_date + timedelta(days=i)).isoformat()
            for i in range((end_date - start_date).days + 1)
        ]

        return [{"curr": json.dumps({"fecha_realizacion": {"eq": d}})} for d in date_list]

    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        if not next_page_token:
            params["q"] = context["curr"]
        return params

class ProduccionStream(DentalinkStream):
    """Define custom stream."""

    name = "produccion"
    path = "/v1/reportes/produccion"
    primary_keys: t.ClassVar[list[str]] = ["id_tratamiento", "id_prestacion", "id_paciente", "id_detalle_tratamiento"]
    #replication_key = "id"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "produccion.json"  # noqa: ERA001

    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        if not next_page_token:
            params.update({"id_sucursal": 1, "fecha_inicio": "2011-01-01", "fecha_fin": "2025-12-31"})
        return params

#class PacientesStream(DentalinkStream):
#    """Define custom stream."""
#
#    name = "pacientes"
#    path = "/pacientes"
#    primary_keys: t.ClassVar[list[str]] = ["id"]
#    replication_key = "id"
#    # Optionally, you may also use `schema_filepath` in place of `schema`:
#    schema_filepath = SCHEMAS_DIR / "pacientes.json"  # noqa: ERA001

#class TratamientosStream(DentalinkStream):
#    """Define custom stream."""
#
#    name = "tratamientos"
#    path = "/tratamientos"
#    primary_keys: t.ClassVar[list[str]] = ["id"]
#    replication_key = "id"
#    # Optionally, you may also use `schema_filepath` in place of `schema`:
#    schema_filepath = SCHEMAS_DIR / "tratamientos.json"  # noqa: ERA001

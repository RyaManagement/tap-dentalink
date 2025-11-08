"""Stream type classes for tap-dentalink."""

from __future__ import annotations

import json
from datetime import date, timedelta, datetime

import typing as t
from importlib import resources
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_dentalink.client import DentalinkStream

SCHEMAS_DIR = resources.files(__package__) / "schemas"

def query_dates(start_date, end_date):
    if end_date:
        return [{"lte": end_date}, {"gte": start_date}]
    else:
        return {"gte": start_date}


class CitasStream(DentalinkStream):
    name = "citas"
    path = "/v1/citas"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "citas.json"

    def get_query_params(self, context):
        filter_date = {"fecha": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class EstadoCitasStream(DentalinkStream):
    name = "estado_citas"
    path = "/v1/citas/estados"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "estado_citas.json"


class MediosDePagoStream(DentalinkStream):
    name = "medios_de_pago"
    path = "/v1/medios"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "medios_de_pago.json"


class MotivoAtencionStream(DentalinkStream):
    name = "motivos_atencion"
    path = "/v1/motivosAtencionEspecialidad"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "motivos_atencion.json"


class PacientesStream(DentalinkStream):
    name = "pacientes"
    path = "/v1/pacientes"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "pacientes.json"

    def get_query_params(self, context):
        filter_date = {"fecha_afiliacion": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class PagosStream(DentalinkStream):
    name = "pagos"
    path = "/v1/pagos"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "pagos.json"

    def get_query_params(self, context):
        filter_date = {"fecha_creacion": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class PrestacionesStream(DentalinkStream):
    name = "prestaciones"
    path = "/v1/prestaciones"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "prestaciones.json"


class SillonesStream(DentalinkStream):
    name = "sillones"
    path = "/v1/sillones"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "sillones.json"


class TratamientosStream(DentalinkStream):
    name = "tratamientos"
    path = "/v1/tratamientos"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "tratamientos.json"

    def get_query_params(self, context):
        filter_date = {"fecha": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class PagosEliminadosStream(DentalinkStream):
    name = "pagoseliminados"
    path = "/v1/pagosEliminados"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "pagoseliminados.json"

    def get_query_params(self, context):
        filter_date = {"fecha_eliminacion": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class ArancelesStream(DentalinkStream):
    name = "aranceles"
    path = "/v1/aranceles"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "aranceles.json"


class BancosStream(DentalinkStream):
    name = "bancos"
    path = "/v1/bancos"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "bancos.json"


class CajasStream(DentalinkStream):
    name = "cajas"
    path = "/v1/cajas"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "cajas.json"


class CategoriasStream(DentalinkStream):
    name = "categorias"
    path = "/v1/categorias"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "categorias.json"


class ConveniosStream(DentalinkStream):
    name = "convenios"
    path = "/v1/convenios"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "convenios.json"


class EspecialidadesStream(DentalinkStream):
    name = "especialidades"
    path = "/v1/especialidades"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "especialidades.json"


class LiquidacionesStream(DentalinkStream):
    name = "liquidaciones"
    path = "/v1/liquidaciones"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "liquidaciones.json"

    def get_query_params(self, context):
        filter_date = {"fecha_inicio": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


class LiquidacionesDetallesStream(DentalinkStream):
    name = "liquidacionesdetalles"
    path = "/v1/liquidacionesDetalles"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "liquidacionesdetalles.json"


class TareasStream(DentalinkStream):
    name = "tareas"
    path = "/v1/tareas"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "id"
    schema_filepath = SCHEMAS_DIR / "tareas.json"

    def get_query_params(self, context):
        filter_date = {"fecha_creacion": query_dates(self.config.get("start_date"), self.config.get("end_date"))}
        return {"q": json.dumps(filter_date)}


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
        end_date_conf = self.config.get("end_date")

        start_date = datetime.fromisoformat(self.config.get("start_date")).date()
        end_date = datetime.fromisoformat(end_date_conf).date() if end_date_conf is not None else date.today()

        date_list = [
            (start_date + timedelta(days=i)).isoformat()
            for i in range((end_date - start_date).days + 1)
        ]

        return [{"curr": json.dumps({"fecha_realizacion": {"eq": d}})} for d in date_list]

    def get_query_params(self, context):
        return {"q": context["curr"]}


class ProduccionStream(DentalinkStream):
    """Define custom stream."""

    name = "produccion"
    path = "/v1/reportes/produccion"
    primary_keys: t.ClassVar[list[str]] = ["id_tratamiento", "id_prestacion", "id_paciente", "id_detalle_tratamiento"]
    #replication_key = "id"
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "produccion.json"  # noqa: ERA001

    @property
    def partitions(self) -> list[dict]:
        sucursal_list = [1] # TODO
        return [{"curr": {"id_sucursal": i}} for i in sucursal_list]

    def get_query_params(self, context):
        end_date_conf = self.config.get("end_date")

        params = context["curr"]
        params["fecha_inicio"] = self.config.get("start_date")
        params["fecha_fin"] = end_date_conf if end_date_conf is not None else date.today().strftime("%Y-%m-%d")
        return params

from uuid import UUID
from typing import Any

from src.share.utility.processor_id.source import convert_uuid, generate_uuid, validate_uuid


class ProcessorID:
    __slots__ = ()

    @staticmethod
    def convert(uuid_value: UUID | str, reference_type: type = None) -> UUID | str: pass

    @staticmethod
    def generate(*name: Any, namespace: UUID = None) -> UUID: pass

    @staticmethod
    def validate(uuid_value: UUID | str, is_common: bool = None) -> bool: pass

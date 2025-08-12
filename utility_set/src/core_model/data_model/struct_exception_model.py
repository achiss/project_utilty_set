from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class StructExceptionModel:
    custom_exception: str
    original_exception: str | None
    message: str
    timestamp: str

    def __str__(self) -> str:
        return (f'\nException: {self.custom_exception}'
                f'\nOriginal exception: {self.original_exception}'
                f'\nMessage exception: {self.message}'
                f'\nCreated at: {self.timestamp}')

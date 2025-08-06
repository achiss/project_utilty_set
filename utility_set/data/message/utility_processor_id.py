"""
Configuration module: ProcessorID message templates
"""

# SECTION: base message
BASE_MSG_CONVERT: str = 'Converting ID failed'

BASE_MSG_GENERATE: str = 'Generating ID failed'

BASE_MSG_VALIDATE: str = 'Validating ID failed'


# SECTION: exception message
MSG_DATA_TYPE_ERROR: str = 'invalid data type - expected ({}), got ({})'

MSG_UNEXPECTED_ERROR: str = 'unexpected error {} {}'

MSG_VALUE_ERROR: str = 'incorrect value - {}'

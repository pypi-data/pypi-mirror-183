__version__ = '0.1.1'

from .protocol import (
    Protocol,
    TAIL_SENTINEL,
    Parser,
    StrParser,
    RawParser,
    Etype,
    Event,
)


__all__ = ['Protocol',
           'TAIL_SENTINEL',
           'Parser',
           'Etype',
           'Event']


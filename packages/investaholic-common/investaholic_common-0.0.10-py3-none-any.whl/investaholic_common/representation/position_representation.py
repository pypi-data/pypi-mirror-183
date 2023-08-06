from .representation import Representation
from ..classes.position import Position
from .ticker_representation import TickerRepresentation
import datetime as dt


class PositionRepresentation(Representation):
    _FMT = '%Y-%m-%d'

    def __init__(self, position: Position):
        Representation.__init__(self)
        self._ticker = position.ticker
        self._qty = position.quantity
        self._closing_date = position.closing_date
        self._proposal_code = position.proposal_code

    def as_dict(self) -> dict:
        return {'ticker': TickerRepresentation(self._ticker).as_dict(),
                'quantity': self._qty,
                'closing_date': dt.datetime.strftime(self._closing_date, self._FMT) if self._closing_date is not None else None,
                'proposal_code': self._proposal_code}

    @classmethod
    def as_object(cls, dictionary: dict):
        return Position(ticker=TickerRepresentation.as_object(dictionary['ticker']),
                        closing_date=dt.datetime.strptime(dictionary['closing_date'], cls._FMT) if dictionary['closing_date'] is not None else None,
                        quantity=dictionary['quantity'],
                        proposal_code=dictionary['proposal_code'])


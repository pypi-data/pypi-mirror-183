from .representation import Representation
from ..classes.position import Position
from .ticker_representation import TickerRepresentation


class PositionRepresentation(Representation):
    def __init__(self, position: Position):
        Representation.__init__(self)
        self._ticker = position.ticker
        self._qty = position.quantity
        self._closing_date = position.closing_date
        self._proposal_code = position.proposal_code

    def as_dict(self) -> dict:
        return {'ticker': TickerRepresentation(self._ticker).as_dict(),
                'quantity': self._qty,
                'closing_date': self._closing_date,
                'proposal_code': self._proposal_code}

    @staticmethod
    def as_object(dictionary: dict):
        return Position(ticker=TickerRepresentation.as_object(dictionary['ticker']),
                        closing_date=dictionary['closing_date'],
                        quantity=dictionary['quantity'],
                        proposal_code=dictionary['proposal_code'])

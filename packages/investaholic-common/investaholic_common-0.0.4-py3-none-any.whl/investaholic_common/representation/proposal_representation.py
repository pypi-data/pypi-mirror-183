from .representation import Representation
from ..classes.proposal import Proposal
from .position_representation import PositionRepresentation
from datetime import datetime as dt


class ProposalRepresentation(Representation):
    def __init__(self, proposal: Proposal):
        Representation.__init__(self)
        self._code = proposal.code
        self._date = proposal.date
        self._positions = proposal.positions
        self._user_id = proposal.user_id

    def as_dict(self) -> dict:
        return {'code': self._code,
                'start_date': f'{self._date:%d-%m-%Y}',
                'positions': [PositionRepresentation(position).as_dict() for position in
                              self._positions],
                'user_id': self._user_id}

    @staticmethod
    def as_object(dictionary: dict) -> Proposal:
        start_date = dt.strptime(dictionary['start_date'], '%d-%m-%Y')
        proposal = Proposal(date=start_date,
                            code=dictionary['code'],
                            user_id=dictionary['user_id'])

        for position in dictionary['positions']:
            proposal.add_position(PositionRepresentation.as_object(position))
        return proposal

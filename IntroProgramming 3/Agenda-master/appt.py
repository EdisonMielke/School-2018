'''
Name: Edison Mielke
Cis211 Appointment
'''

from datetime import datetime

class Appt:
    
    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment has a start time, an end time, and a title.
        The start and end time should be on the same day.
        Usage example:
            appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
            appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
            if appt2 > appt1:
                print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
            elif appt1.overlaps(appt2):
                print("Oh no, a conflict in the schedule!")
                print(appt1.intersect(appt2))
       Should print:
            Oh no, a conflict in the schedule!
            2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
        """
        assert finish > start, f"Period finish ({finish}) must be after start ({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __gt__(self, other:'appt') -> bool:
        return self.start > other.finish
    
    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        if self > other:
            return False
        if other > self:
            return False
        return True
    
    def intersect(self, other: 'Appt'):
        if self.overlaps(other):
            if self > other:
                return other
            else:
                return self
    
    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm  | description
        Note that this is accurate only if start and finish
        are on the same day.
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

class Agenda(list):
    """An Agenda is a collection of appointments.
    It has most of the methods of a list, such as
    'append' and iteration, and in
    addition it has a few special methods, including
    a method for finding conflicting appointments.

    Usage:
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    if agenda.unconflicted():
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {agenda.conflicts().text()}")

    Expected output:
    In agenda:
    2018-03-15 13:30 15:30 | Early afternoon nap
    2018-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def text(self) -> str:
        """Returns a string in the same form as we
        expect to find in an input file.  Note that this
        is different from the __str__ method inherited
        from 'list', which is still available.
        """
        as_list = [str(appt) for appt in self]
        return "\n".join(as_list)

    def unconflicted(self) -> bool:
        """True if none of the appointments in this agenda overlap.
        Side effect: Agenda is sorted.
        """
        return len(self.conflicts()) == 0;

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts
        (overlaps) between this agenda and the other.
        Side effect: This agenda is sorted
        """
        self.sort()
        conflicts = Agenda()
        for obj in range(len(self)):
            for i in range(obj +1, len(self)):
                if self[obj].overlaps(self[i]):
                    conflicts.append(self[obj].intersect(self[i]))
                else:
                    break
            return conflicts
    def sort(self, key=lambda appt: appt.start, reverse=False):
        """We sort by start time unless another
        sort key is given.
        """
        super().sort(key=key, reverse=reverse)

    def __str__(self) ->str:
        return self.text()

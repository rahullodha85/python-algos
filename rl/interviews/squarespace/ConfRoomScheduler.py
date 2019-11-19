import datetime
import os
import sys


class CandidateSolution:

    def __init__(self):
        self.reservations = {}
        self.reserved_rooms = set()

    def reserve_room(self, start_epochseconds, end_epochseconds):
        if start_epochseconds >= end_epochseconds:  # meeting start time greater than meeting end time
            return -2
        if start_epochseconds % 300 != 0 or end_epochseconds%300 != 0:  # meetings not starting or ending on 5 mins interval
            return -2
        if end_epochseconds - start_epochseconds < 300:     # meeting duration less than 5 mins
            return -2
        if len(self.reserved_rooms) < 8:    #check if a conference room is available
            if len(self.reservations.keys()) == 0:  #check if any reservations made so far
                conf_room_num = 1
                self.reservations.update({tuple((start_epochseconds, end_epochseconds, conf_room_num)): conf_room_num})
                self.reserved_rooms.add(1)
                return conf_room_num
            else:
                if len(self.reserved_rooms) < 8:
                    for room in range(1, 9):
                        if room not in self.reserved_rooms:
                            self.reserved_rooms.add(room)
                            self.reservations.update({tuple((start_epochseconds, end_epochseconds, room)): room})
                            return room
        else:
            for reservation in self.reservations.keys():
                if not (reservation[0] <= start_epochseconds <= reservation[1]) or not(
                        reservation[0] <= end_epochseconds <= reservation[1]):  # check for conflict
                    return self.reservations.get(reservation)
            return -1


def _iso8691_to_int(instring):
    return int(datetime.datetime.strptime(instring, '%Y-%m-%dT%H:%M:%S.%fZ').timestamp())


def _main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candidate_solution = CandidateSolution()

    for line in sys.stdin:
        parts = line.strip().split(' ')
        start = _iso8691_to_int(parts[0])
        end = _iso8691_to_int(parts[1])

        result = candidate_solution.reserve_room(start, end)
        fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == '__main__':
    _main()
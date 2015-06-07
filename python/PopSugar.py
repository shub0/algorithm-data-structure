#! /usr/bin/python

class Seat:
    # @param index, an integer
    def __init__(self, index):
        self.index = index
        self.next   = None

class Room:
    # @param num_seat, an integer
    def __init__(self, num_seat):
        if num_seat < 1:
            raise VauleError('invalid room config')
        seat = Seat(1)
        constructor = seat
        for index in range(2, num_seat + 1):
            constructor.next = Seat(index)
            constructor = constructor.next
        constructor.next = seat
        self.token = seat
        self.num_seat = num_seat

    # @param start_index, an integer
    def initial_token(self, start_index=1):
        while self.token.next.index != start_index:
            self.token = self.token.next

    # @return a boolean
    def remove_seat(self):
        if self.num_seat == 1:
            self.survivor = self.token.index
            return False
        self.token.next = self.token.next.next
        self.num_seat -= 1
        return True

    def move_token(self):
        self.token = self.token.next

# @param num_seat, an integer
# @return an integer
def play_game(num_seat, start_index):
    # Initial a room with given number of seats
    room = Room(num_seat)
    # Put token at the given position
    room.initial_token(start_index)
    while room.remove_seat():
        room.move_token()
    return room.survivor

if __name__ == '__main__':
    print play_game(100)

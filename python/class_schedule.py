#! /usr/bin/python

'''
Given a Curriculum and a set of classes you want to enroll, give all possible sechdule
for example, cs100 M, W 1pm - 2pm or Thr, Thu 3 pm - 4 pm, cs120, Thu 3pm - 4pm

Output should be CS100 M, W 1pm - 2pm and CS120, Thu 3pm - 4pm
'''

class Schedule:
    # @param {curriculum}, dict
    def __init__(self, curriculum):
        self.curriculum = curriculum
        self.schedule_list = list()

    def enroll(self, class_list, num_enroll_class=0, schedule=['*'] * 120):
        size = len(class_list)
        if num_enroll_class == size:
            self.schedule_list.append(schedule[:])
        else:
            class_name = class_list[num_enroll_class]
            class_time = self.curriculum[class_name]
            for time in class_time:
                tmp_schedule = schedule[:]
                if fill_time(time, schedule, class_name):
                    self.enroll(class_list, num_enroll_class+1, schedule)
                schedule = tmp_schedule[:]


def fill_time(time, schedule, class_name):
    for frame in time:
        for slot in range(frame[0], frame[1]):
            if schedule[slot] != '*':
                return False
    for frame in time:
        for slot in range(frame[0], frame[1]):
            schedule[slot] = class_name
    return True

if __name__ == '__main__':
    solution = Schedule({'cs100': [[(13,14), (61,62)], [(39,40), (87, 88)]],
                         'cs120': [[(39,40), (87, 88)]]})
    solution.enroll(['cs100', 'cs120'])
    print solution.schedule_list

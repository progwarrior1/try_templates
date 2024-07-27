import json

candidate = {}


class Candidate:
    def __init__(self, path):
        self.path = path

    def load_candidates_in_dict(self):
        global candidate
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate

    def get_data_from_id(self, id1):
        with open(self.path, 'r') as file:
            data = json.load(file)
        for i in data:
            candidate[i['id']] = i
        return candidate[int(id1)]

    def get_candidates_by_name(self, candidate_name):
        count = 1
        string = {}
        for can_ in candidate.values():
            candidate1 = can_['name'].split(' ')
            candidate1 = [x.lower() for x in candidate1]
            if candidate_name.lower() in candidate1:
                string[count] = can_['name']
            count += 1
        return string

    def get_candidates_by_skill(self, skill_name):
        count = 1
        string = {}
        for can_ in candidate.values():
            candidate1 = can_['skills'].split(', ')
            candidate1 = [x.lower() for x in candidate1]
            if skill_name.lower() in candidate1:
                string[count] = can_['name']
        return string

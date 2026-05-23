
class State:
    def __init__(self):
        self.score = 0
        
        self.current_level_physics = 1
        self.current_level_chemistry = 1
        self.current_level_maths = 1

        self.physics_questions = []
        self.chemistry_questions = []
        self.maths_questions = []

        self.finished_physics_questions = {
            "right": {},
            "wrong": {}
        }
        self.finished_chemistry_questions = {
            "right": {},
            "wrong": {}
        }
        self.finished_maths_questions = {
            "right": {},
            "wrong": {}
        }

        self.finished_questions = {
            "right": {},
            "wrong": {}
        }


state = State()


SUBJECT_IDS = {
    "physics": [1, 40],
    "chemistry": [41, 80],
    "maths": [81, 120]

}


SCORE_PER_LEVEL = {
    1: 11,
    2: 13,
    3: 15,
    4: 17,
    5: 19
}


NORMALIZED_SUBJECT = {
    1: "physics",
    2: "chemistry",
    3: "maths"
}


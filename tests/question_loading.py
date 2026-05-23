import yaml

from configs import state, SUBJECT_IDS

with open("questions.yaml", "r") as file:
    content = yaml.safe_load(file)

    for question in content:
        if SUBJECT_IDS["physics"][0] <= question.get("id") <= SUBJECT_IDS["physics"][1]:
            state.physics_questions.append(question)
        
        elif SUBJECT_IDS["chemistry"][0] <= question.get("id") <= SUBJECT_IDS["chemistry"][1]:
            state.chemistry_questions.append(question)

        elif SUBJECT_IDS["maths"][0] <= question.get("id") <= SUBJECT_IDS["maths"][1]:
            state.maths_questions.append(question)

print(state.physics_questions)
# print(state.chemistry_questions)
# print(state.maths_questions)
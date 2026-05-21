import yaml

score = 0
finished_physics_questions = []
finished_chemistry_questions = []
finished_maths_questions = []
finished_question_ids = []

score_schema = {
    1: 11,
    2: 13,
    3: 15,
    4: 17,
    5: 19
}

physics_ids = [1, 40]
chemistry_ids = [41, 80]
maths_ids = [81, 120]


def start():
    with open("questions.yaml", "r") as file:
        content = yaml.safe_load(file)
        
        # physics_questions = [next(question for question in content) if physics_ids[0]<= question.get(id) <= physics_ids[1] else None]
        physics_questions = []
        chemistry_questions = []
        maths_questions = []

        for question in content:
            if physics_ids[0] <= question.get("id") <= physics_ids[1]:
                physics_questions.append(question)

        for question in content:
            if chemistry_ids[0] <= question.get("id") <= chemistry_ids[1]:
                chemistry_questions.append(question)

        for question in content:
            if maths_ids[0] <= question.get("id") <= maths_ids[1]:
                maths_questions.append(question)

        questions = {}

        alpha_index = {
            1: "A",
            2: "B",
            3: "C",
            4: "D"
        }

        choice = input("Which subject would you like to go with first?\n1. Physics\n2. Chemistry\n3. Maths\n").strip()

        if isinstance(choice, int):
            if choice not in [1, 2, 3]:
                print("Unrecognized subject!")
                return

        elif choice.lower() not in ["physics", "chemistry", "maths"]:
            print("Unrecognized subject!")
            return

        if choice == 1 or choice == "physics":
            current_level = 1
            for question in physics_questions: 
                if question.get("difficulty") == current_level:
                    ques = question.get("question")
                    options = question.get("options")
                    questions[ques] = options

                    right_index = question.get("correct_index")
                    right_answer = question.get("options")[right_index]

                    level = question.get("difficulty")

                    if len(finished_physics_questions) == 0:
                        print(f"\n\n{alpha_index[1]}. {ques}\n")
                    else:
                        print(f"\n\n{alpha_index[len(finished_physics_questions)+1]}. {ques}\n")

                    for index, option in enumerate(options, start=0):
                        print(f"{index+1}. {option}:\n")

                    answer = input("\n").strip()

                    if answer == right_answer or answer[:1] == right_index:
                        score += score_schema[level]
                        if 1 <= level <= 5:
                            current_level += 1

                    else:
                        if level not in [1, 5]:
                            current_level -= 1 

                    choice = input("Choose one to change subject:\n1. Physics\n2. Chemistry\n3. Maths\n").strip()


        
        elif choice in [2, "chemistry"]:
            current_level = 1
            for question in chemistry_questions: 
                if question.get("difficulty") == current_level:
                    ques = question.get("question")
                    options = question.get("options")
                    questions[ques] = options

                    right_index = question.get("correct_index")
                    right_answer = question.get("options")[right_index]

                    level = question.get("difficulty")

                    if len(finished_chemistry_questions) == 0:
                        print(f"\n\n{alpha_index[1]}. {ques}\n")
                    else:
                        print(f"\n\n{alpha_index[len(finished_chemistry_questions)+1]}. {ques}\n")

                    for index, option in enumerate(options, start=0):
                        print(f"{index+1}. {option}:")

                    answer = input("\n").strip()

                    if answer == right_answer or answer[:1] == right_index:
                        score += score_schema[level]
                        if 1 <= level <= 5:
                            current_level += 1

                    else:
                        if level not in [1, 5]:
                            current_level -= 1 

                    choice = input("Choose one to change subject:\n1. Physics\n2. Chemistry\n3. Maths\n").strip()




        elif choice in [3, "maths"]:
            current_level = 1
            for question in maths_questions: 
                if question.get("difficulty") == current_level:
                    ques = question.get("question")
                    options = question.get("options")
                    questions[ques] = options

                    right_index = question.get("correct_index")
                    right_answer = question.get("options")[right_index]

                    level = question.get("difficulty")

                    if len(finished_maths_questions) == 0:
                        print(f"\n\n{alpha_index[1]}. {ques}\n")
                    else:
                        print(f"\n\n{alpha_index[len(finished_maths_questions)+1]}. {ques}\n")

                    for index, option in enumerate(options, start=0):
                        print(f"{index+1}. {option}:\n")

                    answer = input("\n").strip()

                    if answer == right_answer or answer[:1] == right_index:
                        score += score_schema[level]
                        if 1 <= level <= 5:
                            current_level += 1

                    else:
                        if level not in [1, 5]:
                            current_level -= 1 

                    choice = input("Choose one to change subject:\n1. Physics\n2. Chemistry\n3. Maths\n").strip()



start()



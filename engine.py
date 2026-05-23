import yaml
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="engine.log",
    filemode="a",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)



from configs import state, SUBJECT_IDS, NORMALIZED_SUBJECT, SCORE_PER_LEVEL


def run(question_file):
    score = state.score

    with open(question_file, "r") as file:
        content = yaml.safe_load(file)

        physics_level = state.current_level_physics
        chemistry_level = state.current_level_chemistry
        maths_level = state.current_level_maths

        finished_physics_questions = state.finished_physics_questions
        finished_chemistry_questions = state.finished_chemistry_questions
        finished_maths_questions = state.finished_maths_questions


        for question in content:
            if SUBJECT_IDS["physics"][0] <= question.get("id") <= SUBJECT_IDS["physics"][1]:
                state.physics_questions.append(question)
            
            elif SUBJECT_IDS["chemistry"][0] <= question.get("id") <= SUBJECT_IDS["chemistry"][1]:
                state.chemistry_questions.append(question)

            elif SUBJECT_IDS["maths"][0] <= question.get("id") <= SUBJECT_IDS["maths"][1]:
                state.maths_questions.append(question)

        print(f"Loaded amount of questions:-\nPhysics: {len(state.physics_questions)}\nChemistry:{len(state.chemistry_questions)}\nMaths: {len(state.maths_questions)}")

        while True:
            choice = input("First, choose one subject to continue:\n1. Physics\n2. Chemistry\n3. Maths\n").strip()
            logger.info("First, choose one subject to continue:\n1. Physics\n2. Chemistry\n3. Maths\n")

            try:
                val = int(choice)
                if val not in [1, 2, 3]:
                    logger.warning("Invalid subject!")
                    print("Invalid subject!")
                    continue
                    
                choice = int(choice)
                break

            except ValueError:
                if choice.lower() not in [NORMALIZED_SUBJECT[i] for i in range(1, 4)]:
                    logger.warning("Invalid subject!")
                    print("Invalid subject!")
                    continue
                    break


        while True:
            if choice in [1, NORMALIZED_SUBJECT[1]]: # Physics
                print("You selected physics!")
                logger.info("You selected physics!")

                print(f"Score: {score}")
                logger.info(f"Score: {score}")
                for question in state.physics_questions:
                    question_difficulty = question.get("difficulty")

                    if question_difficulty == physics_level and question not in [state.finished_physics_questions["right"], state.finished_physics_questions["wrong"]]:
                        physics_questions_solved_count = len(finished_physics_questions["right"]) + len(finished_physics_questions["wrong"])
                        logger.info(f"\n{physics_questions_solved_count+1}. {question.get("question")}")
                        print(f"\n{physics_questions_solved_count+1}. {question.get("question")}")

                        options = question.get("options")

                        for index, option in enumerate(options, start=1):
                            print(f"{index}. {option}")
                            logger.info(f"{index}. {option}")

                        answer = input().strip()

                        correct_answer_index = question.get("correct_index")
                        try:
                            val = int(answer)
                            if val - 1 == correct_answer_index:
                                print("Correct Answer")
                                logger.info("Correct Answer")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_physics_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if physics_level < 5:
                                    physics_level += 1
                                    print(f"New level: {physics_level}")
                                    logger.info(f"New level: {physics_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.warning("Level maxed out at 5!")

                            else:
                                logger.error("Wrong answer!")
                                print("Wrong answer!")
                                state.finished_physics_questions["wrong"] = question
                                if 1 < physics_level <= 5:
                                    physics_level -= 1
                                    print(f"New level: {physics_level}")
                                    logger.info(f"New level: {physics_level}")

                                else:
                                    print("Lowest level reached!")
                                    logger.warning("Lowest level reached!")

                        except ValueError:
                            if answer.lower() in [correct[correct_answer_index].lower() for correct in options]:
                                print("Correct Answer!")
                                logger.info("Correct Answer!")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_physics_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if physics_level < 5:
                                    physics_level += 1
                                    logger.info(f"New level: {physics_level}")
                                    print(f"New level: {physics_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.warning("Level maxed out at 5!")

                            else:
                                logger.error("Wrong answer!")
                                print("Wrong answer!")
                                state.finished_physics_questions["wrong"] = question

                                if 1 < physics_level <= 5:
                                    physics_level -= 1
                                    logger.info(f"New level: {physics_level}")
                                    print(f"New level: {physics_level}")
                                    
                                else:
                                    logger.warning("Lowest level reached!")
                                    print("Lowest level reached!")

                        choice = input("Choose anyone subject to change\nPress enter to continue with current subject:\n").strip()
                        logger.info("Choose anyone subject to change\nPress enter to continue with current subject:\n")

                    if choice in [1, NORMALIZED_SUBJECT[1], "", None]:
                        continue

                    else:
                        break


            elif choice in [2, NORMALIZED_SUBJECT[2]]: # Chemistry
                print("You selected chemistry!")
                logger.info("You selected chemistry!")

                print(f"Score: {score}")
                logger.info(f"Score: {score}")

                for question in state.chemistry_questions:
                    question_difficulty = question.get("difficulty")

                    if question_difficulty == chemistry_level and question not in [state.finished_chemistry_questions["right"], state.finished_chemistry_questions["wrong"]]:
                        finished_chemistry_questions_count = len(finished_chemistry_questions)
                        print(f"\n{finished_chemistry_questions_count+1}. {question.get("question")}")
                        logger.info(f"\n{finished_chemistry_questions_count+1}. {question.get("question")}")

                        options = question.get("options")

                        for index, option in enumerate(options, start=1):
                            print(f"{index}. {option}")
                            logger.info(f"{index}. {option}")

                        answer = input().strip()

                        correct_answer_index = question.get("correct_index")
                        try:
                            val = int(answer)
                            if val - 1 == correct_answer_index:
                                print("Correct Answer")
                                logger.info("Correct Answer")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_chemistry_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if chemistry_level < 5:
                                    chemistry_level += 1
                                    print(f"New level: {chemistry_level}")
                                    logger.info(f"New level: {chemistry_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.warning("Level maxed out at 5!")

                            else:
                                logger.error("Wrong answer!")
                                print("Wrong answer!")
                                state.finished_chemistry_questions["wrong"] = question
                                if 1 < chemistry_level <= 5:
                                    chemistry_level -= 1
                                    print(f"New level: {chemistry_level}")
                                    logger.info(f"New level: {chemistry_level}")

                                else:
                                    logger.warning("Lowest level reached!")
                                    print("Lowest level reached!")

                        except ValueError:
                            if answer.lower() in [correct[correct_answer_index].lower() for correct in options]:
                                print("Correct Answer!")
                                logger.info("Correct Answer!")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_chemistry_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if chemistry_level < 5:
                                    chemistry_level += 1
                                    logger.info(f"New level: {chemistry_level}")
                                    print(f"New level: {chemistry_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.warning("Level maxed out at 5!")

                            else:
                                logger.error("Wrong answer!")
                                print("Wrong answer!")
                                state.finished_chemistry_questions["wrong"] = question

                                if 1 < chemistry_level <= 5:
                                    chemistry_level -= 1
                                    logger.info(f"New level: {chemistry_level}")
                                    print(f"New level: {chemistry_level}")
                                    
                                else:
                                    logger.warning("Lowest level reached!")
                                    print("Lowest level reached!")

                        choice = input("Choose anyone subject to change\nPress enter to continue with current subject:\n").strip()
                        logger.info("Choose anyone subject to change\nPress enter to continue with current subject:\n")

                    if choice in [2, NORMALIZED_SUBJECT[2], "", None]:
                        continue

                    else:
                        break


            elif choice in [3, NORMALIZED_SUBJECT[3]]: # Maths
                print("You selected maths!")
                logger.info("You selected maths!")

                print(f"Score: {score}")
                logger.info(f"Score: {score}")

                for question in state.maths_questions:                    
                    question_difficulty = question.get("difficulty")

                    if question_difficulty == maths_level and question not in [state.finished_maths_questions["right"], state.finished_maths_questions["wrong"]]:
                        finished_maths_questions_count = len(finished_maths_questions)
                        print(f"\n{finished_maths_questions_count+1}. {question.get("question")}")
                        logger.info(f"\n{finished_maths_questions_count+1}. {question.get("question")}")

                        options = question.get("options")

                        for index, option in enumerate(options, start=1):
                            print(f"{index}. {option}")
                            logger.info(f"{index}. {option}")

                        answer = input().strip()

                        correct_answer_index = question.get("correct_index")
                        try:
                            val = int(answer)
                            if val - 1 == correct_answer_index:
                                print("Correct Answer")
                                logger.info("Correct Answer")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_maths_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if maths_level < 5:
                                    maths_level += 1
                                    print(f"New level: {maths_level}")
                                    logger.info(f"New level: {maths_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.warning("Level maxed out at 5!")

                            else:
                                logger.warning("Wrong answer!")
                                print("Wrong answer!")
                                state.finished_maths_questions["wrong"] = question
                                if 1 < maths_level <= 5:
                                    maths_level -= 1
                                    print(f"New level: {maths_level}")
                                    logger.info(f"New level: {maths_level}")

                                else:
                                    print("Lowest level reached!")
                                    logger.warning("Lowest level reached!")

                        except ValueError:
                            if answer.lower() in [correct[correct_answer_index].lower() for correct in options]:
                                print("Correct Answer!")
                                logger.info("Correct Answer!")
                                score += SCORE_PER_LEVEL[question_difficulty]
                                state.finished_maths_questions["right"] = question

                                print(f"Score: {score}")
                                logger.info(f"Score: {score}")

                                if maths_level < 5:
                                    maths_level += 1
                                    print(f"New level: {maths_level}")
                                    logger.info(f"New level: {maths_level}")

                                else:
                                    print("Level maxed out at 5!")
                                    logger.info("Level maxed out at 5!")

                            else:
                                print("Wrong answer!")
                                logger.error("Wrong answer!")
                                state.finished_maths_questions["wrong"] = question

                                if 1 < maths_level <= 5:
                                    maths_level -= 1
                                    print(f"New level: {maths_level}")
                                    logger.info(f"New level: {maths_level}")
                                    
                                else:
                                    print("Lowest level reached!")
                                    logger.warning("Lowest level reached!")

                        choice = input("Choose anyone subject to change\nPress enter to continue with current subject:\n").strip()
                        logger.info("Choose anyone subject to change\nPress enter to continue with current subject:\n")

                    if choice in [3, NORMALIZED_SUBJECT[3], "", None]:
                        continue

                    else:
                        break
        

            else:
                choice = input("\nChoose one subject to continue:\n1. Physics\n2. Chemistry\n3. Maths\n").strip()
                logger.info("First, choose one subject to continue:\n1. Physics\n2. Chemistry\n3. Maths\n")


run("questions.yaml")


import yaml

with open("questions.yaml", "r") as file:
    content = yaml.safe_load(file)

    print("Content loaded")

    for question in content:
        if question.get("question") == "A stone dropped from the top of a tower travels 24.5 m in its last second of journey. The height of the tower is (take g = 9.8 m/s²)":
            print(question.get("subject"))
        # else:
        #     print("Not found")
import yaml

def get_test_cases(config):

    inputs = []
    outputs = []

    with open(config, "r") as config_file:
        contents = yaml.load(config_file, Loader=yaml.FullLoader)
    
    for test in contents["tests"]:
        inputs.append(test["input"])
        outputs.append(test["output"])
    
    return inputs, outputs

def evaluate(ID, code):

    user_input = {}
    state = {"success": False, "message": ""}

    inputs, outputs = get_test_cases(ID + "/config.yaml")

    try:
        exec(code, user_input)
        func_name = user_input.keys()[0]  # TODO: what if more than one func

        for (input, output) in zip(inputs, outputs):
            if user_input[func_name](input) == output:
                continue
            else:
                state["message"] = "Try again!"
                return state

        state["success"] = True
        state["message"] = "Nice work!"

        return state

    except (RuntimeError, SyntaxError) as err:
        state["message"] = str(err)
        return state

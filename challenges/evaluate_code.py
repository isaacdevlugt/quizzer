def evaluate(location, contents, code):

    user_input = {}
    state = {"success": False, "message": ""}
    test_cases = contents["tests"]

    try:
        exec(code, user_input)
        func_name = list(user_input.keys())[1]
        #correct_code = getattr(__import__(location + ".correct_code", fromlist=["add"]), "add")
        for test_case in test_cases:
            if user_input[func_name](*test_case["input"]) == test_case["output"]: 
                # TODO: this will only work when the function accepts individual args
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
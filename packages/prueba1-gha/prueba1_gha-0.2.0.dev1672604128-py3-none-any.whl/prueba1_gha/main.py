def build_hi(name):
    # assert name == "bad_name", f"name should be More!!"  # PASS
    # x = 10
    # print(eval("x * 10"))  # PASS
    # username = "user"           # FAIL
    # password = "admin123456"    # FAIL
    # print(username, password)
    return f"Hi, {name}"


if __name__ == "__main__":
    print(build_hi("Martin+mjmorep+2023"))

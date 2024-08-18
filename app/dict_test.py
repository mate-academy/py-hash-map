from app.main import Dictionary


if __name__ == "__main__":
    custom_dict = Dictionary()

    custom_dict["1"] = 1
    custom_dict["2"] = 2
    print(custom_dict["1"])
    print(custom_dict["2"])

    custom_dict.clear()
    print(len(custom_dict))

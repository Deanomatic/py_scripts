def main():
    f = open("/Users/deansmith/workspace/python_fun/golf.txt", "r")
    main_list = list(f.read().splitlines())
    # print(main_list)
    name_and_score = list()
    counter = 0
    while counter < 9:
        for item in main_list[:2]:
            name_and_score.append(item)
        def find_lowest(name_and_score):
            pass
        print(name_and_score)
        del main_list[0:2]
        name_and_score = list()
        counter += 1
        
main()
def decor_result(result_func):
    def distinction(marks):
        for i in marks:
            if i>=75:
                print("Distinction")
        else:
            result_func(marks)
    return distinction
@decor_result
def result(marks):
    for i in marks:
        if i>33:
            pass
        else:
            print("Fail")
            break
    else:
        print("Pass")
result([55,65,96,67,84])
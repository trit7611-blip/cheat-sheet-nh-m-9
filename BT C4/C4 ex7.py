def computegrade(score):
    
    if score > 1.0 or score < 0.0:
        return "Bad score" # Trả về lỗi nếu điểm nằm ngoài phạm vi 0.0 - 1.0
        
    # Chuỗi điều kiện if/elif/else để xác định điểm chữ
    elif score > 0.9:
        return "A"
    elif score > 0.8:
        return "B"
    elif score > 0.7:
        return "C"
    elif score > 0.6:
        return "D"
    else: # Bao gồm tất cả các trường hợp <= 0.6
        return "F"
while True:
    s_score = input("Enter score: ")
    if not s_score:
        break
    try:
        f_score = float(s_score)
        grade = computegrade(f_score)
        if grade == "Bad score":
            print("Bad score")
        else:
            print(grade)
    except ValueError:
        print("Bad score")
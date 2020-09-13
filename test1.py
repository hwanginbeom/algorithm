def solution(s):
    length = []
    result = ""

    if len(s) == 1:  # 1 일때는 길이가 1이므로 종료한다.
        return 1

    for cut in range(1, len(s) // 2 + 1):  # for문을 돌리는데 //2+1 한 이유는 자르는데 절반이상으로 할 필요가 없기 때문이다.
        count = 1
        tempStr = s[:cut]  # cut길이만큼으로 비교한다.
        print("tempStr(11):"+tempStr)
        for i in range(cut, len(s), cut):  # cut 부터 시작하여 cut을 스탭으로 가진다
            if s[i:i + cut] == tempStr:  # 만약 자른값이랑 그 다음값이 같으면
                count += 1  # 카운트를 더하고
            else:  # 아닐경우
                if count == 1:  # 카운트가 1이면
                    count = ""  # 카운트에 "" 를 넣어서 합친다.
                result += str(count) + tempStr  # 카운트 + tempStr넣었던 값을 더한다 그걸 result에 넣는다
                tempStr = s[i:i + cut]  # 그 다음 다음 tempStr 값을 다시 구한다.
                count = 1  # 카운트는 다시 1부터 시작한다.

        if count == 1:  # 여긴 cut한 부분이 끝났을때 돌아간다
            count = ""
        result += str(count) + tempStr  # 다시 넣어주고
        print("result(24):" + result)

        length.append(len(result))  # result 길이 값을 더해준다.
        result = ""

    return min(length)

s = "ABABA"
print(solution(s))
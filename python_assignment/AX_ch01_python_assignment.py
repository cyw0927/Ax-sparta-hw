"""
AX 2회차 Chapter 1 - Python 기초 과제

학습 범위
- 문자열(str)
- 리스트(list)
- 딕셔너리(dict)
- 조건문(if)
- 반복문(for)
- 함수(def, return)
- 예외처리(try-except)

실행 방법
1. 터미널에서 python_assignment 폴더로 이동
2. python AX_ch01_python_assignment.py 실행
"""


def print_title(title):
    """실행 결과를 보기 쉽게 구분선을 출력하는 보조 함수입니다."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ------------------------------------------------------------
# Part 1. 리스트와 반복문을 이용한 데이터 처리
# ------------------------------------------------------------
def part1_list_and_loop():
    print_title("Part 1. 리스트와 반복문")

    # 여러 학생의 점수를 리스트에 저장합니다.
    scores = [78, 92, 55, 64, 88, 49, 100, 73]

    print("전체 점수:", scores)

    # 조건을 만족한 학생 수를 세기 위한 변수입니다.
    pass_count = 0
    high_score_count = 0

    print("\n학생별 결과")

    # 리스트의 점수를 하나씩 꺼내 반복합니다.
    for score in scores:
        # 60점 이상이면 합격입니다.
        if score >= 60:
            result = "합격"
            pass_count = pass_count + 1
        else:
            result = "불합격"

        # 80점 이상인 학생 수도 따로 계산합니다.
        if score >= 80:
            high_score_count = high_score_count + 1

        print(f"{score}점 -> {result}")

    # 전체 학생 수에서 합격자 수를 빼서 불합격자 수를 계산합니다.
    fail_count = len(scores) - pass_count

    print("\n[집계 결과]")
    print(f"전체 학생 수: {len(scores)}명")
    print(f"합격자 수: {pass_count}명")
    print(f"불합격자 수: {fail_count}명")
    print(f"80점 이상 학생 수: {high_score_count}명")


# ------------------------------------------------------------
# Part 2. 딕셔너리를 이용한 단어 빈도 분석
# ------------------------------------------------------------
def part2_word_frequency_basic():
    print_title("Part 2. 딕셔너리를 이용한 단어 빈도 분석")

    # 과제에서 제시한 문장을 사용합니다.
    sentence = """
파이썬 공부는 재미있다
파이썬 공부는 어렵지만 재미있다
데이터 분석에도 파이썬을 사용한다
파이썬 공부를 계속하면 실력이 늘어난다
"""

    # split()으로 공백과 줄바꿈을 기준으로 단어를 나눕니다.
    words = sentence.split()

    # Key에는 단어, Value에는 등장 횟수를 저장합니다.
    word_counts = {}

    # 단어를 하나씩 확인합니다.
    for word in words:
        # 이미 나온 단어라면 기존 값에 1을 더합니다.
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        # 처음 나온 단어라면 1을 저장합니다.
        else:
            word_counts[word] = 1

    print("전체 단어 목록:")
    print(words)

    print("\n[전체 단어 빈도]")
    for word in word_counts:
        print(f"{word} : {word_counts[word]}회")

    print("\n[2회 이상 등장한 단어]")
    for word in word_counts:
        if word_counts[word] >= 2:
            print(f"{word} : {word_counts[word]}회")

    return sentence, word_counts


# ------------------------------------------------------------
# Part 3. 함수로 반복되는 코드 정리하기
# ------------------------------------------------------------
def count_words(sentence):
    """문자열을 받아 단어별 등장 횟수를 딕셔너리로 반환합니다."""
    words = sentence.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        else:
            word_counts[word] = 1

    return word_counts


def print_words_over_count(word_counts, min_count):
    """기준 횟수 이상 등장한 단어만 출력합니다."""
    found = False

    for word in word_counts:
        if word_counts[word] >= min_count:
            print(f"{word} : {word_counts[word]}회")
            found = True

    if found == False:
        print(f"{min_count}회 이상 등장한 단어가 없습니다.")


def part3_function_refactoring(sentence):
    print_title("Part 3. 함수로 반복 코드 정리")

    result = count_words(sentence)

    print("[count_words()가 반환한 결과]")
    print(result)

    print("\n[2회 이상 등장한 단어]")
    print_words_over_count(result, 2)

    return result


# ------------------------------------------------------------
# Part 4. 오류 확인 및 예외처리
# ------------------------------------------------------------
def search_word_with_exception(word_counts, search_word):
    """없는 Key를 조회할 때 발생할 수 있는 KeyError를 처리합니다."""
    try:
        count = word_counts[search_word]
        print(f"'{search_word}'의 등장 횟수: {count}회")
    except KeyError:
        print(f"'{search_word}'는 분석 결과에 없는 단어입니다.")


def part4_error_check(word_counts):
    print_title("Part 4. 오류 확인 및 코드 검증")

    print("[존재하는 단어 검색]")
    search_word_with_exception(word_counts, "파이썬")

    print("\n[존재하지 않는 단어 검색]")
    search_word_with_exception(word_counts, "자바")

    print("\n[오류 확인 순서]")
    print("1. 오류 메시지 확인")
    print("2. 문제가 발생한 코드 위치 확인")
    print("3. 변수 값 확인")
    print("4. 자료형 확인")
    print("5. 코드 수정")
    print("6. 다시 실행")


# ------------------------------------------------------------
# 도전 문제
# ------------------------------------------------------------
def find_most_frequent_words(word_counts):
    """가장 많이 등장한 단어와 횟수를 찾습니다."""
    max_count = 0
    most_words = []

    for word in word_counts:
        count = word_counts[word]

        if count > max_count:
            max_count = count
            most_words = [word]
        elif count == max_count:
            most_words.append(word)

    return most_words, max_count


def find_least_frequent_words(word_counts):
    """가장 적게 등장한 단어와 횟수를 찾습니다."""
    min_count = None
    least_words = []

    for word in word_counts:
        count = word_counts[word]

        if min_count is None or count < min_count:
            min_count = count
            least_words = [word]
        elif count == min_count:
            least_words.append(word)

    return least_words, min_count


def save_word_counts(word_counts, filename):
    """단어 빈도 결과를 UTF-8 텍스트 파일로 저장합니다."""
    with open(filename, "w", encoding="utf-8") as file:
        for word in word_counts:
            file.write(f"{word} : {word_counts[word]}회\n")


def challenge(word_counts):
    print_title("도전 문제")

    most_words, max_count = find_most_frequent_words(word_counts)
    print(f"가장 많이 등장한 단어: {', '.join(most_words)} ({max_count}회)")

    least_words, min_count = find_least_frequent_words(word_counts)
    print(f"가장 적게 등장한 단어: {', '.join(least_words)} ({min_count}회)")

    print("\n[특정 단어 검색]")
    search_word_with_exception(word_counts, "재미있다")

    print("\n[3회 이상 등장한 단어]")
    print_words_over_count(word_counts, 3)

    output_filename = "word_frequency_result.txt"
    save_word_counts(word_counts, output_filename)
    print(f"\n분석 결과를 '{output_filename}' 파일로 저장했습니다.")


def main():
    # Part 1 실행
    part1_list_and_loop()

    # Part 2 실행
    sentence, basic_word_counts = part2_word_frequency_basic()

    # Part 3 실행
    function_word_counts = part3_function_refactoring(sentence)

    # Part 4 실행
    part4_error_check(function_word_counts)

    # 도전 문제 실행
    challenge(function_word_counts)

    # Part 2와 Part 3이 같은 결과를 만들었는지 마지막으로 확인합니다.
    print_title("최종 검증")
    print("Part 2 결과와 Part 3 결과가 같은가?", basic_word_counts == function_word_counts)


if __name__ == "__main__":
    main()

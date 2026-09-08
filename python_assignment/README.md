# AX 2회차 Chapter 1 — Python 기초 과제

이 폴더는 **Python 기초 과제만 따로 제출하기 위한 폴더**입니다.

## 제출용 파일

- `AX_ch01_python_assignment.py` : Part 1~4 + 도전 문제 전체 코드
- `word_frequency_result.txt` : 도전 문제의 파일 저장 결과 예시
- `README.md` : 실행 방법, 코드 설명, 예상 결과, 확인 질문 답변

---

# 1. 실행 방법

VS Code 터미널에서 저장소를 받은 뒤 Python 과제 폴더로 이동합니다.

```bash
cd python_assignment
```

그 다음 실행합니다.

```bash
python AX_ch01_python_assignment.py
```

Windows에서 `python` 명령어가 안 되면 다음처럼 실행할 수 있습니다.

```bash
py AX_ch01_python_assignment.py
```

실행하면 Part 1 → Part 2 → Part 3 → Part 4 → 도전 문제 → 최종 검증 순서로 결과가 출력됩니다.

---

# 2. Part 1 — 리스트와 반복문을 이용한 데이터 처리

먼저 여러 점수를 리스트에 저장했습니다.

```python
scores = [78, 92, 55, 64, 88, 49, 100, 73]
```

`for` 문은 리스트의 값을 하나씩 꺼내서 같은 작업을 반복합니다.

```python
for score in scores:
```

첫 반복에서는 `78`, 두 번째 반복에서는 `92`, 다음에는 `55`가 `score` 변수에 들어갑니다.

점수가 60점 이상인지 `if` 문으로 판단합니다.

```python
if score >= 60:
    result = "합격"
    pass_count = pass_count + 1
else:
    result = "불합격"
```

`pass_count`는 처음에 0으로 시작하고 합격자가 나올 때마다 1씩 증가합니다.

80점 이상인 학생 수도 같은 방식으로 따로 셉니다.

```python
if score >= 80:
    high_score_count = high_score_count + 1
```

예상되는 주요 결과는 다음과 같습니다.

```text
전체 학생 수: 8명
합격자 수: 6명
불합격자 수: 2명
80점 이상 학생 수: 3명
```

이 Part에서 사용한 핵심 문법은 `list`, `for`, `if`입니다.

---

# 3. Part 2 — 딕셔너리를 이용한 단어 빈도 분석

과제에서 제시한 문장을 그대로 분석합니다.

```python
sentence = """
파이썬 공부는 재미있다
파이썬 공부는 어렵지만 재미있다
데이터 분석에도 파이썬을 사용한다
파이썬 공부를 계속하면 실력이 늘어난다
"""
```

먼저 `split()`을 사용하여 문장을 단어 단위로 나눕니다.

```python
words = sentence.split()
```

그 다음 빈 딕셔너리를 만듭니다.

```python
word_counts = {}
```

이 딕셔너리에서는 다음과 같이 사용합니다.

- Key: 단어
- Value: 그 단어가 등장한 횟수

예를 들어 `{'파이썬': 3}`이라면 `파이썬`이 Key이고 `3`이 Value입니다.

단어를 하나씩 반복하면서 처음 나온 단어인지 이미 나온 단어인지 확인합니다.

```python
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
```

처음 `파이썬`을 만나면 딕셔너리에 없으므로 값이 1이 됩니다.

두 번째 `파이썬`을 만나면 이미 존재하므로 기존 값 1에 1을 더해 2가 됩니다.

세 번째 등장하면 3이 됩니다.

주요 결과는 다음과 같습니다.

```text
파이썬 : 3회
공부는 : 2회
재미있다 : 2회
```

`파이썬`과 `파이썬을`은 문자열이 서로 다르기 때문에 다른 단어로 계산됩니다. 이 과제는 형태소 분석이 아니라 `split()`을 이용한 기초 문자열 처리이므로 정상적인 결과입니다.

`collections.Counter` 같은 자동 빈도 계산 기능은 사용하지 않았습니다.

---

# 4. Part 3 — 함수로 반복 코드 정리

Part 2에서 직접 작성한 단어 빈도 계산 코드를 함수로 만들었습니다.

```python
def count_words(sentence):
```

함수는 문자열을 매개변수로 받아 단어 빈도를 계산한 뒤 딕셔너리를 반환합니다.

```python
return word_counts
```

사용할 때는 다음처럼 함수의 결과를 변수에 저장합니다.

```python
result = count_words(sentence)
```

또한 특정 횟수 이상 나온 단어를 출력하는 기능도 별도 함수로 나눴습니다.

```python
def print_words_over_count(word_counts, min_count):
```

이 함수는 `min_count` 값을 바꾸면 2회 이상, 3회 이상처럼 기준을 바꿔 재사용할 수 있습니다.

함수를 사용한 이유는 같은 코드를 여러 번 복사하지 않고 하나의 기능으로 묶어서 재사용하기 위해서입니다.

---

# 5. Part 4 — 오류 확인 및 예외처리

딕셔너리에서 존재하지 않는 Key를 다음처럼 조회하면 `KeyError`가 발생할 수 있습니다.

```python
word_counts["자바"]
```

이를 `try-except`로 처리했습니다.

```python
try:
    count = word_counts[search_word]
    print(f"'{search_word}'의 등장 횟수: {count}회")
except KeyError:
    print(f"'{search_word}'는 분석 결과에 없는 단어입니다.")
```

따라서 존재하지 않는 단어를 검색해도 프로그램이 중단되지 않고 안내 문장이 출력됩니다.

```text
'자바'는 분석 결과에 없는 단어입니다.
```

오류가 발생했을 때는 다음 순서로 확인합니다.

```text
오류 메시지 확인
→ 오류가 발생한 코드 위치 확인
→ 변수 값 확인
→ 자료형 확인
→ 코드 수정
→ 다시 실행
```

---

# 6. 도전 문제

필수 문제 외에도 다음 기능을 넣었습니다.

- 가장 많이 등장한 단어 찾기
- 가장 적게 등장한 단어 찾기
- 특정 단어 검색하기
- 기준 횟수 이상 등장한 단어 출력하기
- 분석 결과를 텍스트 파일로 저장하기

가장 많이 등장한 단어의 예상 결과는 다음과 같습니다.

```text
가장 많이 등장한 단어: 파이썬 (3회)
```

파일 저장 기능을 실행하면 `word_frequency_result.txt`가 생성됩니다.

---

# 7. 최종 검증

Part 2에서 직접 작성한 단어 빈도 결과와 Part 3의 함수가 만든 결과가 같은지 비교합니다.

```python
basic_word_counts == function_word_counts
```

정상적으로 실행되면 다음과 같이 나옵니다.

```text
Part 2 결과와 Part 3 결과가 같은가? True
```

`True`는 두 방식의 계산 결과가 같다는 뜻입니다.

---

# 8. 확인 질문 답변

## 1) `for` 반복문은 이 프로그램에서 어떤 역할을 하나요?

리스트의 점수나 문장의 단어를 하나씩 꺼내서 같은 작업을 반복하는 역할을 합니다. 반복문이 없으면 데이터 개수만큼 같은 코드를 직접 여러 번 써야 합니다.

## 2) 딕셔너리의 Key와 Value에는 각각 무엇이 저장되나요?

Key에는 단어가 저장되고 Value에는 그 단어가 등장한 횟수가 저장됩니다. 예를 들어 `{'파이썬': 3}`에서 `파이썬`은 Key, `3`은 Value입니다.

## 3) 같은 단어가 다시 등장하면 딕셔너리 값은 어떻게 달라지나요?

이미 존재하는 단어라면 기존 Value에 1을 더합니다. 값이 2인 단어가 다시 나오면 3으로 증가합니다.

## 4) 함수를 사용하는 이유는 무엇인가요?

반복되는 코드를 하나의 기능으로 묶어 다시 사용할 수 있기 때문입니다. 코드가 정리되고 수정할 위치도 찾기 쉬워집니다.

## 5) AI를 사용했다면 AI가 제안한 코드에서 직접 확인하거나 수정한 부분은 무엇인가요?

AI를 이용해 코드 구조와 오류 가능성을 검토했습니다. 이후 `for`, `if`, 딕셔너리의 Key/Value 증가 과정, 함수의 매개변수와 반환값, `try-except`가 처리하는 오류가 무엇인지 직접 확인했고 실행 결과가 예상 결과와 같은지 검증했습니다.

---

# 9. 제출 전 체크

- [ ] `AX_ch01_python_assignment.py`를 직접 실행했다.
- [ ] 실행 오류가 없는 것을 확인했다.
- [ ] Part 1~4 출력 결과를 확인했다.
- [ ] `word_frequency_result.txt`가 생성되는 것을 확인했다.
- [ ] 코드의 `for`, `if`, `dict`, `def`, `return`, `try-except` 역할을 설명할 수 있다.

제출 페이지의 **파이썬 과제 GitHub 링크**에는 이 `python_assignment` 폴더의 GitHub 주소를 제출하면 됩니다.

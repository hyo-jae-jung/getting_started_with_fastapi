
library  
- httpx

`httpx`는 원래 **Python 라이브러리**로 설계되었지만, 최근에 **CLI 환경**에서도 사용할 수 있도록 개발되었습니다. 이를 통해 `httpie`처럼 HTTP 요청을 CLI에서 직접 실행할 수 있습니다. 다음은 `httpx`를 CLI에서 사용하는 방법입니다.

### httpx CLI 설치

`httpx` CLI 도구는 `httpx`의 기능을 명령줄에서 사용할 수 있도록 해줍니다. 이를 위해서는 `httpx`를 설치해야 합니다. `pip`를 사용하여 설치할 수 있습니다.

```bash
pip install httpx-cli
```

설치가 완료되면, `httpx` 명령을 사용할 수 있습니다.

### httpx CLI 기본 사용법

#### GET 요청

CLI에서 `GET` 요청을 보내려면 다음과 같이 명령을 입력합니다.

```bash
httpx get https://api.example.com/data
```

#### POST 요청

`POST` 요청을 보내는 방법은 다음과 같습니다. 이 경우, `--json` 옵션을 사용하여 JSON 데이터를 전송합니다.

```bash
httpx post https://api.example.com/data --json '{"name": "Alice", "email": "alice@example.com"}'
```

#### 다른 HTTP 메서드 사용하기

다른 HTTP 메서드를 사용하려면 `http`, `get`, `post`, `put`, `patch`, `delete` 등의 명령어를 사용하면 됩니다.

```bash
# PUT 요청
httpx put https://api.example.com/data/1 --json '{"name": "Bob"}'

# DELETE 요청
httpx delete https://api.example.com/data/1
```

### httpx CLI 고급 기능

#### 요청 헤더 추가

요청에 헤더를 추가하려면 `-h` 또는 `--header` 옵션을 사용합니다.

```bash
httpx get https://api.example.com/data -h "Authorization: Bearer your_token_here"
```

#### 쿼리 매개변수 추가

쿼리 매개변수를 추가하려면 `-p` 또는 `--params` 옵션을 사용합니다.

```bash
httpx get https://api.example.com/data -p "search=example" -p "page=2"
```

#### 파일 업로드

파일을 업로드하려면 `-f` 또는 `--files` 옵션을 사용합니다.

```bash
httpx post https://api.example.com/upload -f "file=@path/to/report.csv"
```

#### 타임아웃 설정

요청의 타임아웃을 설정하려면 `-t` 또는 `--timeout` 옵션을 사용합니다.

```bash
httpx get https://api.example.com/data -t 10
```

#### 재시도 설정

재시도 설정을 하려면 `-r` 또는 `--retries` 옵션을 사용합니다.

```bash
httpx get https://api.example.com/data -r 3
```

#### 출력 형식 지정

출력 형식을 지정하려면 `--pretty` 옵션을 사용합니다. 이 옵션을 사용하면 응답이 보기 좋게 포맷팅됩니다.

```bash
httpx get https://api.example.com/data --pretty
```

### 전체 옵션 목록

아래는 `httpx` CLI에서 사용할 수 있는 주요 옵션들입니다.

| 옵션           | 설명                                      |
|----------------|-------------------------------------------|
| `-h`, `--header` | 요청에 추가할 헤더를 지정합니다.                |
| `-p`, `--params` | 쿼리 매개변수를 추가합니다.                     |
| `-f`, `--files`  | 업로드할 파일을 지정합니다.                     |
| `-t`, `--timeout` | 요청 타임아웃을 설정합니다.                     |
| `-r`, `--retries` | 요청 재시도 횟수를 지정합니다.                  |
| `--json`       | JSON 형식으로 데이터를 전송합니다.               |
| `--pretty`     | 응답을 가독성 있는 형식으로 출력합니다.            |
| `--http2`      | HTTP/2 프로토콜을 사용합니다.                    |
| `--auth`       | 인증 정보를 지정합니다. `username:password` 형식  |
| `--cert`       | 클라이언트 인증서 파일을 지정합니다.               |
| `--verify`     | SSL 인증서 검증 여부를 설정합니다.                |
| `--proxy`      | 프록시 설정을 지정합니다.                        |
| `--follow`     | 리디렉션을 자동으로 따라갑니다.                    |

### 예제 사용 시나리오

#### 예제 1: 인증 헤더와 쿼리 매개변수를 사용한 GET 요청

```bash
httpx get https://api.example.com/data \
    -h "Authorization: Bearer your_token_here" \
    -p "sort=asc" \
    -p "limit=10"
```

#### 예제 2: JSON 데이터와 파일을 함께 업로드하는 POST 요청

```bash
httpx post https://api.example.com/upload \
    --json '{"title": "My Report", "description": "Annual report"}' \
    -f "file=@path/to/report.pdf"
```

### 요약

- `httpx`는 CLI 환경에서 HTTP 요청을 보낼 수 있도록 `httpx-cli`를 제공합니다.
- 다양한 HTTP 메서드와 옵션을 지원하여, `httpie`와 유사하게 명령줄에서 HTTP 요청을 간편하게 전송할 수 있습니다.
- 헤더 추가, 쿼리 매개변수 설정, 파일 업로드, 인증 처리 등 고급 기능을 포함하여 폭넓은 사용이 가능합니다.

이렇게 `httpx`를 사용하면 Python 코딩 없이도 CLI 환경에서 간편하게 HTTP 요청을 처리할 수 있습니다.



keywords
- Idempotency(멱등성)
    멱등성(Idempotency)은 컴퓨터 과학 및 수학에서 사용되는 개념으로, 연산을 반복해서 수행하더라도 결과가 변하지 않는 특성을 의미합니다. 이 개념은 특히 HTTP 메서드나 데이터베이스 연산 같은 시스템에서 중요한 역할을 합니다.

    ex) 멱등성 O : get, put, delete, select
        멱등성 X : post, insert


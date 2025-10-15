import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지의 레이아웃을 'wide'로 설정하여 넓게 표시합니다.
st.set_page_config(layout="wide")

# HTML 파일이 저장된 경로를 지정합니다.
# os.path.dirname(__file__)는 현재 app.py 파일이 있는 디렉토리를 의미합니다.
html_file_path = os.path.join(os.path.dirname(__file__), 'htmls', 'index.html')

try:
    # 지정된 경로의 HTML 파일을 열고 내용을 읽어옵니다.
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_code = f.read()
    
    # components.html을 사용하여 읽어온 HTML 코드를 Streamlit 앱에 렌더링합니다.
    # height를 넉넉하게 1200px로 설정하여 스크롤 없이 대부분의 콘텐츠가 보이도록 합니다.
    # scrolling=True 옵션으로 내용이 길어질 경우 스크롤이 가능하도록 설정합니다.
    components.html(html_code, height=1200, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: 'htmls' 폴더 안에 'index.html' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요: {html_file_path}")
except Exception as e:
    st.error(f"파일을 읽는 중 예상치 못한 오류가 발생했습니다: {e}")

```

### 실행 방법

1.  터미널(명령 프롬프트)을 엽니다.
2.  `app.py` 파일이 있는 프로젝트 폴더로 이동합니다.
3.  아래 명령어를 입력하고 실행합니다.

    ```bash
    streamlit run app.py
    

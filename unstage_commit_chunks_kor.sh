

# --- 1. 입력 값 확인 ---
# 스크립트 실행 시 2개의 인자가 주어지지 않으면 사용법을 안내하고 종료합니다.
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <chunk_size> \"<commit_message>\""
    echo "Exam : ./commit_split.sh 100 \"feat: Add initial asset chunks\""
    exit 1
fi

# UnStage로 모두 내림
git restore --staged .

# --- 2. 입력 값을 변수로 지정하고 자식 프로세스에 내보내기 ---
CHUNK_SIZE="$1"
BASE_COMMIT_MESSAGE="$2"
COUNT=1

# 현재 묶음(chunk)에 포함될 파일 목록을 임시로 저장할 파일을 만듭니다.
CHUNK_FILE=$(mktemp)

# --- 3. 카운터 초기화 ---
echo 1 > .chunk_count

# --- 4. 메인 로직 실행 ---
# 파일 목록을 읽어와서 한 줄씩 처리 (-d ''는 NULL 문자로 구분)
while IFS= read -r -d '' file; do
    # 현재 파일 경로를 임시 파일에 추가 (NULL 문자로 구분)
    printf '%s\0' "$file" >> "$CHUNK_FILE"
    
    # 임시 파일의 줄 수를 세어 묶음 크기에 도달했는지 확인
    # grep -c ''는 NULL 문자로 구분된 항목의 개수를 셉니다.
    if [[ $(grep -zc '' "$CHUNK_FILE") -ge $CHUNK_SIZE ]]; then
        echo "--- Processing and committing chunk #${COUNT} ---"
        
        # xargs가 임시 파일의 목록을 읽어 안전하게 git add 실행
        xargs -0 git add < "$CHUNK_FILE"
        git commit -m "$BASE_COMMIT_MESSAGE - (${COUNT})"
        
        # 다음 묶음을 위해 임시 파일을 비움
        > "$CHUNK_FILE"
        COUNT=$((COUNT + 1))
    fi
done < <(git diff --name-only -z; git ls-files -z --others --exclude-standard)

# --- 5. 마지막 남은 파일들 처리 ---
# 루프가 끝난 후 임시 파일에 내용이 남아있으면 마지막 묶음으로 커밋
if [[ -s "$CHUNK_FILE" ]]; then
    echo "--- Processing and committing final chunk #${COUNT} ---"
    xargs -0 git add < "$CHUNK_FILE"
    git commit -m "$BASE_COMMIT_MESSAGE - (${COUNT})"
fi

# --- 5. 임시 파일 삭제 ---
rm "$CHUNK_FILE"
rm .chunk_count

echo "--- All files have been committed successfully. ---"
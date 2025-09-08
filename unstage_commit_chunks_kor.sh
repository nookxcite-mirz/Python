#!/bin/bash

# 커밋 되돌리기
#	> git reset --soft {}

# 1. .gitattributes 파일로 프로젝트 전체 스타일 통일 (팀 프로젝트 강력 추천)
# 	# 모든 텍스트 파일의 줄바꿈을 LF로 통일
# 	* text=auto eol=lf
# 	# 특정 바이너리 파일들은 예외 처리
# 	*.png binary
# 	*.jpg binary
# 	*.uasset binary
# 	*.umap binary

# 2. Git Bash에서 실행 권한을 부여 최초 한번만
#	> chmod +x unstage_commit_chunks_kor.sh
# 3. 스크립트 실행
# 	> ./스크립트이름.sh <묶을 개수> "<커밋 메시지>"
#	> ./unstage_commit_chunks_kor.sh 10 "feat: Add Package"


# --- 1. 입력 값 확인 ---
# 스크립트 실행 시 2개의 인자가 주어지지 않으면 사용법을 안내하고 종료합니다.
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <chunk_size> \"<commit_message>\""
    echo "Exam : ./commit_chunks_msg.sh 100 \"feat: Add initial asset chunks\""
    exit 1
fi

# --- 2. 입력 값을 변수로 지정하고 자식 프로세스에 내보내기 ---
CHUNK_SIZE="$1"
BASE_COMMIT_MESSAGE="$2"
COUNT=1
# 파일 목록을 임시로 담아둘 배열 선언
file_chunk=()

# --- 3. 카운터 초기화 ---
echo 1 > .chunk_count

# --- 4. 메인 로직 실행 ---
# 파일 목록을 읽어와서 한 줄씩 처리 (-d ''는 NULL 문자로 구분)
while IFS= read -r -d '' file; do
    # 현재 파일을 배열에 추가
    file_chunk+=("$file")
    
    # 배열의 크기가 지정된 묶음 크기에 도달하면 커밋 실행
    if [ ${#file_chunk[@]} -ge $CHUNK_SIZE ]; then
        echo "--- Processing and committing chunk #${COUNT} ---"
        
        # 배열에 담긴 파일들을 git add
        git add -- "${file_chunk[@]}"
        git commit -m "$BASE_COMMIT_MESSAGE - (${COUNT})"
        
        # 다음 묶음을 위해 배열 비우기 및 카운터 증가
        file_chunk=()
        COUNT=$((COUNT + 1))
    fi
done < <(git diff --name-only -z; git ls-files -z --others --exclude-standard)

# 루프가 끝난 후 배열에 파일이 남아있으면 마지막 묶음으로 커밋
if [ ${#file_chunk[@]} -gt 0 ]; then
    echo "--- Processing and committing final chunk #${COUNT} ---"
    git add -- "${file_chunk[@]}"
    git commit -m "$BASE_COMMIT_MESSAGE - (${COUNT})"
fi

# --- 5. 임시 파일 삭제 ---
rm .chunk_count

echo "--- All files have been committed successfully. ---"
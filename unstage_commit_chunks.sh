#!/bin/bash

# 커밋 되돌리기
#	> git reset --soft {}

# UnStage <> Stage 변환
#	> git add .					/ git add <파일이름>
#	> git restore --staged .    / git restore --staged <파일이름>
# 1. Git Bash에서 실행 권한을 부여 최초 한번만
#	> chmod +x unstage_commit_chunks.sh
# 2. 스크립트 실행
# 	> ./스크립트이름.sh <묶을 개수> "<커밋 메시지>"
#	> ./unstage_commit_chunks.sh 10 "feat: Add Package"

# --- 1. 입력 값 확인 ---
# 스크립트 실행 시 2개의 인자가 주어지지 않으면 사용법을 안내하고 종료합니다.
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: $0 <chunk_size> \"<commit_message>\""
    echo "Exam : ./commit_chunks_msg.sh 100 \"feat: Add initial asset chunks\""
    exit 1
fi

# UnStage로 모두 내림
git restore --staged .

# --- 2. 입력 값을 변수로 지정하고 자식 프로세스에 내보내기 ---
# 자식 셸(sh -c)에서도 이 변수들을 사용할 수 있도록 export 합니다.
export CHUNK_SIZE="$1"
export BASE_COMMIT_MESSAGE="$2"

# --- 3. 카운터 초기화 ---
echo 1 > .chunk_count

# --- 4. 메인 로직 실행 ---
# xargs 명령어의 마지막 부분에서 "_ "$@""를 삭제했습니다
(git diff --name-only -z; git ls-files -z --others --exclude-standard) | xargs -0 -n "$CHUNK_SIZE" sh -c '
    count=$(cat .chunk_count)
    
    final_commit_message="$BASE_COMMIT_MESSAGE - (${count})"
    
    echo "--- Processing chunk #${count} (Size: $CHUNK_SIZE) ---"
    
    git add "$@"
    git commit -m "$final_commit_message"
    
    echo "Chunk #${count} successfully committed."
    
    echo $((count + 1)) > .chunk_count
'

# --- 5. 임시 파일 삭제 ---
rm .chunk_count

echo "--- All files have been committed successfully. ---"
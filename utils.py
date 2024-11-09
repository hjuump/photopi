import time

# 카운트다운 함수
def countdown(seconds, update_func=None):
    """
    지정된 시간 동안 카운트다운을 진행하고 update_func로 남은 시간을 전달.
    """
    for i in range(seconds, 0, -1):
        if update_func:
            update_func(i)  # Flask 웹 서버에 실시간 업데이트를 제공할 때 사용
        time.sleep(1)

# 입장/퇴장 상태 관리
class SessionManager:
    def __init__(self, exit_timeout=5):
        self.entry_time = None
        self.exit_timeout = exit_timeout

    def user_entered(self):
        self.entry_time = time.time()

    def user_exited(self):
        self.entry_time = None

    def is_user_present(self):
        # 사용자가 특정 시간(초과 시간) 안에 여전히 있는지 확인
        if self.entry_time and (time.time() - self.entry_time) <= self.exit_timeout:
            return True
        return False


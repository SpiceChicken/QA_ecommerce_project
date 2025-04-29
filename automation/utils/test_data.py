"""
테스트 간에 데이터를 공유하기 위한 유틸리티 모듈
"""

# 테스트 데이터 저장소
test_data = {
    "registered_email": "testuser@example.com",
    "registered_password": "test123",
    "registered_first_name": "Test",
    "registered_last_name": "User"
}

def set_registered_user(email, password, first_name=None, last_name=None):
    """등록된 사용자 정보를 저장"""
    test_data["registered_email"] = email
    test_data["registered_password"] = password
    test_data["registered_first_name"] = first_name
    test_data["registered_last_name"] = last_name

def get_registered_user():
    """등록된 사용자 정보를 반환"""
    return{
        "email": test_data["registered_email"],
        "password": test_data["registered_password"],
        "first_name": test_data["registered_first_name"],
        "last_name": test_data["registered_last_name"]
        } 

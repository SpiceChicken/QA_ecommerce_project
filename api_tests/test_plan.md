# Test Plan - E-Commerce Demo Site

## 1. 개요
- 대상 사이트: [OpenCart Demo](https://demo.opencart.com/)
- 목적: 기능 정상 동작 검증, 주요 사용자 플로우 자동화

## 2. 테스트 범위
- 회원가입
- 로그인
- 상품 검색
- 장바구니 추가/삭제
- 결제 프로세스 (Checkout)
- API 상품 조회

## 3. 제외 범위
- 관리자(Admin) 기능
- 물리적 결제/실제 금전 결제

## 4. 테스트 유형
- 기능 테스트 (Functional Testing)
- UI 테스트 (Selenium E2E)
- API 테스트 (requests 기반)
- 간단한 성능 테스트 (선택 사항)

## 5. 테스트 환경
- 브라우저: Chrome (최신 버전)
- OS: Windows 10 / Ubuntu 22.04
- Python 3.10

## 6. 리스크 및 제약사항
- Demo 사이트 특성상 데이터 초기화/리셋 가능성 있음
- 일부 기능은 의도적으로 제한되어 있을 수 있음

## 7. 테스트 일정
| 단계 | 기간 | 내용 |
|-----|-----|-----|
| 테스트 설계 | 1일 | Test Case 도출 |
| 테스트 스크립트 개발 | 2~3일 | Selenium + API 스크립트 작성 |
| 테스트 실행 및 리포트 | 1일 | 수동 + 자동화 테스트 실행 |

## 8. 산출물
- 테스트 시나리오 및 케이스
- Defect Report (버그 발견 시)
- 테스트 자동화 스크립트
- HTML 리포트 (pytest-html)

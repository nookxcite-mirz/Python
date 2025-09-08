# 웹 서버를 구축하여 "Hello, World!" 메시지를 웹 페이지에 표시합니다.
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # 성공 응답 코드
        self.send_header('Content-type', 'text/html')  # HTML 콘텐츠 타입
        self.end_headers()  # 헤더 종료
        message = "Hello, World! Python..."  # 표시할 메시지
        self.wfile.write(bytes(f"<html><head><title>Hello</title></head><body><h1>{message}</h1></body></html>", "utf8"))  # HTML 응답 작성

if __name__ == '__main__':
    server_address = ('', 8000)  # 서버 주소 (모든 인터페이스, 포트 8000)
    httpd = HTTPServer(server_address, MyHandler)  # HTTP 서버 생성
    print('서버가 실행 중입니다.')  # 서버 시작 메시지
    httpd.serve_forever()  # 서버가 계속 실행되도록 함

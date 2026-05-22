"""
带 CORS 头的本地视频文件服务器
用法: python cors_server.py
"""
import http.server
import sys

PORT = 8080

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

    def handle_error(self, request, client_address):
        # ConnectionResetError (WinError 10054) 是客户端正常断开连接，不是错误
        # 视频播放完毕或用户关闭播放器时会触发，可以安全忽略
        exc_type = sys.exc_info()[0]
        if exc_type is ConnectionResetError:
            return
        super().handle_error(request, client_address)

if __name__ == '__main__':
    with http.server.HTTPServer(('', PORT), CORSRequestHandler) as httpd:
        print(f"Video server started: http://localhost:{PORT}")
        print(f"Example: http://localhost:{PORT}/videos/1.mp4")
        print(f"Press Ctrl+C to stop\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

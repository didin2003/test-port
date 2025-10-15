# myapp/middleware.py
import socket
from django.shortcuts import render

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = ["10.10.10.74"]
        self.restricted_paths = ["/metrics"]

    def __call__(self, request):
        if request.path in self.restricted_paths:
            client_ip = self.get_client_ip(request) 
            print(f"Client IP: {client_ip}")  # Debugging line
            if client_ip not in self.allowed_ips:
                from django.http import HttpResponseForbidden
                return render(request, "metrices.html")
        return self.get_response(request)

    def get_client_ip(self, request):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
        # Connect to a non-local address (no data sent)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
            return ip
from django.shortcuts import render, redirect
from django.http import HttpResponse
import qrcode
from io import BytesIO
from .models import QRCode

def generate_qr(request):
    if request.method == 'POST':
        data = request.POST['data']
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        buffer.seek(0)

        qr_code = QRCode.objects.create(data=data)
        return HttpResponse(buffer, content_type='image/png')

    return render(request, 'qrs/generate_qr.html')
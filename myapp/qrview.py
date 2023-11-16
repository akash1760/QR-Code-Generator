from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
import png


def index(request): 
    context = {} 
    if request.method == "POST": 
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""),
        image_factory=factory, box_size=20) 
        stream = BytesIO() 
        img.save(stream) 
        context["svg"] = stream.getvalue().decode()
        name="Qrcode.jpg"
        path="C:\\Users\\Dell\\OneDrive\\Desktop\\Project_Output\\"
        img.save(path+name)

   
    return render(request, "home1.html", context=context)

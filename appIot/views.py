from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import ButtonForm1,ButtonForm2,sliderForm1,sliderForm2


# Create your views here.

def button_view1(request):
    response_data = {'value': 0} # khởi tạo giá trị ban đầu của  button là 0
    form_button1 = ButtonForm1() # khởi tạo form_button1 trước khi sử dụng
    if request.method == 'POST':
        
        form_button1 = ButtonForm1(request.POST)  # Tạo một instance của form từ dữ liệu POST
        if form_button1.is_valid():
            # Form hợp lệ, thực hiện các xử lý ở đây (nếu cần)
            response_data ['value'] = 1 
            return JsonResponse(response_data)
        else:
            form_button1 = ButtonForm1()  # Tạo một instance của form rỗng

    return render(request, 'green/index.html', {'form':form_button1})
    
def button_view2(request):
    response_data = {'value': 0} # khởi tạo giá trị ban đầu của  button là 0
    form_button2 = ButtonForm2() # khởi tạo form_button1 trước khi sử dụng
    if request.method == 'POST':
        
        form_button2 = ButtonForm2(request.POST)  # Tạo một instance của form từ dữ liệu POST
        if form_button2.is_valid():
            # Form hợp lệ, thực hiện các xử lý ở đây (nếu cần)
            response_data ['value'] = 1 
            return JsonResponse(response_data)
        else:
            form_button2 = ButtonForm2()  # Tạo một instance của form rỗng

    return render(request, 'green/index.html', {'form1':form_button2})

def slider_view1(request):
    form_slider1 = slider_form1() # khởi tạo form_slider1 trước khi sử dụng
    if request.method == 'POST':
        form_slider1 = slider_form1(request.POST)
        if form_slider1.is_valid():
            slider_value1 = form.cleaned_data['slider1']
            response_data ={'message': f'Slider value received: {slider_value1}'}
            return JsonResponse(request_data)
        else:
            form_slider1 = slider_form1()
    return render(request,'green/index.html',{'form2' : form_slider1})

def slider_view2(request):
    form_slider2 = slider_form2() # khởi tạo form_slider1 trước khi sử dụng
    if request.method == 'POST':
        form_slider2 = slider_form2(request.POST)
        if form_slider1.is_valid():
            slider_value2 = form.cleaned_data['slider2']
            response_data ={'message': f'Slider value received: {slider_value2}'}
            return JsonResponse(request_data)
        else:
            form_slider2 = slider_form2()
    return render(request,'green/index.html',{'form3' : form_slider2})

def get_humidity_data(request):
    # Trong thực tế, bạn sẽ lấy dữ liệu độ ẩm từ máy chủ thời gian thực
    # Đoạn mã dưới đây chỉ là ví dụ cố định giá trị để minh họa
    humidity_data = {'humidity': '60.5'}  # Giả định độ ẩm là 60.5%
    return JsonResponse(humidity_data)
    return render(request,'green/index.html',{'form4' : humidity_data})
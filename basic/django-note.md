# Tài liệu học chuẩn 
- https://docs.djangoproject.com/en/4.0/

# Những thành phần chính của django 
- view 
- model
- admin 
- url 
- templates 
- Static

```
- urls->views -> templates

views:
  - là phần xử lí logic giữa model và template, urls thông qua giao thức http
template:
  - hiện thị dữ liệu thông qua đối tượng context
model: tương tác dữ liệu trong database
urls: đường dẫn đến trang web, định tuyến logic của view
admin: quản lý model
static: nơi lưu trữ các file css, js
```

Những thành phần này liên kết với nhau như thế nào ? 

- settings : cấu hình của hệ thống 
- manage.py: chạy những lệnh của hệ thống ví dụ: tạo app, runserver, ... 
## Bài tập
- Thêm giao diện, html, css cho trang web ví dụ 
- https://preview.tabler.io/layout-vertical.html
- https://adminlte.io/
- Nhập dữ liệu: Tạo form để nhập dữ liệu(submit form, post, get, render, redirct `return redirect('name_of_url')`

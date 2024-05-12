- Khởi nguyên dự án
1. Cài Django: pip install django
2. Tạo project Django: django-admin startproject lthdBCCK

- Triển khai app calculator
1. Vào terminal của dự án Django gốc, tạo app: python manage.py startapp calculator
2. Build view
3. Build template
4. Cấu hình URL, cầu hình từ ứng dụng gốc tới app con.
5. Đăng ký app con calculator trong settings.py, ở INSTALLED_APPS
6. Run server: python manage.py runserver

- Kết nối CSDL MySQL
1. Cài MySQL Adapter: pip install mysqlclient
2. Cấu hình Database trong settings.py
3. Định nghĩa các model
4. Tạo database trong database workbench
5. Tạo migration và migrate:
python manage.py makemigrations
python manage.py migrate

- Tạo ứng dụng CRUD zui zẻ zui zẻ:
1. Tạo app con mới
2. Thêm model.
3. Thểm form.
4. Viết các hàm trong view ứng với CRUD.
5. Viết template.
6. Hiệu chỉnh URL.

- Thêm login/logout/register nhờ django.contrib.auth
Thao tác như cũ.
Có khai báo thêm cặp biến: 
LOGIN_REDIRECT_URL 
LOGOUT_REDIRECT_URL
trong settings.py
Ngoài ra chỉnh hàm view có sẵn tương ứng theo nhu cầu.

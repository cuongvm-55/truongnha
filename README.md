Kiểm thử Trường Nhà - Nhóm 2
============
Kiểm thử chức năng ở truongnha.com

## Các sinh viên tham gia kiểm thử ##

1. Lò May Thy (Nhóm trưởng)   MSSV: 10020354
2. Bùi Đức Tài                MSSV:
3. Vy Mạnh Cường              MSSV: 10020045

## Công cụ kiểm thử ##
Robot Framework - robotframework.org. Thư viện ```selenium2library```.\n
Thư viện tự định nghĩa ```ReusableModule.py```

## Hướng dẫn kiểm thử ##
Sau khi cài đặt Robot Framework, trên màn hình Command Line, gõ lệnh: ``` pybot <thư mục đặt tài liệu> ``` để chạy các ca kiểm thử. Ví dụ: ``` pybot nhapdiem_tests ```.

## Các chức năng được kiểm thử (3) ##
1. Nhập điểm ``` nhapdiem_tests ```
2. Nhập hạnh kiểm ``` nhaphanhkiem_tests ```
3. Xếp loại, xét lên lớp ``` xeploai_xetlenlop_tests ```

## Các ca kiểm thử đã viết ##
I - Nhập điểm (5/5)
1. Kiểm thử một hàng dữ liệu PASSED
2. Kiểm thử một cột dữ liệu PASSED
3. Kiểm thử một ô dữ liệu PASSED
4. Nhập từ Excel (kiểm thử bằng tay) PASSED
5. Xuất ra Excel (kiểm thử bằng tay) PASSED

II - Nhập hạnh kiểm (/)

II - Xếp loại, xét lên lớp (/)

## Các lỗi phát hiện mà không thể kiểm thử ##

## Những khó khăn khi thực hiện ##
- Không thể kiểm thử được chức năng nhập/xuất dữ liệu từ/ra file Excel vì sự hạn chế của công cụ kiểm thử.
- Gặp khó khăn khi tìm kiếm các elements phục vụ kiểm thử.

# Các góp ý cho hệ thống ##
Với những gì đã làm, nhóm 2 xin có một số góp ý cho hệ thống Truongnha.com
- Cần refactoring lại source code cụ thể là việc đặt tên biến để khâu viết kiểm thử được dễ dàng hơn.

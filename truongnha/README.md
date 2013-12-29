Kiểm thử Trường Nhà - Nhóm 2
============
Kiểm thử chức năng ở truongnha.com

## Các sinh viên tham gia kiểm thử ##

1. Lò May Thy (Nhóm trưởng)   MSSV: 10020354
2. Bùi Đức Tài                MSSV: 10020302
3. Vy Mạnh Cường              MSSV: 10020045

## Công cụ kiểm thử ##
Robot Framework - robotframework.org.

Thư viện ```selenium2library```.

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

1. Kiểm thử nhập hạnh kiểm đúng chuẩn hiển thị(T,K,TB,Y)              PASSED
2. Kiểm thử nhập hạnh kiểm đúng nhưng sai chuẩn hiển thị(t,k,b,y,...) PASSED
3. Kiểm thử nhập hạnh kiểm không đúng       PASSED
4. Kiểm thử chức năng xem hạnh kiểm theo lớp học PASSED
5. Kiểm thử chức năng import File(kiểm thử bằng tay)  PASSED
6. Kiểm thử chức năng export File(kiểm thử bằng tay)  PASSED

III - Xếp loại, xét lên lớp (/20)

1. Kiểm thử Xét học lực (kiểm các điều kiện từ học lực Giỏi trở xuống đến học lực Kém) (12 ca kiểm thử)

    1.1. Học lực Giỏi (1 ca kiểm thử)
    
    - (Trung bình chung) TB >= 8.0, TB Văn hoặc TB Toán >= 8.0, không có môn nào TB <= 6.5, điểm Thể dục điểm Đạt
        
    1.2. Học lực Khá (3 ca kiểm thử)
    
    - 8.0 <= TB, 6.5 <= TB Văn và TB Toán < 8.0, không có môn nào TB <= 5.0, điểm Thể dục điểm Đạt
    - 8.0 <= TB, TB Văn hoặc TB Toán >= 6.5, có 1 môn 5.0 <= TB <= 6.5, điểm Thể dục điểm Đạt
    - 6.5 <= TB < 8.0, TB Văn hoặc TB Toán >= 6.5, không có môn nào TB <= 5.0, điểm Thể dục điểm Đạt
    
    1.3. Học lực Trung Bình (3 ca kiểm thử)
    
    - 6.5 <= TB, 5.0 <= TB Toán hoặc TB Văn < 6.5, không có môn nào TB <= 3.5, điểm Thể dục điểm Đạt
    - 6.5 <= TB, TB Toán hoặc TB Văn >= 5.0, có 1 môn 3.5 <= TB < 5.0, điểm Thể dục điểm Đạt
    - 5.0 <= TB < 6.5, TB Toán hoặc TB Văn >= 5.0, không có môn nào TB <= 3.5, điểm Thể dục điểm Đạt
    
    1.4. Học lực Yếu (3 ca kiểm thử)
    
    - 5.0 <= TB, có 1 môn 2.0 <= TB < 3.5
    - 5.0 <= TB, không có môn nào TB <= 2.0, điểm Thể dục điểm Chưa Đạt
    - 3.5 <= TB < 5.0, không có môn nào TB <= 2.0
    
    1.5. Học lực Kém (2 ca kiểm thử)
    
    - 3.5 > TB
    - có 1 môn TB < 2.0, TB chung tùy ý
    
2. Kiểm thử xét lên lớp (Kiểm thử xét danh hiệu) (8 ca kiểm thử)

    2.1. Học sinh Giỏi (1 ca kiểm thử)
    
    - Học lực Giỏi, Hạnh kiểm Tốt
    
    2.2. Học sinh Tiên Tiến (2 ca kiểm thử)
    
    - Học lực Giỏi, Hạnh kiểm Khá
    - Học lực Khá, Hạnh kiểm Tốt
    - Học lực Khá, Hạnh kiểm Khá
    
    2.3. Không xếp loại danh hiệu (5 ca kiểm thử)
    
    - Hạnh kiểm Trung Bình
    - Hạnh kiểm Yếu
    - Học lực Trung Bình
    - Học lực Yếu
    - Học lực Kém
    
## Các lỗi phát hiện mà không thể kiểm thử ##

## Những khó khăn khi thực hiện ##
- Không thể kiểm thử được chức năng nhập/xuất dữ liệu từ/ra file Excel vì sự hạn chế của công cụ kiểm thử.
- Gặp khó khăn khi tìm kiếm các elements phục vụ kiểm thử.
- Đôi khi WebDriver không tìm thấy các phần tử của trang web (button, link, ...)
- Khó khăn trong việc thao tác với các giá trị Tiếng Việt (UTF-8)

# Các góp ý cho hệ thống ##
Với những gì đã làm, nhóm 2 xin có một số góp ý cho hệ thống Truongnha.com
- Cần refactoring lại source code cụ thể là việc đặt tên biến để khâu viết kiểm thử được dễ dàng hơn.

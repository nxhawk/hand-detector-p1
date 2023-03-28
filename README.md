# Cơ bản về opencv và mediapipe

![image](https://user-images.githubusercontent.com/92797788/228290847-c9aeda86-ff51-475a-a13b-eb37b51f8846.png)

## I. Trục tọa độ trong opencv
- Gốc tọa độ ảnh đặt ở góc phía trên bên trái.
- Trục nằm dọc là trục y - tương ứng với chiều cao ảnh.
- Trục nằm ngang là trục x - tương ứng với chiều rộng ảnh.
- Trục z là trục chiều sâu (bạn tưởng tượng nó tương tự khối lập phương 3D đã từng học ở lớp 12 á) - tương ứng với kênh màu ảnh.


Ảnh minh họa tọa độ các điểm trong ảnh (ma trận 2D) có kích thước 7x11 (height x width):

![image](https://user-images.githubusercontent.com/92797788/228284950-ed186100-e697-47f0-adb7-53fb12e3b8f2.png)

## II. Màu trong opencv
- Ảnh màu được biểu diễn bằng cách pha ba màu cơ bản là Đỏ (Red), Xanh Lá (Green) và Xanh Dương (Blue) - còn gọi là hệ màu RGB. Ở mỗi kênh màu đỏ hoặc xanh dương hoặc xanh lá được biểu diễn mức sáng trong miền giá trị 0-255. Một bộ giá trị 3 kênh RGB (trong lập trình gọi là tuple) biểu diễn một sắc màu. Như vậy, tổng cộng ta sẽ có tổ hợp của 255 x 255 x 255 = 16,581,375 - 16 triệu màu!~
- Do đó, đối với ảnh màu ta cần 3 kênh màu để lưu trữ. Thứ tự kênh màu trong `OpenCV` được sắp theo `BGR` (Blue, Green, Red). Lưu ý: màu đen được biểu diễn theo 3 kênh sẽ là (0, 0, 0), màu trắng là (255, 255, 255), và các mức xám sẽ được biểu diễn là (K, K, K) với giá trị K nằm trong đoạn (0, 255).


## III. Đôi chút về mediapipe
- Một cách đơn giản để phát hiện các node trên bàn tay như hình dưới đây:

![image](https://user-images.githubusercontent.com/92797788/228286420-77977a73-70bc-4428-a715-eec96edf4a63.png)

- Dựa vào vị trí của node này so với các node khác bạn có thể làm nhiều điều thú vị với nó. Cụ thể một ví dụ đơn giản là khi so sánh tọa độ y của node số 8 và node số 6 bạn sẽ biết khi nào ngón trỏ gập xuống hay không (tổng quát dùng để phát hiện bàn tay đang biểu thị số mấy).
- Trong file [hand.py](https://github.com/nxhawk/hand-detector-p1/blob/master/hand.py) sẽ chứa code cơ bản cho việc dùng module `mediapipe`, với hàm `findHands` để phát hiện bàn tay trong ảnh và hàm `findPosition` để phát hiện tọa độ các node ngón tay lưu dưới dạng sau: [node, x, y] (với node là số thứ tự node như hình minh họa, (x, y) là tọa độ theo opencv screen)

## IV. Tài liệu tham khảo
- [Opencv modules](https://docs.opencv.org/4.x/)
- [Opencv và xử lý ảnh](https://minhng.info/tutorials/opencv-cau-truc-du-lieu-anh.html)
- [Use mediapipe](https://google.github.io/mediapipe/solutions/hands.html) 

![image](https://user-images.githubusercontent.com/92797788/228291682-d683aff0-404f-46b6-a6b9-66e16c197df5.png)












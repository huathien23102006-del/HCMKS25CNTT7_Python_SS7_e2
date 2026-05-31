
# 1 Vì sao transaction.strip() không làm thay đổi trực tiếp chuỗi ban đầu?
# 2 Chuỗi giao dịch thực tế được phân tách bằng ký tự nào?
# 3 Vì sao transaction.split("-") là sai?
# 4 Sau khi tách bằng sai delimiter, dữ liệu trong parts bị lệch như thế nào?
# 5 Vì sao cần .strip() lại từng phần sau khi split()?
# 6 Vì sao cần chuyển amount từ chuỗi sang số trước khi định dạng tiền?

# 1 vì chuỗi (string) trong Python là immutable (không thể thay đổi trực tiếp), strip() chỉ tạo ra chuỗi mới đã xóa khoảng trắng, không sửa chuỗi cũ.
# 2 chuỗi giao dịch được phân tách bằng ký tự: |
# 3 Vì chuỗi không dùng dấu - để phân tách dữ liệu.
# 4 Toàn bộ chuỗi nằm trong 1 phần tử duy nhất, không tách được tên, trạng thái và số tiền.
# 5 Vì sau khi tách vẫn còn khoảng trắng dư.
# 6 Vì dữ liệu tách ra từ split() luôn là kiểu str do đó nếu muốn định dạng số tiền phải đổi kiểu dữ liệu của biến lưu trữ số tiền

transaction = " nguyEN vAn a | PYTHON-01 | 15000000 | paid "
transaction = transaction.strip()
name, subject, money, status = transaction.split("|")

name = name.strip()
name = name.title()

subject = subject.strip()
subject = subject.upper()

money = int(money)
format_money = f"{money:,}"

status = status.strip()
status = status.upper()

print("Học Viên: ",name)
print("Khóa học: ",subject)
print("Số tiền: ",format_money,"VND")
print("Trạng thái: ",status)
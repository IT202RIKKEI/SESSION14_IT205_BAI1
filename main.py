# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    """
    Tính tổng giá trị đơn hàng sau khi giảm giá và cộng phí ship.
    """
    # Logic: Giá đã giảm = price * (1 - discount)
    total = price * (1 - discount) + shipping_fee
    
    return total

# Sửa lại: Truyền đúng tên tham số vào giá trị tương ứng
# price=100000, discount=0.1, shipping_fee=15000
order_total = calculate_final_price(price=100000, discount=0.1, shipping_fee=15000)

# Hệ thống cộng thêm 5000 phí đóng gói
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)
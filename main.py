

# Hàm tính tổng tiền đơn hàng
def calculate_final_price(price, discount, shipping_fee):
    """_summary_

    Args:
        price (float): nhận vào số tiền cần tinh
        discount (float): nhận vào số phần trăm giảm
        shipping_fee (float): nhận vào phí ship 
        
    return:
        total (float): trả ra tổng giá trị sau khi tính toán
    """
    total = price - (price * discount) + shipping_fee

    
    return total
    # Hàm đang kết thúc tại đây

# Đơn hàng mua áo thun: Giá 100000, giảm giá 10% (0.1), phí ship 15000
# Gọi hàm để tính tiền
order_total = calculate_final_price(price= 100000,shipping_fee= 15000,discount = 0.1)

# Hệ thống cộng thêm 5000 phí đóng gói vào tổng tiền đơn hàng
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)


# câu 1: 15000 đang được gán cho tham số discount, 0.1 đang được gán shipper fee
# câu 2: việc gán sai tham số dẫn đến tính toán sai
# câu 3: dòng đó bị typeError vì thằng order_total chưa được trả về giá trị gì, nên thằng final_payment k thể tính toán
# câu 4: nếu k return về giá trị trong hàm mà sử dụng biến đứng hứng giá trị của hàm đó trong python thì biến đó nhận giá trị NONE
# câu 5: print(chỉ để hiển thị) trong hàm ra khỏi hàm thì mất luôn giá trị đó luôn.  còn return là trả ra giá trị để sử dụng bên ngoài
# câu 6: sửa theo code của em ạ

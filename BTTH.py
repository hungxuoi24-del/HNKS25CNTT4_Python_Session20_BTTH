import logging
logging.basicConfig(
    level = logging.INFO,
    filename = "arena_tickets.log",
    filemode = "a",
    format ="%(asctime)s - %(levelname)s - %(message)s"
)


ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]


# CHỨC NĂNG 1: Xem danh sách vé đã bán
def display_tickets(tickets):
    if not tickets:
        print("\nHiện chưa có vé nào trong hệ thống.")
        return

    logging.info("User viewed ticket list.")
    print("\n--- DANH SÁCH VÉ ---")
    print(f"{'Mã Vé':<6} | {'Tên Khách Hàng':<15} | {'Giá Vé':<7} | {'Chỗ Ngồi':<8} | Trạng Thái")
    print("-" * 59)

    for ticket in tickets:
        try:
            status = ticket["status"]

            if status == "Cancelled":
                status += " [ĐÃ HỦY]"
            
            area, seat_number = ticket["seat"]
            seat = f"{area}-{seat_number}"
            
            print(f"{ticket["ticket_id"]:<6} | {ticket["buyer_name"]:<15} | {ticket["price"]:<7} | {seat:<8} | {status}")
    

        except KeyError as e:
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            logging.error(f"Missing key while displaying ticket: {e}")


# CHỨC NĂNG 2: Đặt vé mới
def book_ticket(tickets):
    print("\n--- ĐẶT VÉ MỚI ---")
    # Mã vé
    while True:
        ticket_id = input("Nhập mã vé: ").strip().upper()
        if not ticket_id:
            print("Mã vé không được để trống!")
        else:
            break
    
    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return
    
    # Tên khách hàng
    while True:
        buyer_name = input("Nhập tên khách hàng: ").strip().title()
        if not buyer_name:
            print("Tên khách hàng không được để trống!")
        else:
            break
    
    # Giá vé
    while True:
        try:
            price = float(input("Nhập giá vé: "))
            if price <= 0:
                print("Giá vé phải lớn hơn 0. Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("Giá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

    # khu vực ghế
    while True:
        area = input("Nhập khu vực ghế: ").strip().upper()
        if not area:
            print("Khu vực ghế không được để trống!")
        elif not area.isalpha():
            print("Khu vực ghế phải là chữ. Vui lòng nhập lại.")
        else:
            break
    
    # Số ghế
    while True:
        try:
            seat_number = int(input("Nhập số ghế: "))
            if seat_number <= 0:
                print("Số ghế phải lớn hơn 0. Vui lòng nhập lại.")
            else:
                break
        except ValueError:
            print("Số ghế phải là số. Vui lòng nhập lại.")

    seat = (area, seat_number)

    new_tiket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": seat
    }

    tickets.append(new_tiket)
    print(f"Thành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")


# CHỨC NĂNG 3: Đổi chỗ ngồi (Cập nhật vé)
def change_seat(tickets):
    print("\n--- ĐỔI CHỖ NGỒI ---")
    # Nhập mã vé 
    while True:
        ticket_id = input("Nhập mã vé cần đổi: ").strip().upper()
        if not ticket_id:
            print("Mã vé cần đổi không được để trống!")
        else:
            break
    
    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:
            # Nhập khu vực ghế
            while True:
                new_area = input("Nhập khu vực ghế mới: ").strip().upper()
                if not new_area:
                    print("Khu vực ghế mới không được để trống!")
                elif not new_area.isalpha():
                    print("Khu vực ghế phải là chữ. Vui lòng nhập lại.")
                else:
                    break
            
            # Nhập số ghế
            while True:
                try:
                    new_seat_number = int(input("Nhập số ghế mới: "))
                    if new_seat_number <= 0:
                        print("Số ghế phải lớn hơn 0. Vui lòng nhập lại.")
                    else:
                        break
                except ValueError:
                    print("Số ghế phải là số nguyên. Vui lòng nhập lại.")
            
            ticket["seat"] = (new_area, new_seat_number)
            seat = f"{new_area}-{new_seat_number}"
            print(f"Thành công: Đã đổi chỗ vé {ticket_id} sang {seat}.")
            logging.info(f"Seat changed for ticket {ticket_id} to {seat}")
            break

    # Trường hợp không tìm thấy
    else:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")


# CHỨC NĂNG 4: Hủy vé
def cancel_ticket(tickets):
    print("\n--- HỦY VÉ ---")
    # Nhập mã vé
    while True:
        ticket_id = input("Nhập mã vé cần hủy: ").strip().upper()
        if not ticket_id:
            print("Mã vé cần hủy không được để trống!")
        else:
            break
    
    for ticket in tickets:
        if ticket_id == ticket["ticket_id"]:

            # Nếu vé có sẵn trạng thái "Cancelled"
            if ticket["status"] == "Cancelled":
                print(f"Vé {ticket_id} đã ở trạng thái Cancelled trước đó.")
                return
            
            # Trường tìm thấy và hủy thành công
            ticket["status"] = "Cancelled"
            print(f"Thành công: Vé {ticket_id} đã được hủy.")
            logging.warning(f"Ticket {ticket_id} has been cancelled.")
            return

    # Trường hợp không tìm thấy    
    else:
        print(f"Không tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")


def calculate_total_revenue(ticket_list):
    total = 0.0

    for ticket in ticket_list:
        if ticket["status"] == "Booked":
            total += ticket["price"]

    return total

# CHỨC NĂNG 5: Báo cáo doanh thu (Bài toán Debugging)
def calculate_revenue(tickets):
    print("\n--- BÁO CÁO DOANH THU ---")

    total_revenue = 0
    booked_count = 0
    cancelled_count = 0

    try:
        total_revenue = calculate_total_revenue(tickets)

        for ticket in tickets:
            if ticket["status"] == "Booked":
                booked_count += 1
            elif ticket["status"] == "Cancelled":
                cancelled_count += 1
    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        logging.error(f"Missing key while calculating revenue: {e}")

        print("Tổng doanh thu hợp lệ: 0.0")
        return
    
    print(f"Tổng số vé đã đặt: {booked_count}")
    print(f"Tổng số vé đã hủy: {cancelled_count}")
    print(f"Tổng doanh thu hợp lệ: {total_revenue}")

    logging.info(f"Revenue report generated. Total: {total_revenue}")


def main():
    choice = ""
    while choice != "6":
        print()
        print("=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi (Cập nhật vé)")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")
        print("======================================== ")
        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                cancel_ticket(ticket_db)
            case "5":
                calculate_revenue(ticket_db)
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports. ")
                logging.info("Ticket management system closed.")
            case _:
                print("Lựa chọn không hợp lệ! ")

if __name__ == "__main__":
    main()
import dns.resolver
import re

def validate_email_domain(email):
    """
    ตรวจสอบความถูกต้องของโดเมนในอีเมล โดยเช็ค DNS Records (MX และ A)

    Args:
        email (str): อีเมลที่ต้องการตรวจสอบ

    Returns:
        tuple: (is_valid, message)
               is_valid (bool): True ถ้าโดเมนถูกต้อง, False ถ้าไม่ถูกต้อง
               message (str): ข้อความอธิบายผลลัพธ์
    """
    
    # 1. ตรวจสอบรูปแบบอีเมลเบื้องต้น (Syntax Validation)
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return (False, "รูปแบบอีเมลไม่ถูกต้อง (Invalid syntax)")

    # 2. แยกชื่อโดเมนออกจากอีเมล
    try:
        domain = email.split('@')[1]
    except IndexError:
        return (False, "ไม่สามารถแยกชื่อโดเมนได้")

    # 3. ตรวจสอบ MX Record
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            # ถ้าพบ MX record อย่างน้อยหนึ่งรายการ ถือว่าโดเมนถูกต้อง
            # สามารถดูรายการเซิร์ฟเวอร์ได้จาก mx_records.response.answer
            print(f"พบ MX records สำหรับโดเมน '{domain}': {[str(r.exchange) for r in mx_records]}")
            return (True, f"โดเมน '{domain}' ถูกต้องและมี MX record")
            
    except dns.resolver.NoAnswer:
        # ไม่พบ MX record แต่โดเมนอาจจะยังมีอยู่
        print(f"ไม่พบ MX record สำหรับโดเมน '{domain}', กำลังตรวจสอบ A record...")
        pass # ไปตรวจสอบ A record ต่อ
    except dns.resolver.NXDOMAIN:
        # NXDOMAIN หมายถึง Non-Existent Domain คือโดเมนนี้ไม่มีอยู่จริงในระบบ DNS
        return (False, f"โดเมน '{domain}' ไม่มีอยู่จริง (NXDOMAIN)")
    except dns.exception.Timeout:
        # การ query ใช้เวลานานเกินไป
        return (False, f"การตรวจสอบโดเมน '{domain}' หมดเวลา (Timeout)")
    except Exception as e:
        # จัดการข้อผิดพลาดอื่นๆ ที่อาจเกิดขึ้น
        return (False, f"เกิดข้อผิดพลาดในการตรวจสอบ MX record: {e}")

    # 4. ตรวจสอบ A Record (เป็น Fallback กรณีไม่พบ MX Record)
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        if a_records:
            # ถ้าพบ A record ถือว่าโดเมนมีอยู่จริง แต่อาจจะรับอีเมลไม่ได้
            print(f"พบ A records สำหรับโดเมน '{domain}': {[str(r) for r in a_records]}")
            return (True, f"โดเมน '{domain}' ถูกต้อง (มี A record แต่ไม่มี MX record)")
            
    except dns.resolver.NoAnswer:
        # ไม่พบทั้ง MX และ A records
        return (False, f"โดเมน '{domain}' ไม่มีทั้ง MX และ A records")
    except dns.resolver.NXDOMAIN:
        # ควรจะถูกดักจับไปแล้วในส่วนของ MX แต่ใส่ไว้อีกครั้งเพื่อความปลอดภัย
        return (False, f"โดเมน '{domain}' ไม่มีอยู่จริง (NXDOMAIN)")
    except dns.exception.Timeout:
        return (False, f"การตรวจสอบโดเมน '{domain}' หมดเวลา (Timeout)")
    except Exception as e:
        return (False, f"เกิดข้อผิดพลาดในการตรวจสอบ A record: {e}")
        
    # หากโค้ดมาถึงตรงนี้โดยไม่มีเงื่อนไขใดเป็นจริง (ซึ่งไม่น่าจะเกิดขึ้น)
    return (False, "ไม่สามารถตรวจสอบโดเมนได้")


# # --- ตัวอย่างการใช้งาน ---

# # อีเมลที่ถูกต้องและมี MX Record
# email1 = "contact@google.com"
# is_valid1, message1 = validate_email_domain(email1)
# print(f"Email: {email1}\nResult: {is_valid1}, Message: {message1}\n" + "="*30)

# # อีเมลที่ถูกต้อง แต่โดเมนไม่มี MX record (แต่มี A record) - หายากในปัจจุบัน
# # ตัวอย่างสมมติ: สมมติว่า example.org มีแต่เว็บเซิร์ฟเวอร์
# email2 = "user@example.org"
# is_valid2, message2 = validate_email_domain(email2)
# print(f"Email: {email2}\nResult: {is_valid2}, Message: {message2}\n" + "="*30)

# # อีเมลที่โดเมนไม่มีอยู่จริง
# email3 = "test@this-domain-does-not-exist-12345.com"
# is_valid3, message3 = validate_email_domain(email3)
# print(f"Email: {email3}\nResult: {is_valid3}, Message: {message3}\n" + "="*30)

# # อีเมลที่รูปแบบผิด
# email4 = "invalid-email.com"
# is_valid4, message4 = validate_email_domain(email4)
# print(f"Email: {email4}\nResult: {is_valid4}, Message: {message4}\n" + "="*30)

email5 = "purim09966@gmail.comom"
is_valid5, message5 = validate_email_domain(email5)
print(f"Email: {email5}\nResult: {is_valid5}, Message: {message5}\n" + "="*30)
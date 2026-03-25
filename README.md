# Track 1: The "History & Priority" Processor
โปรแกรมจำลองระบบลงทะเบียนเรียนแบบ Command Line Interface (CLI) พัฒนาด้วยภาษา Python โดยประยุกต์ใช้โครงสร้างข้อมูล (Data Structures) ที่หลากหลายเพื่อเพิ่มประสิทธิภาพในการทำงาน โปรเจกต์นี้เป็นส่วนหนึ่งของการศึกษาวิชา Data Structures and Algorithms


## Features
- **Search & Add Courses:** ค้นหาและเพิ่มรายวิชาด้วยรหัสวิชา (Course Code) อย่างรวดเร็ว
- **Section Handling:** รองรับรายวิชาที่มีหลายกลุ่มเรียน (Sections) โดยระบบจะดึงข้อมูลกลุ่มเรียนแรกให้อัตโนมัติเพื่อความรวดเร็ว
- **Duplicate Prevention:** ระบบป้องกันการลงทะเบียนวิชาเดิมซ้ำซ้อน
- **Undo System:** สามารถยกเลิกการเพิ่มรายวิชาล่าสุดได้ (รองรับการย้อนหลังสูงสุด 3 รายการ)
- **Smart Queue Processing:** ระบบจัดเรียงลำดับวิชาที่ลงทะเบียน โดยให้ความสำคัญกับวิชาเรียนทฤษฎี (Sec/Lecture) ขึ้นก่อนวิชาปฏิบัติการ (Lab) อัตโนมัติ
- **Credit Calculation:** คำนวณและสรุปผลหน่วยกิตรวมทั้งหมดที่ลงทะเบียนสำเร็จ

---

## How to Run
1. ติดตั้ง **Python 3.x**
2. เตรียมไฟล์ฐานข้อมูลรายวิชา `CprE_Subject.csv` วางอยู่ในโฟลเดอร์เดียวกับ `main.py` โดยมีโครงสร้างคอลัมน์: `Code, Name, Type, Credit, Semester, Lecturer`
3. เปิด Terminal หรือ Command Prompt นำทางมาที่โฟลเดอร์โปรเจกต์ แล้วรันคำสั่ง:
```bash
python main.py

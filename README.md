# Track 1: The "History & Priority" Processor
โปรแกรมจำลองระบบลงทะเบียนเรียนแบบ Command Line Interface (CLI) พัฒนาด้วยภาษา Python โดยประยุกต์ใช้โครงสร้างข้อมูล (Data Structures) ที่หลากหลายเพื่อเพิ่มประสิทธิภาพในการทำงาน โปรเจกต์นี้เป็นส่วนหนึ่งของการศึกษาวิชา Data Structures and Algorithms


## Features
- **Search & Add Courses:** ค้นหาและเพิ่มรายวิชาด้วยรหัสวิชา (Course Code)
- **Section Selection:** รองรับรายวิชาที่มีหลายกลุ่มเรียน (Sections) โดยมีระบบเมนูให้ผู้ใช้เลือก
- **Duplicate Prevention:** ระบบป้องกันการลงทะเบียนวิชาเดิมซ้ำซ้อน
- **Undo System:** สามารถยกเลิกการเพิ่มรายวิชาล่าสุดได้ (รองรับการย้อนหลังสูงสุด 3 รายการ)
- **Smart Queue Processing:** ระบบจัดเรียงลำดับวิชาที่ลงทะเบียน โดยให้ความสำคัญกับวิชาเรียนทฤษฎี (Sec/Lecture) ขึ้นก่อนวิชาปฏิบัติการ (Lab) อัตโนมัติ
- **Credit Calculation:** คำนวณและสรุปผลหน่วยกิตรวมทั้งหมดที่ลงทะเบียนสำเร็จ

## Data Structures & Algorithms Used
1. **Hash Table / Dictionary (`course_dict`)**
   - ใช้จัดเก็บและจัดกลุ่มรายวิชาตามรหัสวิชา (Key = Course Code, Value = List of Sections)
   - **Time Complexity:** $O(1)$ สำหรับการค้นหาวิชา ทำให้ระบบทำงานได้รวดเร็วแม้มีรายวิชาจำนวนมาก
2. **Stack (`history_stack`)**
   - ใช้ในการทำระบบ **Undo** (LIFO - Last In, First Out)
   - มีการจำกัดขนาดของประวัติไว้ที่ 3 รายการล่าสุดเพื่อประหยัดหน่วยความจำ
3. **Priority Queue / Min-Heap (`priority_queue`)**
   - ใช้จัดระเบียบและแสดงผลใบเสร็จการลงทะเบียน โดยใช้ `heapq` ในการสร้าง Min-Heap
   - กำหนด Priority ให้วิชาทฤษฎี (Sec) = 1 และวิชาปฏิบัติ (Lab) = 2 เพื่อบังคับให้วิชาทฤษฎีถูกประมวลผล (heappop) ออกมาก่อนเสมอ
4. **Lazy Deletion (`isActivate` flag)**
   - เทคนิคการลบข้อมูลแบบไม่รื้อโครงสร้าง เนื่องจาก Heap ไม่รองรับการลบข้อมูลตรงกลางคิวแบบ O(1)
   - เมื่อผู้ใช้กด Undo ระบบจะเปลี่ยนสถานะ `isActivate = False` แทนการดึงข้อมูลออกจาก Heap ตรงๆ และจะทำการกรองทิ้งในขั้นตอน `process_all()` เพื่อรักษาประสิทธิภาพของโปรแกรมให้ดีที่สุด

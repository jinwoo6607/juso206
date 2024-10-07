import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

class AddressBookDiary:
    def __init__(self, master):
        self.master = master
        self.master.title("주소록 및 다이어리")
        self.master.geometry("400x600")
        self.master.configure(bg="#f0f0f0")

        self.contacts = {}
        self.diary_entries = {}

        # 스타일 설정
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ADD8E6", foreground="black", font=('Arial', 10))
        self.style.map("TButton", background=[('active', '#87CEEB')], foreground=[('active', 'black')])

        # 주소록 UI
        ttk.Label(master, text="=== 주소록 ===", font=('Arial', 14)).pack(pady=10)
        
        ttk.Label(master, text="이름:").pack()
        self.entry_name = ttk.Entry(master)
        self.entry_name.pack(pady=5, padx=10)

        ttk.Label(master, text="전화번호:").pack()
        self.entry_phone = ttk.Entry(master)
        self.entry_phone.pack(pady=5, padx=10)

        ttk.Button(master, text="추가", command=self.add_contact).pack(pady=5)
        ttk.Button(master, text="찾기", command=self.find_contact).pack(pady=5)
        ttk.Button(master, text="수정", command=self.update_contact).pack(pady=5)
        ttk.Button(master, text="삭제", command=self.delete_contact).pack(pady=5)

        # 다이어리 UI
        ttk.Label(master, text="=== 다이어리 ===", font=('Arial', 14)).pack(pady=10)

        ttk.Label(master, text="날짜 (YYYY-MM-DD):").pack()
        self.entry_date = ttk.Entry(master)
        self.entry_date.pack(pady=5, padx=10)

        ttk.Label(master, text="메모:").pack()
        self.text_diary = scrolledtext.ScrolledText(master, width=40, height=10, font=('Arial', 10))
        self.text_diary.pack(pady=5, padx=10)

        ttk.Button(master, text="추가", command=self.add_diary_entry).pack(pady=5)
        ttk.Button(master, text="찾기", command=self.find_diary_entry).pack(pady=5)
        ttk.Button(master, text="수정", command=self.update_diary_entry).pack(pady=5)
        ttk.Button(master, text="삭제", command=self.delete_diary_entry).pack(pady=5)

    # 주소록 기능
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("정보", f"{name}이(가) 추가되었습니다.")
            self.clear_contact_entries()

    def find_contact(self):
        name = self.entry_name.get()
        if name in self.contacts:
            phone = self.contacts[name]
            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(0, phone)

    def update_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("정보", f"{name}의 전화번호가 수정되었습니다.")

    def delete_contact(self):
        name = self.entry_name.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("정보", f"{name}이(가) 삭제되었습니다.")
            self.clear_contact_entries()

    def clear_contact_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

    # 다이어리 기능
    def add_diary_entry(self):
        date = self.entry_date.get()
        entry = self.text_diary.get("1.0", tk.END).strip()
        if date and entry:
            self.diary_entries[date] = entry
            messagebox.showinfo("정보", f"{date}의 메모가 추가되었습니다.")
            self.clear_diary_entries()

    def find_diary_entry(self):
        date = self.entry_date.get()
        if date in self.diary_entries:
            entry = self.diary_entries[date]
            self.text_diary.delete("1.0", tk.END)
            self.text_diary.insert(tk.END, entry)

    def update_diary_entry(self):
        date = self.entry_date.get()
        entry = self.text_diary.get("1.0", tk.END).strip()
        if date in self.diary_entries:
            self.diary_entries[date] = entry
            messagebox.showinfo("정보", f"{date}의 메모가 수정되었습니다.")

    def delete_diary_entry(self):
        date = self.entry_date.get()
        if date in self.diary_entries:
            del self.diary_entries[date]
            messagebox.showinfo("정보", f"{date}의 메모가 삭제되었습니다.")
            self.clear_diary_entries()

    def clear_diary_entries(self):
        self.entry_date.delete(0, tk.END)
        self.text_diary.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookDiary(root)
    root.mainloop()

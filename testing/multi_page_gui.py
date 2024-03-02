# import tkinter as tk

# class MyApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Single Page Application")

#         # Create and pack a container frame
#         self.container = tk.Frame(root)
#         self.container.pack(fill=tk.BOTH, expand=True)

#         # Create pages
#         self.page1 = Page1(self.container, self)
#         self.page2 = Page2(self.container, self)

#         # Show the initial page
#         self.show_page(self.page1)

#     def show_page(self, page):
#         # Hide current page and show the new page
#         if hasattr(self, "current_page"):
#             self.current_page.pack_forget()
#         page.pack(fill=tk.BOTH, expand=True)
#         self.current_page = page

# class Page1(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         label = tk.Label(self, text="Page 1")
#         label.pack(pady=10)

#         # Button to switch to Page 2
#         button = tk.Button(self, text="Go to Page 2", command=lambda: controller.show_page(controller.page2))
#         button.pack(pady=10)

# class Page2(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller

#         label = tk.Label(self, text="Page 2")
#         label.pack(pady=10)

#         # Button to switch to Page 1
#         button = tk.Button(self, text="Go to Page 1", command=lambda: controller.show_page(controller.page1))
#         button.pack(pady=10)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MyApp(root)
#     root.geometry("400x300")
#     root.mainloop()

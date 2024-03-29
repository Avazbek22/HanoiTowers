import tkinter as tk

class TowerOfHanoi:
    def __init__(self, master, num_disks):
        self.master = master
        self.num_disks = num_disks
        self.canvas_width = 400
        self.canvas_height = 200
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.tower_a = [i for i in range(num_disks, 0, -1)]
        self.tower_b = []
        self.tower_c = []

        self.draw_towers()

    def draw_towers(self):
        self.canvas.delete("all")

        tower_width = 10
        tower_height = 150
        tower_padding = 50

        for tower, x_offset in zip([self.tower_a, self.tower_b, self.tower_c], [tower_padding, tower_padding*3, tower_padding*5]):
            x1 = x_offset
            y1 = self.canvas_height - tower_height
            x2 = x_offset + tower_width
            y2 = self.canvas_height

            self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

            disk_width_unit = tower_width / self.num_disks
            for i, disk_size in enumerate(tower):
                disk_width = (i + 1) * disk_width_unit
                x1 = x_offset + (tower_width - disk_width) / 2
                y1 = self.canvas_height - (i + 1) * (tower_height / self.num_disks)
                x2 = x_offset + (tower_width + disk_width) / 2
                y2 = self.canvas_height - i * (tower_height / self.num_disks)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    def move_disk(self, source, target):
        disk = source.pop()
        target.append(disk)
        self.draw_towers()
        self.master.update()
        self.master.after(1000)  # Adjust the delay as needed

    def hanoi(self, n, source, target, auxiliary):
        if n == 1:
            self.move_disk(source, target)
        else:
            # Рекурсивный вызов для перемещения дисков
            self.hanoi(n - 1, source, auxiliary, target)
            self.move_disk(source, target)
            self.hanoi(n - 1, auxiliary, target, source)

def main():
    num_disks = 4
    root = tk.Tk()
    root.title("Tower of Hanoi")

    hanoi_game = TowerOfHanoi(root, num_disks)
    hanoi_game.hanoi(num_disks, hanoi_game.tower_a, hanoi_game.tower_c, hanoi_game.tower_b)

    root.mainloop()

if __name__ == "__main__":
    main()
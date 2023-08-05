class Container:
    def __init__(self, x, y, width, height):
        self.x, self.y = (x, y)
        self.width, self.height = (width, height)
        self.color = 'White'
        self.border_color = 'Black'
        self.bordered = False
        self.border_width = 3
        self.elements = []

    def add(self, elem):
        self.elements.append(elem)
        elem.x = self.x
        print(f"Added {elem} to Container's element list!")

    def remove(self, elem):
        selected_elem = self.elements.count(elem)

        if selected_elem:
            self.elements.pop(selected_elem)
            print(f"Removed {selected_elem} from the containers element list!")

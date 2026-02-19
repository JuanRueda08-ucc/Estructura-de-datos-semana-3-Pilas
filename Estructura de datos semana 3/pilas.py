"""
Simulates a 3D printer that manages layers.
If a layer fails, it allows undoing operations until reaching a stable point where the printer functions correctly.

"""


class Stack:
    """Generic Stack implementation."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def print_stack(self):
        print("\nCurrent Stack State (Top -> Bottom):")
        if self.is_empty():
            print("  (Empty Stack)")
        else:
            # Show from last element (top) to first (bottom)
            for item in reversed(self.items):
                print(f"  | {item} |")
        print("-" * 30)


class Layer:
    """ Represents a 3D printing layer."""

    def __init__(self, number, content):
        self.number = number
        self.content = content

    def __str__(self):
        return f"Layer {self.number}: {self.content}"


class ThreeDPrinter:
    """
    Simulates a 3D Printer managing layers.
    If a layer fails, allows undoing to a stable point where the printer works correctly.
    """
    def __init__(self):
        self.layer_stack = Stack()
        self.layer_count = 0

    def add_layer(self, content):
        self.layer_count += 1
        new_layer = Layer(self.layer_count, content)
        print(f"--> Printing: {new_layer}")
        self.layer_stack.push(new_layer)

    def show_progress(self):
        self.layer_stack.print_stack()

    def handle_print_error(self):
        """Simulates an error: Removes layers until finding a stable one (or empty if severe)."""
        print("\n ALERT: Print error detected !")
        
        # Simulate removing the last 2 defective layers
        layers_to_remove = 2 
        
        for _ in range(layers_to_remove):
            removed_layer = self.layer_stack.pop()
            if removed_layer:
                print(f"<-- Removing defective layer: {removed_layer}")
            else:
                print("No more layers to remove.")
                break
        
        # Adjust layer count to resume from where we left off
        top_layer = self.layer_stack.top()
        if top_layer:
            self.layer_count = top_layer.number
            print(f"System stabilized. Last valid layer: {top_layer}")
        else:
            self.layer_count = 0
            print("System stabilized. Printing restarted from scratch.")


# Block Test
if __name__ == "__main__":
    printer = ThreeDPrinter()

    # 1. Start normal printing
    printer.add_layer("Solid Base")
    printer.add_layer("Bottom Infill")
    printer.add_layer("Walls Level 1")
    
    printer.show_progress()

    # 2. Continue printing
    printer.add_layer("Infill Level 1")
    printer.add_layer("Overhang Bridge (Unstable)") # Assumed to fail here
    
    printer.show_progress()

    # 3. An error occurs
    printer.handle_print_error()

    printer.show_progress()

    # 4. Retry printing with correction
    print("--- Retrying corrected print ---")
    printer.add_layer("Structural Support (Correction)")
    printer.add_layer("Overhang Bridge (Stable)")
    
    printer.show_progress()

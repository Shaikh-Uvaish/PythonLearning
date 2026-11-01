class TextEditor:
   
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def append(self, text):
        self.undo_stack.append(("append", text))
        self.document += text
        self.redo_stack.clear()

    def delete(self, count):
        count = min(count, len(self.document))
        deleted = self.document[-count:]
        self.undo_stack.append(("delete", deleted))
        self.document = self.document[:-count]
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return
        action, value = self.undo_stack.pop()
        if action == "append":
            self.document = self.document[:-len(value)]
        elif action == "delete":
            self.document += value
        self.redo_stack.append((action, value))

    def redo(self):
        if not self.redo_stack:
            return
        action, value = self.redo_stack.pop()
        if action == "append":
            self.document += value
        elif action == "delete":
            self.document = self.document[:-len(value)]
        self.undo_stack.append((action, value))

    def show(self):
        """Prints the current state of the document."""
        print(f"Document: '{self.document}'")


# Example usage
if __name__ == "__main__":
    editor = TextEditor()
    editor.append("Hello, ")
    editor.append("world!")
    editor.show()       # → "Hello, world!"
    editor.delete(6)
    editor.show()       # → "Hello,"
    editor.undo()
    editor.show()       # → "Hello, world!"
    editor.redo()
    editor.show()       # → "Hello,"

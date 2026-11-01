from collections import deque

class EventQueueSystem:
  
    def __init__(self):
        self.queue = deque()

    def add_event(self, event_name):
        """Add a new event to the back of the queue."""
        self.queue.append(event_name)
        print(f"✅ Event '{event_name}' added to the queue.")

    def process_event(self):
        """Process the event at the front of the queue."""
        if not self.queue:
            print("⚠️ No events to process.")
            return
        event = self.queue.popleft()
        print(f"🟢 Processing event: '{event}'")

    def cancel_event(self, event_name):
        """Cancel a specific event before it is processed."""
        if event_name in self.queue:
            self.queue.remove(event_name)
            print(f"❌ Event '{event_name}' canceled.")
        else:
            print(f"⚠️ Event '{event_name}' not found in the queue.")

    def list_events(self):
        """Display all events currently in the queue."""
        if not self.queue:
            print("📭 No pending events.")
        else:
            print("📋 Pending events:")
            for idx, event in enumerate(self.queue, start=1):
                print(f"   {idx}. {event}")


# Example usage
if __name__ == "__main__":
    system = EventQueueSystem()

    while True:
        print("\n=== Real-Time Event Processing System ===")
        print("1. Add Event")
        print("2. Process Event")
        print("3. List Events")
        print("4. Cancel Event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            event_name = input("Enter event name: ")
            system.add_event(event_name)
        elif choice == "2":
            system.process_event()
        elif choice == "3":
            system.list_events()
        elif choice == "4":
            event_name = input("Enter event name to cancel: ")
            system.cancel_event(event_name)
        elif choice == "5":
            print("👋 Exiting system...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

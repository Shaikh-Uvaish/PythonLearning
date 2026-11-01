def linear_search(customer_ids, target):
    """Perform a linear search to check if target ID exists."""
    for i in range(len(customer_ids)):
        if customer_ids[i] == target:
            return i 
    return -1  


def binary_search(customer_ids, target):
    low = 0
    high = len(customer_ids) - 1

    while low <= high:
        mid = (low + high) // 2
        if customer_ids[mid] == target:
            return mid
        elif customer_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1



if __name__ == "__main__":
    # List of customer IDs (unsorted for demo)
    customer_ids = [105, 102, 120, 110, 115, 101, 108]

    print("Customer Account IDs:", customer_ids)

    # Input target ID to search
    target = int(input("Enter the Customer Account ID to search: "))

    # ---- Linear Search ----
    print("\n🔍 Performing Linear Search...")
    pos = linear_search(customer_ids, target)
    if pos != -1:
        print(f"✅ Customer ID {target} found at position {pos} (Linear Search)")
    else:
        print(f"❌ Customer ID {target} not found (Linear Search)")

    # ---- Binary Search ----
    print("\n⚙️ Performing Binary Search (sorted list)...")
    sorted_ids = sorted(customer_ids)
    print("Sorted Customer IDs:", sorted_ids)
    pos = binary_search(sorted_ids, target)
    if pos != -1:
        print(f"✅ Customer ID {target} found at position {pos} (Binary Search)")
    else:
        print(f"❌ Customer ID {target} not found (Binary Search)")

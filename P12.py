def read_rainfall_data(file_path):
    rainfall = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                amount = float(line.strip())
                if amount < 0:
                    print("Rainfall amount cannot be negative. Skipping entry.")
                    continue
                rainfall.append(amount)
            except ValueError:
                print("Invalid input. Skipping entry.")
    return rainfall

def main():
    file_path = 'rainfall_data.txt'  # Replace with your file path
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    rainfall = read_rainfall_data(file_path)
    
    if not rainfall:
        print("No valid rainfall data found.")
        return
    
    highest = max(rainfall)
    lowest = min(rainfall)
    total = sum(rainfall)
    average = total / len(rainfall)
    
    highest_month = months[rainfall.index(highest)]
    lowest_month = months[rainfall.index(lowest)]
    
    print(f"Data list: {rainfall}")
    print(f"Highest: {highest_month} {highest}")
    print(f"Lowest: {lowest_month} {lowest}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()

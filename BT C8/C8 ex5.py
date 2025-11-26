def process_mailbox_data(filename):
    from_count = 0
    try:
        with open(filename, 'r') as file_handle:
            for line in file_handle:
                if line.startswith("From "):
                    from_count += 1
                    words = line.split()
                    if len(words) > 1:
                        sender_email = words[1]
                        print(sender_email)
                        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0 # Trả về 0 nếu có lỗi

    return from_count

file_name = input("Enter a file name: ")

total_from_lines = process_mailbox_data(file_name)

print(f"There were {total_from_lines} lines in the file with From as the first word")
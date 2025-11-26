def process_file_words(filename):
   
    word_list = [] 
    try:
        with open(filename, 'r') as file_handle:
            for line in file_handle:
                words = line.strip().split() 
                for word in words:
                    if word not in word_list:
                        word_list.append(word)
                        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    word_list.sort()
    return word_list
file_name = input("Enter file: ")
result_words = process_file_words(file_name)
if result_words:
    print(result_words)
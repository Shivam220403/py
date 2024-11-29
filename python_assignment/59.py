def split_list_into_chunks(my_list, chunk_size):
    return [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]


my_list = []
my_list = input("Enter a List: ").split(' ')

chunk_size = int(input("Enter the Chunk size: "))

chunks = split_list_into_chunks(my_list, chunk_size)
print(chunks)


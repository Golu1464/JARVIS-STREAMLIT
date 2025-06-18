
memory_data = []

def add_to_memory(msg):
    if len(memory_data) > 10:
        memory_data.pop(0)
    memory_data.append(msg)

def get_memory():
    return memory_data

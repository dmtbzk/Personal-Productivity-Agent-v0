memory = []

def save_memory(note: str):
    memory.append(note)
    return f"Memory saved: {note}"

def get_memory():
    return memory
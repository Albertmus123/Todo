def individual_serial(todo)-> dict:
    return {
        'id' : str(todo["_id"]),
        'title': todo['title'],
        'description': todo['description'],
        'completed' : todo["completed"]
    }

def list_of_todos(todos)-> list:
    return [individual_serial(todo) for todo in todos]
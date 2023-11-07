#Description: "Start a new chat with a user"

def start_new_chat(client):
    empty_thread = client.beta.threads.create()
    return empty_thread

# Retrieve previous chat/Thread

def get_chat(client, thread_id):
    thread = client.beta.threads.retrieve(thread_id)
    return thread

#Description: "Add a message to a chat/Thread" 

def add_message(client, thread, content):
    thread_message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role="user",
    content=content,
    )
    return thread_message

# Description: "Get the previous messages in a chat/Thread"
def get_messages_in_chat(client, thread):
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    return messages

# Description: "Run the thread with the assistant"
def run_chat(client, thread, assistant):
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    )
    return run

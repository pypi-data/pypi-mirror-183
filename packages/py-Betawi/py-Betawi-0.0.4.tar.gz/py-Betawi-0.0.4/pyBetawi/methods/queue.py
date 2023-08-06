class Queue(object):
    def __init__(self):
        self.queue = {}

    def add_to_queue(self, chat_id, songname, link, ref, type, quality):
        if chat_id in self.queue:
            chat_queue = self.queue[chat_id]
            chat_queue.append([songname, link, ref, type, quality])
            return int(len(chat_queue) - 1)
        self.queue[chat_id] = [[songname, link, ref, type, quality]]
    
    
    def get_queue(self, chat_id):
        if chat_id in self.queue:
            return self.queue[chat_id]
        return 0
    
    
    def pop_an_item(self, chat_id):
        if chat_id not in self.queue:
            return 0
    
        chat_queue = self.queue[chat_id]
        chat_queue.pop(0)
        return 1
    
    
    def clear_queue(self, chat_id: int):
        if chat_id not in self.queue:
            return 0
    
        self.queue.pop(chat_id)
        return 1

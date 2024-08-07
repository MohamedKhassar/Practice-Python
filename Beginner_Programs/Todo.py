class Task():
    def __init__(self,title,content,priority,deadline):
        self.title=title
        self.content=content
        self.priority=priority
        self.deadline=deadline
    
    def get_task(self):
        print(f"""
. Title: {self.title}
. Content: {self.content}
. Priority: {self.priority}
. Deadline: {self.deadline}
              """)
    def update_task(self):
        data={
            "title":"",
            "content":"",
            "priority":"",
            "deadline":""
        }
        for dt in data:
            data[dt]=input(f"Enter new {dt}: ")
        
        if data["title"]:
            self.title=data["title"]
        if data["content"]:
            self.content=data["content"]
        if data["priority"]:
            self.priority=data["priority"]
        if data["deadline"]:
            self.deadline=data["deadline"]
        print("Task has been updated")

t1=Task("Implement User Authentication","Develop a user authentication system for the application. This includes setting up user registration, login, and logout functionalities. Ensure password security by using hashing and implement session management. Write tests to verify the authentication processes.","High","July 15, 2024")

t1.get_task()
t1.update_task()
t1.get_task()
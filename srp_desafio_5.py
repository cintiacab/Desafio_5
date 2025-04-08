
class TaskHandler:
    def send_report(self):
        self.__connect_api('Server connected')
        self.__create_task()
        self.__update_task()
        self.__remove_task()
        self.__send_notification()
        self.__generate_report()
        print("Report sent")

    def __connect_api(self, message: str):
        print(message)

    def __create_task(self):
        confirmation = "Task created"
        print(confirmation) 

    def __update_task(self):
        confirmation = "Task updated"
        print(confirmation)
    
    def __remove_task(self):
        confirmation = "Task removed"
        print(confirmation)
    
    def __send_notification(self):
        confirmation = "Notification sent"
        print(confirmation)

    def __generate_report(self):
        confirmation = "Report generated"
        print(confirmation)
        
task_handler = TaskHandler()
task_handler.send_report()
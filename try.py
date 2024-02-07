tasks= []
                        

def add_task():

    num_tasks = int(input("How many tasks you want to add? "))
    for i in range (num_tasks):
        task = input("Enter a new task ")
        tasks.append({"task": task, "Done": False})
        print("Task added successfully.")

def view_task():
    if len(tasks)== 0:
        print("no task.")
    else:
        print('List of tasks')

    for i, task in enumerate(tasks):
        status = "Done" if task["Done"] else "Not Done"
        print(f'{i+1}. {task["task"]} - {status}')


def update_tasks():

    task_index = int(input("Enter the task number to mark as complete ")) - 1
    if 0 <= task_index <= len(tasks):
        tasks[task_index]["Done"]  = True 


    
def delete_task(): 
    if len(tasks) == 0:
        print('no tasks to delete.')
       

    
    else:
        print('tasks:')

    choice = int(input('Enter the task to be deleted: '))

    if 0 < choice <= len(tasks):

        del tasks[choice - 1]
        
        print('Task deleted successfully.')
        
    else:
        print('invalid task number')



def main():

    

        while True:
            print('\n===== To-Do-List Application=====')
            print("1. Add task")
            print('2. View task')
            print('3. Delete task')
            print("4. Update tasks")
            print('5. Quit')

            choice = int(input("Enter your choice ")) 

            if choice == 1:
                add_task()

            elif choice ==2:
                view_task()
            elif choice==3:
                delete_task()
            elif choice == 4:
                update_tasks()

            elif choice ==5:
                print("Thank you for using the To Do list Application")
                break
            
            
    

        else:
            print('Invalid choice. Please try againa')
main()            


        








import requests

BACKEND_URL ="http://127.0.0.5000/tasks"


def update_task(ID, update_summary, update_description):
    update_task ={
        "update_summary": update_summary,
        "update_description": update_description
    }
    response



BACKEND_URL = "htp://127.0.0.1:5000/tasks"


def get_task_by_id(pk):
    single_task = task.select_by_id(pk)
    if not single_task:
        return{"ok": False, "message": "Not found"}, 404
    out = {
    "task": single_task,
    "ok": True
    }
    return out

def update_task(summmary, description):
    edit = {
        "summary: summary",
        "description: description"
    }
    response = requests.put(BACKEND_URL, jason=edit)
    if response .status_code == 204:
        print("Update succeeded")

    else:
        print("Update failed.")
    if __name__=="__main__":
        print("Fill out the prompt below to edit a task:")
        summary = input("Changed task summary: ")
        description = input("Changed task description ")
        update_task(summary, description)





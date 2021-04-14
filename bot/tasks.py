tasks = []


def createTaskSentence(task_list):
	sentence = ""
	for word in task_list:
		sentence += word + " "
	return sentence

def addTask(task):
	tasks.append(task)
	return "Tarea agregada!"

def deleteTask(index):
	assert isinstance(index,int), "index should be an integer value"
	if index>len(tasks):
		return "Numero invalido!"
	del tasks[index-1]

	return "Tarea " +str(index)+" eliminada :^("

def clearTasks():
	tasks.clear()
	return "Se han eliminado todas las tareas!"

def listAllTasks():

	if(not tasks):
		return "No hay tareas pendientes"

	tasks_list = ''
	for (i, task) in enumerate(tasks,start=1):
		tasks_list += str(i) + '. ' + task 
		if(i<len(tasks)):
			tasks_list += '\n'
	return tasks_list


# task-ruleset

A Python Package that acts as a scheduler for task and ruleset based parallel computation. Useful for highly parallel applications.

This package was created to help speed up time consuming activities in large software projects, such as waiting for HTTP response or DB operations.<br>
Most large software projects consist of chunks of code which are independent, but are still made to run in sequence.

Any algorithm can be divided into a set of steps, called Tasks. Some Tasks may need to be run in a particular order, and some may be run in any order.

We allow the users to define Tasks of several types, and a Rule for acting on each type of Task. These Rules may perform some computation and end their Task, and then may create one or more new Tasks of same or different types, or may not create any new Tasks and end the chain. All Tasks which exist at a given point in time must not depend on each other and will run in parallel.

Paralellism is achieved by creating a fixed number of sub-processes and scheduling the Tasks on those sub-processes.

### Usage Example

For detailed examples on how this project can be used, please check the folder named Examples on this project's [GitHub page](https://github.com/venunathan12/task-ruleset).<br>
It also contains full details on the example which will be discussed shortly.

For now, lets consider a simple use case. We wish to run a Google search for whole numbers from 1 to 64 and save the search result locally as a html page.<br>
This represents a usecase where one may need to make several HTTP requests, which are indepentent of each other.

The code for a parallel implementation of such use cases utilizing this package is shown below:

```python
import task_ruleset as trs
import __helper as h
import time; startTimeStamp = time.time()


# the list of numbers we wish to google
numsToPull = range(1, 64 + 1)


# The Generator which states how tasks of type 'init' need to be performed
# It yields when a new task is ready to start execution
def rule_init(TaskKey, TaskData):

    # create output folder
    outputPath = h.prepareOutputFolder()
    # record output path in a location accessible by all processes
    trs.CommonDict['OUTPUT_PATH'] = outputPath

    # for each number
    for num in numsToPull:
        
        # create new task of type 'proc', pass name of file to process as a param
        yield trs.Task("proc", f"proc_{num}", [num])

    # mark this task as completed
    return


# The Function which states how tasks of type 'proc' need to be performed
# It returns an empty list since it does not schedule more tasks
def rule_proc(TaskKey, TaskData):

    # get the number to google, from the params passed when creating the task
    num = TaskData[0]
    # get the output path recorded during execution of the initial task
    outputPath = trs.CommonDict['OUTPUT_PATH']
    
    # search for the number on google and get the search results
    processedData = h.googleSearchNumber(num)
    
    # save the search results to a file
    h.saveOutputFile(outputPath, num, processedData)

    # mark this task as completed
    return []


# Details about task organisation
trs.NGuests = 8                                 # State that the tasks need to be performed on 8 processes
trs.Rules["init"] = (0, rule_init)              # Declare that there is a task of type 'init' which needs 0 params
trs.Rules["proc"] = (1, rule_proc)              # Declare that there is a task of type 'proc' which needs 1 param
trs.InitTask = trs.Task("init", "init", [])     # State that initial task is of type 'init', and does not take any params

# Only the main thread should run this code
if __name__ == '__main__':
    
    # Start execution of the tasks, starting with trs.InitTask
    trs.main()
    
    # Record the number of tasks completed by each process
    print("main - Tasks completed by each process :", trs.TasksAssignedToProcess)

    # Record execution time
    print(f"Completed Execution in: {time.time() - startTimeStamp} secs")

```

The initial task is to create 64 new tasks, each of which is to perform a Google search.<br>
These 64 tasks are independent of each other, and are scheduled in parallel on 8 processes.

While testing, we observed roughly 7x speed up when using this parallelized program in place of the single threaded implementation.

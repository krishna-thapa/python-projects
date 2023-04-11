## Threading vs Multiprocessing

We have two common approaches to run code in parallel (achieve multitasking and speed up your program) : via threads or via multiple processes.

### Process
A Process is an instance of a program, e.g. a Python interpreter. They are independent from each other and do not share the same memory.

Key facts:
- A new process is started independently from the first process 
- Takes advantage of multiple CPUs and cores 
- Separate memory space 
- Memory is not shared between processes 
- One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation 
- Great for CPU-bound processing 
- Child processes are interruptable/killable 
- Starting a process is slower that starting a thread 
- Larger memory footprint 
- IPC (inter-process communication) is more complicated

### Threads
A thread is an entity within a process that can be scheduled for execution (Also known as "leightweight process"). A Process can spawn multiple threads. The main difference is that all threads within a process share the same memory.

Key facts:
- Multiple threads can be spawned within one process 
- Memory is shared between all threads 
- Starting a thread is faster than starting a process 
- Great for I/O-bound tasks 
- Leightweight - low memory footprint 
- One GIL for all threads, i.e. threads are limited by GIL 
- Multithreading has no effect for CPU-bound tasks due to the GIL 
- Not interruptible/killable -> be careful with memory leaks 
- increased potential for race conditions

### Threading in Python
Use the `threading` module.

Note: The following example usually won't benefit from multiple threads since it is CPU-bound. 
It should just show the example of how to use threads.

```
from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()
```

### When is Threading useful
Despite the GIL it is useful for I/O-bound tasks when your program has to talk to slow devices, like a hard drive or a network connection. With threading the program can use the time waiting for these devices and intelligently do other tasks in the meantime.

Example: Download website information from multiple sites. Use a thread for each site.

## Multiprocessing
Use the `multiprocessing` module. The syntax is very similar to above.

```
from multiprocessing import Process
import os


def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()
```

### When is Multiprocessing useful
It is useful for CPU-bound tasks that have to do a lot of CPU operations for a large amount of data and require a lot of computation time. With multiprocessing you can split the data into equal parts an do parallel computing on different CPUs.

Example: Calculate the square numbers for all numbers from 1 to 1000000. Divide the numbers into equal sized parts and use a process for each subset.

## GIL - Global interpreter lock
This is a mutex (or a lock) that allows only one thread to hold control of the Python interpreter. This means that the GIL allows only one thread to execute at a time even in a multi-threaded architecture.

#### Why is it needed?
It is needed because CPython's (reference implementation of Python) memory management is not thread-safe. Python uses reference counting for memory management. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count reaches zero, the memory occupied by the object is released. The problem was that this reference count variable needed protection from race conditions where two threads increase or decrease its value simultaneously. If this happens, it can cause either leaked memory that is never released or incorrectly release the memory while a reference to that object still exists.

#### How to avoid the GIL
The GIL is very controversial in the Python community. The main way to avoid the GIL is by using multiprocessing instead of threading. Another (however uncomfortable) solution would be to avoid the CPython implementation and use a free-threaded Python implementation like Jython or IronPython. A third option is to move parts of the application out into binary extensions modules, i.e. use Python as a wrapper for third party libraries (e.g. in C/C++). This is the path taken by numypy and scipy.

        
# More on Threading

## Create and run threads
You create a thread with `threading.Thread()`. It takes two important arguments:

`target`: a callable object (function) for this thread to be invoked when the thread starts
`args`: the (function) arguments for the target function. This must be a tuple
Start a thread with `thread.start()`

Call `thread.join()` to tell the program that it should wait for this thread to complete before it continues with the rest of the code.

## Share data between threads
Since threads live in the same memory space, they have access to the same (public) data. Thus, you can for example simply use a global variable to which all threads have read and write access.

Task: Create two threads, each thread should access the current database value, modify it (in this case only increase it by 1), and write the new value back into the database value. Each thread should do this operation 10 times.

## How to use Locks
Notice that in the above example, the 2 threads should increment the value by 1, so 2 increment operations are performed. But why is the end value 1 and not 2?

### Race condition
A race condition happened here. A race condition occurs when two or more threads can access shared data and they try to change it at the same time. Because the thread scheduling algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. In our case, the first thread accesses the database_value (0) and stores it in a local copy. It then increments it (local_copy is now 1). With our time.sleep() function that just simulates some time consuming operations, the programm will swap to the second thread in the meantime. This will also retrieve the current database_value (still 0) and increment the local_copy to 1. Now both threads have a local copy with value 1, so both will write the 1 into the global database_value. This is why the end value is 1 and not 2.

### Avoid race conditions with Locks
A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access to a resource in an environment where there are many threads of execution. A Lock has two states: locked and unlocked. If the state is locked, it does not allow other concurrent threads to enter this code section until the state is unlocked again.

Two functions are important:

- lock.acquire() : This will lock the state and block
- lock.release() : This will unlock the state again.

### Use the lock as a context manager
After lock.acquire() you should never forget to call lock.release() to unblock the code. You can also use a lock as a context manager, wich will safely lock and unlock your code. It is recommended to use a lock this way:
```
def increase(lock):
    global database_value 
    
    with lock: 
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
```

## Using Queues in Python
Queues can be used for thread-safe/process-safe data exchanges and data processing both in a multithreaded and a multiprocessing environment.

### The queue
A queue is a linear data structure that follows the First In First Out (FIFO) principle. A good example is a queue of customers that are waiting in line, where the customer that came first is served first.

### Using a queue in multithreading
Operations with a queue are thread-safe. Important methods are:

- q.get() : Remove and return the first item. By default, it blocks until the item is available.
- q.put(item) : Puts element at the end of the queue. By default, it blocks until a free slot is available.
- q.task_done() : Indicate that a formerly enqueued task is complete. For each get() you should call this after you are done with your task for this item.
- q.join() : Blocks until all items in the queue have been gotten and proccessed (task_done() has been called for each item).
- q.empty() : Return True if the queue is empty.

- The following example uses a queue to exchange numbers from 0...19. Each thread invokes the worker method. Inside the infinite loop the thread is waiting until items are available due to the blocking q.get() call. When items are available, they are processed (i.e. just printed here), and then q.task_done() tells the queue that processing is complete. In the main thread, 10 daemon threads are created. This means that they automatically die when the main thread dies, and thus the worker method and infinite loop is no longer invoked. Then the queue is filled with items and the worker method can continue with available items. At the end q.join() is necessary to block the main thread until all items have been gotten and proccessed.

### Daemon threads

In the above example, daemon threads are used. Daemon threads are background threads that automatically die when the main program ends. This is why the infinite loops inside the worker methods can be exited. Without a daemon process we would have to use a signalling mechanism such as a threading.Event to stop the worker. But be careful with daemon processes: They are abruptly stopped and their resources (e.g. open files or database transactions) may not be released/completed properly.
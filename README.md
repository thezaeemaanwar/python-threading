# 🪡 Python Threading
This repo contains my practice tasks for python threading.

## 📄 Description 

There are 3 threads created named
1. Thread1
2. Thread2
3. Thread3

### 1. Thread1
- prints acknowledge statement
- waits for 2 seconds
- wakes up

### 2. Thread2
- prints acknowledge statement
- waits for 1/2 seconds
- wakes up

### 3. Thread3
- prints acknowledge statement
- waits for 2 seconds
- wakes up 

### Main Process
- starts threads 
- sleeps for 5 seconds
- wakes up

## 🔍 Findings
- Threads are executed in the same process
- Threads share memory
- They have same Process IDs
- When a thread is idle, process executes some other threads e.g. When parent thread was sleeping, Thread1 started its execution. 



#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import TaskQueueManager
def main():
    print("Task Queue Manager Demo")
    q = TaskQueueManager()
    q.enqueue("default", "task1", priority=1)
    q.enqueue("default", "task2", priority=2)
    t = q.dequeue("default")
    print(f"Dequeued: {t.data if t else 'None'}")
    print("Done!")
if __name__ == "__main__": main()

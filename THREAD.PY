import time

import threading

 

thread_event = threading.Event()

 

def sleep_func():

    try:

        thread_event.set()

        print("sleep started")

        time.sleep(10)

        print("sleep is over")

    except Exception as e:

        print(f"exception in sleep_func: {str(e)}")

    finally:

        thread_event.clear()

 

def main_func():

    try:

        print("calling sleep_func in thread")

        sleepThread = threading.Thread(target=sleep_func)

        sleepThread.start()

        print("sleep thread started")

        # sleepThread.join()

        # if you want to do something immediatly after starting the thread

        while thread_event.is_set():

            # print("this should not print if join is called before while")

            # if you want to do something in parallel with thread

            pass

        # if you want to do something after thread is over

        print("this will print after event is clear")

    except Exception as e:

        print(f"exception in main_func: {str(e)}")

    finally:

        print("Finally is executed")

 

if __name__ == "__main__":

    main_func()
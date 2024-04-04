# src\useAxisZ\start_stop_AxisZ_pywinauto.py
import threading
import subprocess
import pywinauto


def terminate_process(process):
    """
    Function to terminate the child process gracefully.

    Args:
        process (subprocess.Popen): The child process object.
    """
    try:
        process.terminate()
    except ProcessLookupError:
        # Process might have already exited
        pass
    finally:
        # Wait for the process to finish (optional)
        process.wait()


def run_and_terminate(exe_path, timeout):
    """
    Executes the specified EXE, waits for timeout using a thread, and attempts to close the WPF window.

    Args:
        exe_path (str): Path to the executable file.
        timeout (int): Timeout duration in seconds.
    """

    process = None
    termination_event = threading.Event()

    def timeout_handler():
        nonlocal termination_event
        termination_event.set()

    timer_thread = threading.Timer(timeout, timeout_handler)
    timer_thread.start()

    try:
        # Start the child process
        process = subprocess.Popen(exe_path)

        # Wait for the process to finish or termination event to be set
        termination_event.wait()

        # Terminate the process if timeout occurred
        if not process.returncode:
            process.terminate()

        # Wait for the process to finish completely
        process.wait()

    except FileNotFoundError:
        print(f"Error: EXE '{exe_path}' not found.")
    finally:
        # Cancel the timer thread if it's still running
        timer_thread.cancel()

    # Attempt to close the WPF window (optional)
    close_wpf_app(wpf_title)  # Replace with actual title

    # ... (rest of the loop for multiple executions)


def close_wpf_app(title):
    """
    Attempts to close a WPF application by closing its main window.

    Args:
        title (str): Title of the WPF application window.
    """
    try:
        app = pywinauto.Application().connect(title=title)
        app.window(best_match=True).close()
    except pywinauto.ElementNotFoundError:
        print(f"WPF application window with title '{title}' not found.")


if __name__ == "__main__":
    # Replace 'path/to/your/exe.exe' with the actual path to your EXE
    exe_path = r"C:\Program Files\Axion BioSystems, Inc\AxIS Z\AxisZ.exe"
    timeout = 5 * 60  # 5 minutes in seconds
    num_executions = 12
    wpf_title = "AxIS Z – 3.12.1"  # Replace with actual title

    for _ in range(num_executions):
        run_and_terminate(exe_path, timeout)

        print(f"Execution {_ + 1} completed.")

    print("All executions finished.")

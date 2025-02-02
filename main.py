import src.task1_sequential as task1
import src.task2_threading as task2
import src.task3_multiprocessing as task3
import src.task4_performance_analysis as task4

print("\n--- Running Sequential Execution ---")
exec(open("src/task1_sequential.py").read())

print("\n--- Running Threading Execution ---")
exec(open("src/task2_threading.py").read())

print("\n--- Running Multiprocessing Execution ---")
exec(open("src/task3_multiprocessing.py").read())

print("\n--- Running Performance Analysis ---")
exec(open("src/task4_performance_analysis.py").read())


import sys
from typing import List, NamedTuple, Tuple


class AssemblyOperation(NamedTuple):
    name: str
    duration: int
    dependencies: Tuple[str, ...]

def minimum_assembly_time(ops: List[AssemblyOperation]) -> int:
    # Enter your code here: return an interger indicating the answer to the problem
    tasks_dic = {task.name: {'duration': task.duration, 'dependencies': task.dependencies} for task in ops }

    def get_dependencies_times(task: AssemblyOperation):
        dep_times = []
        if not task.dependencies:
            return 0
        for dep in task.dependencies:
            temp = AssemblyOperation(tasks_dic[dep],int(tasks_dic[dep]['duration']),tasks_dic[dep]['dependencies'])
            dep_time = tasks_dic[dep]['duration'] + get_dependencies_times(temp)
            dep_times.append(dep_time)
        return max(dep_times)
    all_task_times = []
    for item in ops:
        all_task_times.append(item.duration + get_dependencies_times(item))
    return max(all_task_times)


def main():
    ops = []
    # for line in sys.stdin:
    with open('data') as f:
        for line in f.readlines():
            # print(line)
            name, duration, *dependencies = line.rstrip().split()
            # print(name, duration, dependencies)
            ops.append(AssemblyOperation(name, int(duration), dependencies))
    # print('===============')
    # print(ops)
    print(minimum_assembly_time(ops))


if __name__ == "__main__":
    main()

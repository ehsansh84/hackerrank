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
        if 'dep_duration' in tasks_dic[task.name]:
            return tasks_dic[task.name]['dep_duration']
        for dep in task.dependencies:
            temp = AssemblyOperation(dep,int(tasks_dic[dep]['duration']),tasks_dic[dep]['dependencies'])
            # print(f'temp.name{temp.name}')
            dep_time = tasks_dic[dep]['duration'] + get_dependencies_times(temp)
            dep_times.append(dep_time)
        t = max(dep_times)
        # print(tasks_dic)
        # print(task.name)
        # print(tasks_dic[task.name])
        tasks_dic[task.name]['dep_duration'] = t
        return t
    all_task_times = []
    for item in ops:
        all_task_times.append(item.duration + get_dependencies_times(item))
    # print(tasks_dic)
    return max(all_task_times)


def main():
    ops = []
    # for line in sys.stdin:
    with open('data-tc12') as f:
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
